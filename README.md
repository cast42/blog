# Blog of cast42

[https://cast42.github.io/blog/](https://cast42.github.io/blog/)

To create an editor with the fast api editor run:

```bash
uv run fastapi dev src/blog/asgi.py
```

To preview the blog locally:

```bash
uv run mkdocs serve
```

To see the preview, open a browser to port 8000 on localhost [http://127.0.0.1:8000/blog/](http://127.0.0.1:8000/blog/)

Don't forget to add <!-- more --> to the end of the markdown!

RSS is rebuilt and checked on every deployment. Set `date: YYYY-MM-DD` in
each new post. To announce a later revision in the updated feed, use:

```yaml
date:
  created: 2026-09-07
  updated: 2026-09-08
```

Without an update date, RSS uses the creation date. Both feeds contain the
20 most recent posts for their respective dates. Posts with `draft: true`
are excluded. To check locally, run `uv run mkdocs build` followed by
`uv run python scripts/check_rss.py`.
