#!/usr/bin/env python3
"""Auto-format an article HTML into site template.

Examples:
  python3 scripts/format_article.py \
    --input "/Users/lumine/Downloads/raw.html" \
    --output "/Users/lumine/Desktop/personal-website/articles/my-note.html" \
    --type book --date "2024.06" --sync
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SUBTITLE_RE = re.compile(
    r'<p[^>]*class=["\'][^"\']*subtitle[^"\']*["\'][^>]*>(.*?)</p>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")

MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_MAP = {m.lower(): i + 1 for i, m in enumerate(MONTH_ABBR)}
MONTH_MAP.update(
    {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
    }
)


def strip_tags(text: str) -> str:
    out = TAG_RE.sub("", text)
    out = html.unescape(out)
    out = re.sub(r"\s+", " ", out).strip()
    return out


def clean_cjk_spaces(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    # Remove spaces accidentally inserted between CJK chars.
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    return text


def sanitize_inline(fragment: str) -> str:
    allowed = {"strong", "em", "u", "code", "br"}
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.DOTALL)

    def repl(match: re.Match[str]) -> str:
        whole = match.group(0)
        closing = whole.startswith("</")
        tag = match.group(1).lower()
        if tag not in allowed:
            return ""
        if tag == "br":
            return "<br>"
        return f"</{tag}>" if closing else f"<{tag}>"

    fragment = re.sub(r"</?([a-zA-Z0-9]+)(?:\s[^>]*)?>", repl, fragment)
    fragment = html.unescape(fragment)
    fragment = clean_cjk_spaces(fragment)
    return fragment


def extract_title(raw: str) -> str:
    patterns = [
        r'<h1[^>]*class=["\'][^"\']*page-title[^"\']*["\'][^>]*>(.*?)</h1>',
        r"<h1[^>]*>(.*?)</h1>",
        r"<title>(.*?)</title>",
    ]
    for p in patterns:
        m = re.search(p, raw, flags=re.IGNORECASE | re.DOTALL)
        if m:
            title = strip_tags(m.group(1))
            title = re.sub(r"\s+[—-]\s+Luminescence$", "", title).strip()
            if title:
                return title
    return "Untitled"


def extract_notion_property(raw: str, key: str) -> str:
    m = re.search(
        rf"<tr[^>]*>\s*<th[^>]*>.*?{re.escape(key)}.*?</th>\s*<td[^>]*>(.*?)</td>\s*</tr>",
        raw,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return strip_tags(m.group(1)) if m else ""


def extract_subtitle(raw: str) -> str:
    m = SUBTITLE_RE.search(raw)
    if not m:
        return ""
    return strip_tags(m.group(1))


def infer_type(type_text: str) -> tuple[str, str]:
    t = type_text.lower()
    if "research" in t:
        return "research", "Research"
    if "film" in t:
        return "film", "Film Note"
    return "book", "Book Note"


def parse_date(raw: str) -> str:
    v = raw.strip().replace("@", "")
    if not v:
        return ""

    # Jan 2024
    m = re.fullmatch(r"([A-Za-z]+)\s+(\d{4})", v)
    if m:
        month = MONTH_MAP.get(m.group(1).lower())
        if month:
            return f"{MONTH_ABBR[month-1]} {m.group(2)}"

    # 2024.06
    m = re.fullmatch(r"(\d{4})\.(\d{1,2})", v)
    if m:
        month = int(m.group(2))
        if 1 <= month <= 12:
            return f"{MONTH_ABBR[month-1]} {m.group(1)}"

    # 2024年6月
    m = re.fullmatch(r"(\d{4})年\s*(\d{1,2})月", v)
    if m:
        month = int(m.group(2))
        if 1 <= month <= 12:
            return f"{MONTH_ABBR[month-1]} {m.group(1)}"

    # January 6, 2024
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            dt = datetime.strptime(v, fmt)
            return f"{MONTH_ABBR[dt.month-1]} {dt.year}"
        except ValueError:
            pass

    return v


def extract_main_body(raw: str) -> str:
    # Existing site article.
    m = re.search(
        r'<div[^>]*class=["\'][^"\']*article-body[^"\']*["\'][^>]*>(.*)</div>\s*<script',
        raw,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        section = m.group(1)
        section = re.sub(
            r'<div[^>]*class=["\'][^"\']*article-meta[^"\']*["\'][^>]*>.*?</div>',
            "",
            section,
            count=1,
            flags=re.IGNORECASE | re.DOTALL,
        )
        return section

    # Notion exported article.
    m = re.search(
        r'<div[^>]*class=["\'][^"\']*page-body[^"\']*["\'][^>]*>(.*)</div>\s*</article>',
        raw,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        section = m.group(1)
        section = re.sub(
            r'<nav[^>]*class=["\'][^"\']*table_of_contents[^"\']*["\'][^>]*>.*?</nav>',
            "",
            section,
            flags=re.IGNORECASE | re.DOTALL,
        )
        return section

    return raw


def extract_blocks(section_html: str) -> list[tuple[str, str | list[str]]]:
    blocks: list[tuple[str, str | list[str]]] = []
    for m in re.finditer(
        r"<(h2|h3|p|ul|blockquote)\b[^>]*>(.*?)</\1>",
        section_html,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        tag = m.group(1).lower()
        inner = m.group(2)
        if tag == "p":
            text = sanitize_inline(inner)
            if strip_tags(text):
                blocks.append(("p", text))
            continue
        if tag == "h2":
            text = strip_tags(inner)
            if text:
                blocks.append(("h2", text))
            continue
        if tag == "h3":
            text = strip_tags(inner)
            if text:
                blocks.append(("h3", text))
            continue
        if tag == "blockquote":
            text = sanitize_inline(inner)
            if strip_tags(text):
                blocks.append(("blockquote", text))
            continue
        if tag == "ul":
            lis = []
            for li in re.finditer(r"<li\b[^>]*>(.*?)</li>", inner, flags=re.IGNORECASE | re.DOTALL):
                text = sanitize_inline(li.group(1))
                if strip_tags(text):
                    lis.append(text)
            if lis:
                blocks.append(("ul", lis))

    return blocks


def render_blocks(blocks: list[tuple[str, str | list[str]]]) -> str:
    lines: list[str] = []
    for tag, content in blocks:
        if tag in {"h2", "h3", "p", "blockquote"}:
            lines.append(f"  <{tag}>{content}</{tag}>")
        elif tag == "ul":
            lines.append("  <ul>")
            for li in content:  # type: ignore[assignment]
                lines.append(f"    <li>{li}</li>")
            lines.append("  </ul>")
    return "\n".join(lines)


def slugify(text: str) -> str:
    t = text.strip().lower().replace(" ", "-")
    t = re.sub(r"[^\w\u4e00-\u9fff-]+", "", t)
    t = re.sub(r"-{2,}", "-", t).strip("-")
    return t or "article"


def build_html(title: str, type_label: str, date_text: str, body_html: str) -> str:
    subtitle = f"{type_label} · {date_text}" if date_text else type_label
    meta_date = f"    <span>{date_text}</span>" if date_text else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)} — Luminescence</title>
  <style>
    .page-header h1 {{
      font-family: var(--windsor) !important;
      letter-spacing: 0.04em !important;
      text-transform: none !important;
    }}
  </style>
  <link rel="stylesheet" href="../style.css">
  <style>
    .article-body {{
      max-width: 720px;
      margin: 0 auto;
      padding: 0 40px 100px;
      font-family: var(--windsor);
      color: rgba(255,255,255,0.85);
      line-height: 1.85;
    }}

    .article-meta {{
      font-family: var(--windsor);
      font-size: 14px;
      letter-spacing: 0.08em;
      color: rgba(255,255,255,0.5);
      margin-top: 24px;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}

    .article-meta span {{ margin-right: 22px; white-space: nowrap; }}

    .article-body h2 {{
      font-family: var(--windsor);
      font-size: 20px;
      letter-spacing: 0.04em;
      font-weight: normal;
      color: #fff;
      margin: 52px 0 18px;
    }}

    .article-body h3 {{
      font-family: var(--windsor);
      font-size: 15px;
      letter-spacing: 0.04em;
      font-weight: normal;
      font-style: italic;
      color: rgba(255,255,255,0.6);
      margin: 32px 0 12px;
    }}

    .article-body p, .article-body li, .article-body blockquote {{
      font-size: 16px;
      color: rgba(255,255,255,0.78);
    }}

    .article-body p {{ margin-bottom: 18px; }}

    .article-body ul {{
      padding-left: 20px;
      margin: 0 0 20px;
    }}

    .article-body li {{ margin-bottom: 12px; }}

    .article-body blockquote {{
      margin: 14px 0 20px;
      padding-left: 16px;
      border-left: 1px solid rgba(255,255,255,0.25);
      line-height: 1.9;
    }}

    .article-body strong {{
      color: rgba(255,255,255,0.94);
      font-weight: 600;
    }}
  </style>
</head>
<body>

<div id="page-fade"></div>

<nav class="nav">
  <a class="nav-logo" href="../index.html" onclick="fadeOut(event,'../index.html')">Luminescence</a>
  <a class="nav-back" href="../writings.html" onclick="fadeOut(event,'../writings.html')">← writings</a>
</nav>

<header class="page-header">
  <h1>{html.escape(title)}</h1>
  <p class="subtitle">{html.escape(subtitle)}</p>
</header>

<div class="article-body">

  <div class="article-meta">
{meta_date}
    <span>{html.escape(type_label)}</span>
  </div>

{body_html}

</div>

<script>
  function fadeOut(e, url) {{
    e.preventDefault();
    const fade = document.getElementById('page-fade');
    fade.classList.add('out');
    setTimeout(() => {{ window.location.href = url; }}, 580);
  }}
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Format one article to site template.")
    parser.add_argument("--input", required=True, type=Path, help="Source HTML path.")
    parser.add_argument("--output", type=Path, help="Output HTML path.")
    parser.add_argument("--title", help="Override title.")
    parser.add_argument("--type", choices=["research", "book", "film"], help="Override article type.")
    parser.add_argument("--date", help='Override date, e.g. "2024.06" or "Jun 2024".')
    parser.add_argument("--sync", action="store_true", help="Also sync writings.html after formatting.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Project root path.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    src = args.input.expanduser().resolve()
    if not src.exists():
        raise FileNotFoundError(f"Input file not found: {src}")

    raw = src.read_text(encoding="utf-8", errors="ignore")

    extracted_title = extract_title(raw)
    subtitle_text = extract_subtitle(raw)
    notion_type = extract_notion_property(raw, "Type")
    notion_completed = extract_notion_property(raw, "Completed")

    if args.type:
        type_key = args.type
        type_label = {"research": "Research", "book": "Book Note", "film": "Film Note"}[args.type]
    else:
        type_key, type_label = infer_type(subtitle_text or notion_type)

    if args.date:
        date_text = parse_date(args.date)
    else:
        date_guess = ""
        if "·" in subtitle_text:
            date_guess = subtitle_text.split("·", 1)[1].strip()
        elif "-" in subtitle_text:
            date_guess = subtitle_text.split("-", 1)[1].strip()
        date_text = parse_date(date_guess or notion_completed)

    title = args.title or extracted_title

    if args.output:
        output = args.output.expanduser().resolve()
    else:
        slug = slugify(src.stem if src.stem else title)
        output = root / "articles" / f"{slug}.html"

    section = extract_main_body(raw)
    blocks = extract_blocks(section)
    body_html = render_blocks(blocks)

    formatted = build_html(title=title, type_label=type_label, date_text=date_text, body_html=body_html)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(formatted, encoding="utf-8")

    print(f"Formatted article written to: {output}")

    if args.sync:
        sync_script = root / "scripts" / "sync_writings.py"
        try:
            result = subprocess.run(
                ["python3", str(sync_script), "--root", str(root)],
                check=True,
                capture_output=True,
                text=True,
            )
            if result.stdout.strip():
                print(result.stdout.strip())
        except subprocess.CalledProcessError as exc:
            reason = exc.stderr.strip().splitlines()[-1] if exc.stderr else str(exc)
            print(
                f"[WARN] 文章已格式化，但同步 writings 失败: {reason}",
                file=sys.stderr,
            )


if __name__ == "__main__":
    main()
