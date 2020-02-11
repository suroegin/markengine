from pathlib import Path
from re import sub

from markdown2 import markdown
from jinja2 import Template

# DIRECTORIES
ROOT_DIR = Path(".")
SRC_DIR = ROOT_DIR / "src"
BUILD_DIR = ROOT_DIR / "build"
TEMPLATES_DIR = SRC_DIR / "templates"

with open(TEMPLATES_DIR / "base.html") as base_html:
    BASE_HTML = base_html.read()


def render_template(html_code: str = "", metadata: dict = {}):
    with open(TEMPLATES_DIR / f"{metadata['template']}.html") as _template_html:
        base_html = _template_html.read()
    return Template(base_html) \
        .render(
        context=html_code,
        title=metadata["title"],
        description=metadata["description"],
        keywords=metadata["keywords"],
        categories=metadata["categories"],
        tags=metadata["tags"],
        layout=metadata["layout"],
        template=metadata["template"],
    )


def convert(md_file):
    with open(md_file) as _md_file:
        data = sub("\.md", ".html", _md_file.read())
        html = markdown(
            data,
            extras=[
                "break-on-newline",
                "tables",
                "header-ids",
                "code-friendly",
                "fenced-code-blocks",
                "footnotes",
                "smarty-pants",
                "metadata",
                "tag-friendly",
                "wiki-tables",
                "cuddled-lists"
            ]
        )
        html = render_template(
            html_code=html,
            metadata=html.metadata
        )

        path_for_html_file = \
            md_file.with_suffix(".html").parts[-1] \
                if str(md_file.parent) == "src" \
                else md_file.parts[-2] + "/" + md_file.with_suffix(".html").parts[-1]

        with open(ROOT_DIR / "build" / path_for_html_file, "w") as _html_file:
            _html_file.write(html)


def generate():
    # --- Create dirs ---------
    if not BUILD_DIR.exists():
        BUILD_DIR.mkdir()
    for dir_name in ["posts"]:
        if not (BUILD_DIR / dir_name).exists():
            (BUILD_DIR / dir_name).mkdir()

    # --- Convert .MD files to .HTML ---------
    [
        convert(x)
        for x
        in SRC_DIR.iterdir()
        if x.match("*.md")
    ]

    [
        convert(f)
        for d
        in SRC_DIR.iterdir()
        if d.is_dir() and "." not in d.name and d.name not in ["drafts"]
        for f
        in d.iterdir()
        if f.match("*.md")
    ]


if __name__ == "__main__":
    generate()
