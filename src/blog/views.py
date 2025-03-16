import base64
import re
import shutil
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

import markdown
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

POSTS_DIR = Path("docs/posts")
if not POSTS_DIR.exists():
    POSTS_DIR.mkdir()


@app.get("/", response_class=HTMLResponse)
async def editor(request: Request):
    return templates.TemplateResponse("editor.html", {"request": request})


from pydantic import BaseModel


class PostData(BaseModel):
    title: str = ""
    content: str = ""


@app.post("/preview")
async def preview(data: PostData):
    html = markdown.markdown(
        data.content,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
            "markdown.extensions.codehilite",
            "markdown.extensions.nl2br",
            "markdown.extensions.sane_lists",
        ],
        output_format="html5",
    )
    return {"html": html}


def save_base64_image(base64_str, post_dir):
    """Save a base64 image to the post directory and return the relative path."""
    # Extract the actual base64 string and file type
    match = re.match(r"data:image/(\w+);base64,(.+)", base64_str)
    if not match:
        return None

    img_type, img_data = match.groups()

    # Create a filename based on timestamp to ensure uniqueness
    filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{img_type}"
    filepath = post_dir / filename

    # Decode and save the image
    with open(filepath, "wb") as f:
        f.write(base64.b64decode(img_data))

    return filename


@app.post("/save")
async def save_post(data: PostData):
    title = data.title.strip()
    content = data.content.strip()

    if not title or not content:
        raise HTTPException(status_code=400, detail="Title and content are required")

    # Create a safe directory name from the title
    dir_name = "".join(c for c in title.lower() if c.isalnum() or c in (" ",)).replace(
        " ", "-"
    )
    post_dir = POSTS_DIR / dir_name

    # If directory exists, add a timestamp to make it unique
    if post_dir.exists():
        dir_name = f"{dir_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        post_dir = POSTS_DIR / dir_name

    # Create post directory
    post_dir.mkdir(parents=True, exist_ok=True)

    # Process content for images
    def process_image_match(match):
        alt_text = match.group(1)
        image_src = match.group(2)

        # Handle base64 images
        if image_src.startswith("data:image"):
            filename = save_base64_image(image_src, post_dir)
            if filename:
                return f"![{alt_text}]({filename})"
            return match.group(0)

        # Handle URLs or local file paths
        if image_src.startswith(("http://", "https://", "file://")):
            try:
                # For local files, copy them to the post directory
                if image_src.startswith("file://"):
                    src_path = unquote(image_src[7:])
                    if Path(src_path).exists():
                        ext = Path(src_path).suffix
                        filename = (
                            f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
                        )
                        shutil.copy2(src_path, post_dir / filename)
                        return f"![{alt_text}]({filename})"
            except Exception as e:
                print(f"Error processing image {image_src}: {e}")
                return match.group(0)

        return match.group(0)

    # Update image references in content
    content = re.sub(r"!\[(.*?)\]\((.*?)\)", process_image_match, content)

    # Add metadata
    metadata = {
        "title": title,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "created_at": datetime.now().isoformat(),
        "last_modified": datetime.now().isoformat(),
    }

    # Save markdown file with metadata as YAML frontmatter
    post_path = post_dir / "index.md"
    post_path.write_text(
        "---\n"
        + "".join(f"{key}: {value}\n" for key, value in metadata.items())
        + "---\n\n"
        + content
    )

    return {
        "success": True,
        "path": post_path.relative_to(POSTS_DIR),
        "directory": dir_name,
    }


if __name__ == "__main__":
    import granian

    granian.run(app, host="0.0.0.0", port=8000)
