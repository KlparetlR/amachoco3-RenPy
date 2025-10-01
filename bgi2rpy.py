import re,os,sys
def convert_to_renpy(input_file, output_file):
    CMD_PREVIOUS_PARAMS_CONFIG = {
        # 需要往回读取的 '@003f' 行数
        "_BustshotMotion": 3,
        "_EventCGMotion": 3,
        "_bseraseEx": 1,
        "_bserase": 1,
        "_bustshotFadein": 1
    }
    CMD_LOOKBACK_PARAMS_CONFIG = {
        # 需要往回读取的 '@003f' 行数
        "@0232": 2,
        "@0234": 2,
        "@0311": 2,
        "@0388": 1,
        "@0391": 1,
        "@0301": 2
    }
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("label start:\n")
        lines = [line.strip() for line in infile.readlines()]
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith("@003f") and (i + 1) < len(lines) and \
               lines[i+1].startswith("@007e") and "addr=" in lines[i+1]:
                next_line = lines[i+1]
                param_match = re.search(r'@003f\s*\[([^\]]+)\]', line)
                addr_match = re.search(r'addr=(0x[0-9a-fA-F]+)', next_line)
                if param_match and addr_match:
                    if addr_match.group(1) == '0x15d':
                        param = param_match.group(1).strip()
                        address_hex = addr_match.group(1).replace('0x', '')
                        outfile.write(f'    $ f_{address_hex}([{param}])\n')
                    i += 2
                    continue
            elif line.startswith("@001c"):
                match = re.search(r'@001c\s*\[([^\]]+)\]', line)
                if match:
                    params_str = match.group(1)
                    parts = [p.strip() for p in params_str.split(',')]
                    command = parts[-1].strip('"')
                    if command in CMD_PREVIOUS_PARAMS_CONFIG:
                        num_params_to_find = CMD_PREVIOUS_PARAMS_CONFIG[command]
                        command_params = parts[:-1]
                        previous_params = []
                        found_count = 0
                        search_index = i - 1
                        while search_index >= 0 and found_count < num_params_to_find:
                            prev_line = lines[search_index]
                            if prev_line.startswith("@003f") and not prev_line.startswith('@003f ["'):
                                param_match = re.search(r'@003f\s*\[([^\]]+)\]', prev_line)
                                if param_match:
                                    found_params = [p.strip() for p in param_match.group(1).split(',')]
                                    previous_params = found_params + previous_params
                                    found_count += 1
                            search_index -= 1
                        all_params = previous_params + command_params
                        outfile.write(f'    $ {command}([{", ".join(all_params)}])\n')
                    else:
                        renpy_params = parts[:-1]
                        outfile.write(f'    $ {command}([{", ".join(renpy_params)}])\n')
            elif any(line.startswith(cmd) for cmd in CMD_LOOKBACK_PARAMS_CONFIG.keys()):
                current_cmd = next(cmd for cmd in CMD_LOOKBACK_PARAMS_CONFIG.keys() if line.startswith(cmd))
                lookback = CMD_LOOKBACK_PARAMS_CONFIG[current_cmd]
                if i >= lookback and lines[i - lookback].startswith("@003f"):
                    prev_line = lines[i - lookback]
                    param_match = re.search(r'@003f\s*\[([^\]]+)\]', prev_line)
                    if param_match:
                        params_str = param_match.group(1)
                        command_number_str = current_cmd.replace('@', '')
                        command_number_int = int(command_number_str)
                        outfile.write(f'    $ f_{command_number_int}([{params_str}])\n')
            elif line.startswith("say"):
                match = re.search(r'say\s*\[([^\]]+)\]', line)
                if match:
                    params = [p.strip() for p in match.group(1).split(',')]
                    valid_params = []
                    for p in params:
                        if not p.startswith("addr=") and not (p.strip('"').isdigit() and p.strip('"') not in ['0', '1']):
                            valid_params.append(p)
                    if len(valid_params) >= 5:
                        selected_params = valid_params[-5:]
                        outfile.write(f'    $ _say([{", ".join(selected_params)}])\n')
                    else:
                        print(f"警告: (文件: {os.path.basename(input_file)}) 在行 '{line}' 发现无效的say参数，参数数量不足5个")
                        outfile.write(f"    # 原始行: {line}\n")
                        outfile.write(f"    $ _say([{', '.join(params)}])\n")
            i += 1

if __name__ == "__main__":
    input_folder = "AC3\\data01XXX"
    output_folder = "AC3\\data01XXX\\temp"
    if not os.path.isdir(input_folder):
        print(f"错误: 输入文件夹 '{input_folder}' 不存在。")
        print("请确保脚本与'AC3'文件夹在同一目录下，或者修改'input_folder'为正确的路径。")
        sys.exit(1)
    os.makedirs(output_folder, exist_ok=True)
    files_to_process = [f for f in os.listdir(input_folder) if f.endswith('.txt')]
    if not files_to_process:
        print(f"在文件夹 '{input_folder}' 中未找到任何 .txt 文件。")
    else:
        print(f"找到 {len(files_to_process)} 个文件，开始转换...")
        for filename in files_to_process:
            input_path = os.path.join(input_folder, filename)
            base_name = os.path.splitext(filename)[0]
            output_filename = f"{base_name}.rpy"
            output_path = os.path.join(output_folder, output_filename)
            print(f" - 正在转换: {filename} -> {output_filename}")
            convert_to_renpy(input_path, output_path)
        print(f"\n批量转换完成! 所有文件已保存至文件夹: {output_folder}")