import os
from pathlib import Path
import re
import sys

def remove_obsidian_refs(content: str):
    pattern = r'!\[\[(.*?)\]\]'
    matches = []
    result = content
    current_position = 0
    
    while True:
        match = re.search(pattern, result[current_position:])
        if not match:
            break
            
        link = match.group(0)
        inner_text = match.group(1)

        matches.append(link)
        link_number = len(matches)
        start_pos = current_position + match.start()
        end_pos = current_position + match.end()
        result = result[:start_pos] + f'({inner_text})' + result[end_pos:]
        current_position = start_pos + len(f'[{link_number}]')
    
    return result, matches

def remove_double_dollars(content: str) -> str:
    pattern = r'\$\$(.*?)\$\$'
    matches = re.findall(pattern, content, re.DOTALL)
    for match in matches:
        cleaned_match = match.replace('\n', ' ').strip()
        content = content.replace(f'$${match}$$', f'${cleaned_match}$')
    return content

def convert_markdown_to_json_structure(content: str) -> str:
    lines = content.split('\n')
    current_level = 0
    stack = []
    result = []
    buffer = []
    
    def get_heading_level(line: str) -> int:
        if line.startswith('#'):
            return len(line) - len(line.lstrip('#'))
        return 0
    
    def flush_buffer() -> None:
        if buffer:
            if result:
                result.append(', ')
            result.append(', '.join(buffer))
            buffer.clear()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        heading_level = get_heading_level(line)
        
        if heading_level > 0:
            flush_buffer()
            
            while stack and stack[-1] >= heading_level:
                if result:
                    result.append('}')
                stack.pop()
            
            if result:
                result.append(', ')
            heading_text = line.lstrip('#').strip()
            result.append(f'==**{heading_text}**==:'+' {{')
            stack.append(heading_level)
        else:
            buffer.append(line)
    
    flush_buffer()
    
    while stack:
        result.append('}')
        stack.pop()
    
    return '{' + ''.join(result) + '}'



def concatenate_markdown_files(directory_path: str) -> str:
    combined_json = []
    
    dir_path = Path(directory_path)
    
    if not dir_path.is_dir():
        raise ValueError(f"Directory not found: {directory_path}")
    
    for file_path in sorted(dir_path.glob("*.md")):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                content = remove_double_dollars(content)
                json= convert_markdown_to_json_structure(content)
                combined_json.append(json)
                # if file_path.name != "Basics.md":
                #     break

        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
    
    return "\n\n".join(combined_json)

def main():
    print("WARNING: This script does not currently handle links in the best of ways and still needs improvement")
    if len(sys.argv) != 3:
        print("Usage: python generate_cheat_sheet.py <input_directory> <output_file>")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2])
    if not input_dir.is_dir():
        print(f"Error: Input directory '{input_dir}' does not exist or is not a directory")
        sys.exit(1)
    if output_file.exists():
        print(f"Error: Output file '{output_file}' already exists")
        sys.exit(1)

    content = concatenate_markdown_files(str(input_dir))
    content, links = remove_obsidian_refs(content)
    
    with open(output_file, "w") as f:
        f.write(content)
   
if __name__ == "__main__":
    main()