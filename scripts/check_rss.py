"""Check generated feeds against post dates before publishing."""

import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

import yaml


def timestamp(value):
    if isinstance(value, str):
        value = datetime.fromisoformat(value)
    if not isinstance(value, datetime):
        value = datetime.combine(value, datetime.min.time())
    return value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value


def check(site_dir):
    posts = []
    for path in Path("blog/posts").rglob("*.md"):
        text = path.read_text()
        if not text.startswith("---\n"):
            continue
        meta = yaml.safe_load(text.split("---", 2)[1])
        if meta.get("draft"):
            continue
        dates = meta["date"]
        created = dates["created"] if isinstance(dates, dict) else dates
        updated = (dates.get("updated") or created) if isinstance(dates, dict) else created
        title = meta.get("title") or next(line[2:] for line in text.splitlines() if line.startswith("# "))
        posts.append((title, timestamp(created), timestamp(updated)))

    for name, column in (("created", 1), ("updated", 2)):
        channel = ET.parse(Path(site_dir) / f"feed_rss_{name}.xml").getroot().find("channel")
        items = channel.findall("item")
        assert items, "Feed is empty"
        expected = sorted(posts, key=lambda post: post[column], reverse=True)[:20]
        actual = [(item.findtext("title"), parsedate_to_datetime(item.findtext("pubDate"))) for item in items]
        cutoff = expected[-1][column]
        required = {(post[0], post[column]) for post in posts if post[column] > cutoff}
        allowed = {(post[0], post[column]) for post in posts if post[column] >= cutoff}
        assert len(actual) == len(expected) and required <= set(actual) <= allowed, f"{name}: posts or dates differ from frontmatter"
        dates = [entry[1] for entry in actual]
        assert dates == sorted(dates, reverse=True), f"{name}: incorrect ordering"
        guids = [item.findtext("guid") for item in items]
        assert len(set(guids)) == len(items), "Duplicate GUIDs"
        for value in [channel.findtext("image/url"), *(item.findtext("link") for item in items)]:
            url = urlparse(value)
            assert url.scheme == "https" and url.netloc, f"Invalid URL: {value}"
        print(f"{name}: verified {len(items)} entries, dates, order, GUIDs and URLs")


if __name__ == "__main__":
    check(sys.argv[1] if len(sys.argv) > 1 else "site")
