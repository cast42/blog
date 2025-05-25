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
