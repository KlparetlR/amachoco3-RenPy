import json
import re
from collections import defaultdict
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def parse_script_blocks(script_lines):
    # 脚本以 say 为区块分割
    blocks = []
    current_block = []
    for line in script_lines:
        if line.strip().startswith('say '):
            current_block.append(line)
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append(current_block)
    return blocks

def extract_say_text(say_line):
    # 正则提取所有字符串参数, 取最后一个就是原文/台词
    strs = re.findall(r'"((?:[^"\\]|\\.)*?)"', say_line)
    return strs[-1] if strs else ""

def preprocess_json(raw_json):
    # 生成 forbidden 集合(raw有立绘关键字重复)和 allow_map
    raw_map = defaultdict(list)  # raw => [(fname, rep, keyid)]
    for kid, entry in raw_json.items():
        for k, v in entry.items():
            if k == "raw":
                continue
            raw_map[ entry['raw'] ].append( (k, v, kid) )
    forbidden = set()
    allow_map = {}
    for rtxt, lst in raw_map.items():
        counter = defaultdict(set)
        for fname, rep, _ in lst:
            counter[fname].add(rep)
        conflicted = [fname for fname, reps in counter.items() if len(reps) > 1]
        if conflicted:
            forbidden.add(rtxt)
        else:
            allow_map[rtxt] = [ (fname, rep) for fname, rep, _ in lst ]
    return forbidden, allow_map

def apply_replacements_by_raw(block, raw_txt, allow_map, forbidden, log_list):
    if raw_txt in forbidden:
        log_list.append(f"【有raw和立绘文件名重复但值不同,需手工处理】: {raw_txt}")
        return block
    if raw_txt not in allow_map:
        return block
    block_str = "\n".join(block)
    replaced_any = False
    for fname, rep in allow_map[raw_txt]:
        pattern = re.escape(fname)
        new_fname = fname.replace("X", rep)
        if re.search(pattern, block_str):
            block_str = re.sub(pattern, new_fname, block_str)
            replaced_any = True
        else:
            log_list.append(f"【未匹配到:{fname}】 在区块/原文: {raw_txt[:20]} ...")
    return block_str.split('\n')

def process_script(script_text, json_text):
    script_lines = script_text.splitlines()
    repl_json = json.loads(json_text)
    forbidden, allow_map = preprocess_json(repl_json)
    blocks = parse_script_blocks(script_lines)
    log_list = []
    result_lines = []

    for block in blocks:
        # 找到say那行，提取原文
        for line in reversed(block):
            if line.strip().startswith('say '):
                say_txt = extract_say_text(line)
                break
        else:
            say_txt = ""
        # 模糊匹配找到对应raw
        best_id = None
        best_sim = 0
        matched_raw = ""
        for kid, entry in repl_json.items():
            sim = similar(say_txt, entry.get("raw", ""))
            if sim > best_sim:
                best_sim = sim
                best_id = kid
                matched_raw = entry.get("raw", "")
        if best_sim > 0.7 and matched_raw:
            block = apply_replacements_by_raw(block, matched_raw, allow_map, forbidden, log_list)
        result_lines.extend(block)
    return "\n".join(result_lines), log_list

if __name__ == "__main__":
    with open("AC3\\data01120.arc\\ac3_08harem.txt", encoding="utf-8") as f:
        script = f.read()
    with open("AC3\\后宫线.json", encoding="utf-8") as f:
        jsondata = f.read()
    new_script, logs = process_script(script, jsondata)
    with open("AC3\\data01120.arc\\ac3_08harem_patched.txt", "w", encoding="utf-8") as f:
        f.write(new_script)
    with open("patch_log.txt", "w", encoding="utf-8") as f:
        for l in logs:
            f.write(l+'\n')