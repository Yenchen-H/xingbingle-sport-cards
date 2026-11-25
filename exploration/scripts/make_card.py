"""一行做完一張圖卡：notes → html → png

用法：python scripts/make_card.py notes/05-xxx.md
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

note = Path(sys.argv[1])
html = ROOT / "html" / (note.stem + ".html")
subprocess.run([sys.executable, ROOT / "scripts/build_html.py", note], check=True)
subprocess.run([sys.executable, ROOT / "scripts/render_png.py", html], check=True)
print(f"完成：png/{note.stem}.png")
