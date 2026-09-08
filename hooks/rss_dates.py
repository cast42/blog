"""Give RSS stable dates for both Material blog frontmatter formats."""

from datetime import date, datetime

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority


@event_priority(50)
def on_page_content(html, page, **kwargs):
    # Run before RSS collects the rendered post (default priority 0).
    if not page.file.src_uri.startswith("posts/") or page.meta.get("draft"):
        return html
    dates = page.meta.get("date")
    created = dates.get("created") if isinstance(dates, dict) else dates
    updated = (dates.get("updated") or created) if isinstance(dates, dict) else created
    for key, value in (("rss_created", created), ("rss_updated", updated)):
        if isinstance(value, str):
            try:
                value = datetime.fromisoformat(value)
            except ValueError as exc:
                raise PluginError(f"Invalid post date in {page.file.src_uri}: {value}") from exc
        if not isinstance(value, date):
            raise PluginError(f"Missing or invalid post date in {page.file.src_uri}")
        page.meta[key] = value
    return html
