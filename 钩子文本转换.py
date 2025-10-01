import re
import json
import logging

logging.basicConfig(filename='extractor.log', level=logging.INFO, encoding='utf8', filemode='w')
log = logging.getLogger('extractor')

def load_folder_structure(path):
    with open(path, encoding='utf8') as f:
        return json.load(f)

def build_resource_matchers(fs):
    """
    fs: dict, e.g. {"kag": [...], "chi": [...], ...}
    返回: {"kag": ["kag01a_001", ...], ...}（全部小写）
    """
    all_resources = {}
    for group, names in fs.items():
        names_lower = [n.lower() for n in names]
        all_resources[group] = names_lower
    return all_resources

def to_x_key(resource_full):
    # 转换为通用key
    m = re.match(r'([a-z]+[0-9]{2})([ABCabc])[_](\d{3}[a-z]?|\d{3})$', resource_full, re.I)
    if not m:
        return None, None
    code, ab, suffix = m.groups()
    code = code.lower()
    abX = 'X'
    suffix = str(suffix)
    key = f"{code}{abX}_{suffix}"
    ab = ab.upper()
    return key, ab

def find_exact_resources(line, all_resources, wanted_groups=None):
    """
    优先精确匹配带a/h后缀的，如koh01b_102a。
    koh01b_102/ich04c_231等，如果后面正好被koh01b_102a覆盖，则不输出koh01b_102。
    """
    found = []
    line_lower = line.lower()
    matches = []

    for group, names in all_resources.items():
        if wanted_groups and group not in wanted_groups:
            continue
        # 优先匹配长的
        for n in sorted(names, key=lambda x: -len(x)):
            if n.endswith('base'):
                continue
            idx = line_lower.find(n)
            if idx >= 0:
                matches.append((idx, n, group))
    if not matches:
        return []
    matches.sort()  # 按行出现顺序

    used_indexes = set()
    found_names = []
    for idx, n, group in matches:
        # 检查长的是否已出现（比如koh01b_102a先于koh01b_102）
        dup = False
        # 如koh01b_102和koh01b_102a，koh01b_102a应排在前面，koh01b_102被a覆盖不能算
        for fn in found_names:
            if fn.startswith(n) and len(fn) > len(n):
                dup = True
                break
        if dup:
            continue
        # 尾a或h优先，koh01b_102被koh01b_102a覆盖则不要koh01b_102
        tailabs = ['a', 'h']
        m = re.match(r'(.+?)([ah])$', n)
        if m:
            shortbase = m.group(1)
            if any(fn == shortbase for fn in found_names):
                found_names.remove(shortbase)
        found_names.append(n)

    for n in found_names:
        for group, names in all_resources.items():
            if n in names:
                found.append((n, group))
                break
    return found

def fuzzy_prefix_match(line, all_resources, valid_prefixes=None):
    """
    模糊前缀匹配。支持chi, ich, kag, koh, mik, nan, tuk。
    优先匹配同名资源，a/h尾部需与文本一致。
    """
    if valid_prefixes is None:
        valid_prefixes = ["chi","ich","koh","kag","mik","nan","tuk"]
    result = []
    # e.g. oh01b_102a -> koh01b_102a / kag01b_102a
    pat = r'\b([a-z]{2,3})\d{2}[abc]?_\d{3}[ah]?\b'
    for m in re.finditer(pat, line, re.I):
        fragment = m.group().lower()
        prefix = fragment[:3]
        if prefix in valid_prefixes:
            continue 
        body = fragment[3:]
        suffix_ah = ''
        sm = re.match(r'(.+?)([ah])$', fragment)
        if sm:
            suffix_ah = sm.group(2)
        for real_prefix in valid_prefixes:
            candidate = real_prefix + body
            for group, names in all_resources.items():
                if candidate in names:
                    if suffix_ah and not candidate.endswith(suffix_ah):
                        continue
                    result.append((candidate, fragment))
    return result

def extract_raw_after_s15(line):
    m = re.search(r'(?<=s15)[\+]*(.*)', line, flags=re.I)
    if m:
        raw = m.group(1).strip(' +')
        raw = raw.split('+', 1)[-1] if '+' in raw else raw
        return raw.strip()
    return ""

def line_s15_after_contains_resource(line_after_s15):
    return bool(re.search(r'[a-z]{3}\d{2}[abc]?_\d{3}[a-z]?', line_after_s15, re.I))

def main():
    folder_json = 'AC3\\AC3assets\\character\\character_list.json'
    input_text = 'AC3\\AC3catchinfo\\后宫线.txt'
    output_json = 'AC3\\后宫线.json'

    folder_struct = load_folder_structure(folder_json)
    all_resources = build_resource_matchers(folder_struct)
    output = {}
    line_no = 1

    with open(input_text, encoding='utf8') as fin:
        for line in fin:
            line = line.strip().replace('==================', '')
            if not line:
                continue
            m = re.search(r's00s01s02s03s04s05s06s07s08s09s10s11s12s13s14s15', line)
            if not m:
                continue

            found_full = find_exact_resources(line, all_resources)
            already_matched = set([x[0] for x in found_full])
            keydict = {}
            for resource_name, group in found_full:
                key, ab = to_x_key(resource_name)
                if not key: continue
                if key in keydict: continue
                keydict[key] = ab

            found_fuzzy = fuzzy_prefix_match(line, all_resources)
            for standard_name, bad_form in found_fuzzy:
                if standard_name in already_matched:
                    continue
                key, ab = to_x_key(standard_name)
                if not key: continue
                if key in keydict: continue
                keydict[key] = ab
                log.info(f"[容错-前缀fuzzy] line{line_no} {line.strip()} - 模糊前缀修正 {bad_form} -> {standard_name} => {key}")
            if keydict:
                after_s15 = line.split('s00s01s02s03s04s05s06s07s08s09s10s11s12s13s14s15', 1)[-1]
                if line_s15_after_contains_resource(after_s15):
                    log.warning(f"[特殊] line{line_no} s15后可能仍有立绘：{line.strip()}")
                raw_content = extract_raw_after_s15(line)
                outobj = {"raw": raw_content}
                outobj.update(keydict)
                output[str(line_no)] = outobj

            line_no += 1

    with open(output_json, 'w', encoding='utf8') as fout:
        json.dump(output, fout, ensure_ascii=False, indent=2)
    print(f"完成，输出到 {output_json}，详细日志见 extractor.log")

if __name__ == '__main__':
    main()