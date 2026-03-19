#!/usr/bin/env python3
"""Sync writings.html article list from local articles/*.html files.

Usage:
  python3 scripts/sync_writings.py
"""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path


AUTO_START = "<!-- AUTO-ARTICLES-START -->"
AUTO_END = "<!-- AUTO-ARTICLES-END -->"

TITLE_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
SUBTITLE_RE = re.compile(
    r'<p[^>]*class=["\'][^"\']*subtitle[^"\']*["\'][^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
ARTICLE_META_RE = re.compile(
    r'<div[^>]*class=["\'][^"\']*article-meta[^"\']*["\'][^>]*>(.*?)</div>',
    re.IGNORECASE | re.DOTALL,
)
SPAN_RE = re.compile(r"<span[^>]*>(.*?)</span>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")

MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


@dataclass
class Article:
    filename: str
    title: str
    type_key: str
    type_label: str
    date_display: str
    sort_key: int


def clean_text(fragment: str) -> str:
    text = TAG_RE.sub("", fragment)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_date(value: str) -> tuple[str, int]:
    value = value.strip()
    if not value:
        return "0000.00", 0

    m = re.fullmatch(r"(\d{4})\.(\d{1,2})", value)
    if m:
        year = int(m.group(1))
        month = int(m.group(2))
        if 1 <= month <= 12:
            return f"{year:04d}.{month:02d}", year * 100 + month

    m = re.fullmatch(r"(\d{4})年\s*(\d{1,2})月", value)
    if m:
        year = int(m.group(1))
        month = int(m.group(2))
        if 1 <= month <= 12:
            return f"{year:04d}.{month:02d}", year * 100 + month

    m = re.fullmatch(r"([A-Za-z]+)\s+(\d{4})", value)
    if m:
        month_word = m.group(1).lower()
        year = int(m.group(2))
        month = MONTHS.get(month_word, 0)
        if month:
            return f"{year:04d}.{month:02d}", year * 100 + month

    return value, 0


def infer_type(subtitle: str) -> tuple[str, str]:
    t = subtitle.lower()
    if "research" in t:
        return "research", "Research"
    if "book" in t:
        return "book", "Book Note"
    if "film" in t:
        return "film", "Film Note"
    return "research", "Research"


def parse_article(path: Path) -> Article | None:
    raw = path.read_text(encoding="utf-8", errors="ignore")

    title_match = TITLE_RE.search(raw)
    subtitle_match = SUBTITLE_RE.search(raw)
    if not title_match or not subtitle_match:
        return None

    title = clean_text(title_match.group(1))
    subtitle = clean_text(subtitle_match.group(1))
    type_key, type_label = infer_type(subtitle)

    date_candidate = ""
    if "·" in subtitle:
        date_candidate = subtitle.split("·", 1)[1].strip()
    elif "-" in subtitle:
        date_candidate = subtitle.split("-", 1)[1].strip()

    if not date_candidate:
        meta_match = ARTICLE_META_RE.search(raw)
        if meta_match:
            spans = SPAN_RE.findall(meta_match.group(1))
            if spans:
                date_candidate = clean_text(spans[0])

    date_display, sort_key = parse_date(date_candidate)

    return Article(
        filename=path.name,
        title=title,
        type_key=type_key,
        type_label=type_label,
        date_display=date_display,
        sort_key=sort_key,
    )


def build_items(articles: list[Article]) -> str:
    lines: list[str] = []
    for a in articles:
        lines.extend(
            [
                f'    <a class="article-item" href="articles/{a.filename}" data-type="{a.type_key}">',
                f"      <span class=\"article-title\">{html.escape(a.title)}</span>",
                f"      <span class=\"article-tag\">{a.type_label}</span>",
                f"      <span class=\"article-date\">{a.date_display}</span>",
                "    </a>",
                "",
            ]
        )
    if lines:
        lines.pop()
    return "\n".join(lines)


def sync(writings_path: Path, articles_dir: Path) -> int:
    articles: list[Article] = []
    for path in sorted(articles_dir.glob("*.html")):
        article = parse_article(path)
        if article:
            articles.append(article)

    articles.sort(key=lambda a: (a.sort_key, a.filename), reverse=True)
    items_html = build_items(articles)

    content = writings_path.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise RuntimeError(
            "writings.html 缺少自动区域标记。请添加 "
            f"{AUTO_START} 和 {AUTO_END}。"
        )

    insert_start = start_idx + len(AUTO_START)
    updated = content[:insert_start] + "\n" + items_html + "\n  " + content[end_idx:]
    writings_path.write_text(updated, encoding="utf-8")
    return len(articles)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync writings list from articles.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Project root path (default: script parent).",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    writings = root / "writings.html"
    articles = root / "articles"

    count = sync(writings, articles)
    print(f"Synced {count} article(s) into {writings}")


if __name__ == "__main__":
    main()
