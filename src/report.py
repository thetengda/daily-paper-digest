import os
import re
from datetime import datetime
from typing import List, Dict

from .config import OUTPUT_DIR

Paper = Dict


def generate_daily_report(papers: List[Paper], summary_text: str, date_str: str) -> str:
    lines = []
    lines.append(f"# 每日文献速递 — {date_str}\n")
    lines.append(f"共检索到 {len(papers)} 篇相关文献  |  生成时间: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n")

    if summary_text:
        lines.append(summary_text)
    else:
        lines.append("## 全部文献\n")
        for i, p in enumerate(papers, 1):
            lines.append(f"{i}. **{p['title']}**  \n")
            lines.append(f"   作者: {', '.join(p['authors'][:3])}  |  来源: {p['source']}  \n")
            abstract = p.get("abstract", "")[:300]
            if abstract:
                lines.append(f"   摘要: {abstract}...  \n")
            lines.append(f"   链接: {p.get('link', '')}  \n")

    content = "\n".join(lines)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, f"{date_str}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def update_readme_index(date_str: str, filepath: str) -> None:
    index_path = os.path.join(OUTPUT_DIR, "README.md")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    header = """# 每日文献速递 索引

GNSS / 多源融合导航 / SLAM / 自动驾驶 相关文献每日自动检索与摘要。

"""

    new_entry = f"- [{date_str}]({date_str}.md)\n"

    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        if header in content:
            if new_entry in content:
                return
            existing = content
        else:
            existing = header + content
    else:
        existing = header

    entries = re.findall(r"- \[(\d{4}-\d{2}-\d{2})\]\(.*?\)", existing)
    entries = sorted(set(entries + [date_str]), reverse=True)
    lines = [f"- [{d}]({d}.md)" for d in entries]
    body = header + "\n".join(lines) + "\n"

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(body)
