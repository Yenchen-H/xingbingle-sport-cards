"""notes/*.md → html/*.html

把每份內容筆記套進同一個版型，確保每張圖卡風格一致。
用法：python scripts/build_html.py            （全部轉）
      python scripts/build_html.py notes/01-injury-prediction.md   （只轉一份）
"""
import re
import sys
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERIES = "星冰樂的運動科學手帳"


def parse_note(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    front, body = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S).groups()
    meta = {}
    for line in front.splitlines():
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"')
    sections = {}
    for block in re.split(r"\n## ", "\n" + body)[1:]:
        title, _, content = block.partition("\n")
        sections[title.strip()] = content.strip()
    meta["sections"] = sections
    return meta


def inline(s: str) -> str:
    """處理粗體與 [來源] 標記。"""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\[([^\]]+? \d{4})\]", r'<span class="cite">\1</span>', s)
    return s


def build(note: dict) -> str:
    sec = note["sections"]
    points = []
    for line in sec["三個重點"].splitlines():
        m = re.match(r"\d+\.\s+\*\*(.+?)\*\*[:：](.+)", line)
        if m:
            points.append((m.group(1), m.group(2).strip()))
    memo = [l[2:] for l in sec["研究小抄"].splitlines() if l.startswith("- ")]

    cat_svg = (ROOT / "style/xingbingle.svg").read_text(encoding="utf-8")
    prop_svg = (ROOT / f"style/props/{note['prop']}.svg").read_text(encoding="utf-8")

    pts_html = "\n".join(
        f'<div class="pt"><div class="num">{i}</div><div><h3>{html.escape(h)}</h3><p>{inline(p)}</p></div></div>'
        for i, (h, p) in enumerate(points, 1)
    )
    memo_html = "\n".join(f"<li>{inline(m)}</li>" for m in memo)

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<title>{note['id']} {html.escape(note['title'])}｜{SERIES}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style/card.css">
</head>
<body>
<div class="paper">
  <div class="tape l"></div><div class="tape r"></div>
  <div class="series">{SERIES}<b>No.{note['id']}</b></div>
  <h1>{html.escape(note['title'])}</h1>
  <div class="en">{html.escape(note['en'])}</div>

  <div class="def">{inline(sec['一句話定義'])}</div>

  <div class="points">
{pts_html}
  </div>

  <div class="bottom">
    <div class="memo"><h4>📒 研究小抄</h4><ul>
{memo_html}
    </ul></div>
    <div class="cat">
      <div class="bubble">{inline(sec['星冰樂小提醒'])}</div>
      <div class="mascot">{cat_svg}<div class="prop">{prop_svg}</div></div>
    </div>
  </div>

  <footer><span>{SERIES} · No.{note['id']}</span><span>來源：{html.escape(note['sources'])}</span></footer>
</div>
</body>
</html>
"""


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted((ROOT / "notes").glob("*.md"))
    for f in files:
        f = f if f.is_absolute() else ROOT / f
        out = ROOT / "html" / (f.stem + ".html")
        out.write_text(build(parse_note(f)), encoding="utf-8")
        print("✓", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
