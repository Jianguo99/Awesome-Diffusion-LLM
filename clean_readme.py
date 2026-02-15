#!/usr/bin/env python3
"""
清理README.md文件
删除今天添加的不相关论文，只保留真正与diffusion language model相关的
"""

import re

def clean_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到Others部分
    others_start = content.find('## 7 Others <a id="others"></a>')
    if others_start == -1:
        print("❌ 未找到Others部分")
        return
    
    # 找到表格开始
    table_start = content.find('| Date       | Title', others_start)
    if table_start == -1:
        print("❌ 未找到表格")
        return
    
    # 找到表格结束（下一个##开始）
    next_section = content.find('\n## ', table_start)
    if next_section == -1:
        next_section = len(content)
    
    # 提取表格内容
    table_content = content[table_start:next_section]
    lines = table_content.split('\n')
    
    # 分析并过滤
    filtered_lines = []
    removed_2026_count = 0
    kept_2026_count = 0
    
    for line in lines:
        # 保留表头和分隔线
        if '| Date |' in line or '|---' in line or not line.strip():
            filtered_lines.append(line)
            continue
        
        # 检查是否是2026-02-15的论文
        if '2026-02-15' in line:
            # 检查是否与diffusion language model相关
            title_match = re.search(r'\|\s*2026-02-15\s*\|\s*(.+?)\s*\|\s*<details>', line)
            if title_match:
                title = title_match.group(1).lower()
                
                # 判断是否相关
                is_diffusion = 'diffusion' in title
                is_language_model = any(keyword in title for keyword in [
                    'language model', 'llm', 'large language model', 'text',
                    'natural language', 'nlp', 'transformer', 'attention'
                ])
                
                if is_diffusion and is_language_model:
                    filtered_lines.append(line)
                    kept_2026_count += 1
                    print(f"✅ 保留: {title[:60]}...")
                else:
                    removed_2026_count += 1
                    print(f"❌ 移除: {title[:60]}...")
            else:
                # 如果没有<details>标签，检查其他格式
                filtered_lines.append(line)
        else:
            # 保留非2026-02-15的论文
            filtered_lines.append(line)
    
    # 重建内容
    new_table_content = '\n'.join(filtered_lines)
    new_content = content[:table_start] + new_table_content + content[next_section:]
    
    # 写入文件
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n📊 清理完成:")
    print(f"  移除了 {removed_2026_count} 篇不相关的2026-02-15论文")
    print(f"  保留了 {kept_2026_count} 篇相关的2026-02-15论文")
    print(f"  文件已更新")

if __name__ == "__main__":
    clean_readme()