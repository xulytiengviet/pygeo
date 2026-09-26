#!/usr/bin/env python3
"""Kiểm tra cấu trúc bản Việt hóa PyGeo mà không cài thư viện ngoài."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "index.md", ROOT / "GLOSSARY_VI.md"]
PAGES += [ROOT / f"day{day}.md" for day in range(1, 10)]
NOTEBOOKS = [ROOT / f"day{day}" / f"day{day}.ipynb" for day in range(1, 9)]
REQUIRED = PAGES + NOTEBOOKS + [
    ROOT / "README.md",
    ROOT / "_config.yml",
    ROOT / "_data" / "lessons.yml",
    ROOT / "_layouts" / "default.html",
    ROOT / "assets" / "css" / "pygeo.css",
]
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def check_markdown_links(source: Path) -> None:
    """Đảm bảo liên kết nội bộ trong các trang bài học không bị gãy."""
    for raw_url in LINK_PATTERN.findall(source.read_text(encoding="utf-8")):
        raw_url = raw_url.strip().split(" ", 1)[0].strip("<>")
        parsed = urlsplit(raw_url)
        if parsed.scheme or raw_url.startswith(("#", "mailto:", "//")):
            continue
        relative_path = unquote(parsed.path)
        if not relative_path:
            continue
        if relative_path.endswith(".html"):
            relative_path = relative_path[:-5] + ".md"
        destination = (source.parent / relative_path).resolve()
        if not destination.is_relative_to(ROOT):
            raise AssertionError(f"Liên kết vượt thư mục dự án: {source} -> {raw_url}")
        if not destination.exists():
            raise AssertionError(f"Liên kết hỏng: {source.relative_to(ROOT)} -> {raw_url}")


def check() -> None:
    missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
    if missing:
        raise AssertionError(f"Thiếu tệp: {', '.join(missing)}")

    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    layout = (ROOT / "_layouts" / "default.html").read_text(encoding="utf-8")
    assert 'baseurl: "/pygeo"' in config, "Sai đường dẫn GitHub Pages"
    assert '<html lang="vi">' in layout, "Thiếu ngôn ngữ tài liệu tiếng Việt"
    assert 'name="viewport"' in layout, "Thiếu khai báo tương thích điện thoại"

    for page in PAGES:
        content = page.read_text(encoding="utf-8")
        assert content.startswith("---\n"), f"Thiếu Jekyll front matter: {page}"
        assert "layout: default" in content.split("---", 2)[1], f"Sai layout: {page}"
        assert "github.com/geomorphlab/medaes/blob/" not in content, (
            f"Liên kết Notebook còn trỏ về kho gốc: {page}"
        )
        check_markdown_links(page)

    total_markdown_cells = 0
    for index, path in enumerate(NOTEBOOKS, start=1):
        book = json.loads(path.read_text(encoding="utf-8"))
        assert book["nbformat"] == 4, f"Notebook không đúng phiên bản: {path}"
        cells = book.get("cells", [])
        assert cells and cells[0]["cell_type"] == "markdown", (
            f"Thiếu phần giới thiệu tiếng Việt: {path}"
        )
        intro = "".join(cells[0]["source"])
        assert f"Bài {index}" in intro, f"Sai tiêu đề notebook: {path}"
        total_markdown_cells += sum(c["cell_type"] == "markdown" for c in cells)

    print(
        f"ĐẠT: {len(PAGES)} trang Markdown, {len(NOTEBOOKS)} Notebook, "
        f"{total_markdown_cells} ô Markdown; các liên kết nội bộ hợp lệ."
    )


if __name__ == "__main__":
    check()
