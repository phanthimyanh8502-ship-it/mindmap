#!/usr/bin/env python3
"""Nhúng mọi file nghiep-vu/**/quy-trinh-nghiep-vu.md vào mindmap-don-hang-v2.html và mindmap-don-hang.html (v1) (giữa 2 dấu DOCS:BEGIN / DOCS:END).
Chạy lại mỗi khi sửa quy-trinh-nghiep-vu.md:  python3 scripts/embed-docs.py"""
import json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
# Khóa = đường dẫn thư mục trong nghiep-vu/ (vd 05-GIAO-LAP-DAT/01-PHIEU-THI-CONG)
ct = root / 'nghiep-vu'
docs = {p.parent.relative_to(ct).as_posix(): p.read_text(encoding='utf-8') for p in sorted(ct.rglob('quy-trinh-nghiep-vu.md'))}
payload = json.dumps(docs, ensure_ascii=False).replace('</', '<\\/')
block = '<!-- DOCS:BEGIN -->\n<script type="application/json" id="docsData">' + payload + '</script>\n<!-- DOCS:END -->'
for html in (root / 'mindmap-don-hang-v2.html', root / 'mindmap-don-hang.html'):
    s = html.read_text(encoding='utf-8')
    s, n = re.subn(r'<!-- DOCS:BEGIN -->.*?<!-- DOCS:END -->', lambda m: block, s, flags=re.S)
    if n != 1:
        raise SystemExit('Không tìm thấy dấu DOCS:BEGIN / DOCS:END trong ' + html.name)
    html.write_text(s, encoding='utf-8')
    print(html.name + ':', f'đã nhúng {len(docs)} file')
