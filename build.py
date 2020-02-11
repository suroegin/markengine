from pathlib import Path
from re import sub

from markdown2 import markdown
from jinja2 import Template

ROOT_DIR = Path(".")
SRC_DIR = ROOT_DIR / "src"
BUILD_DIR = ROOT_DIR / "build"
TEMPLATES_DIR = SRC_DIR / "templates"

with open(TEMPLATES_DIR / "base.html") as base_html:
    BASE_HTML = base_html.read()

# Create dirs
if not BUILD_DIR.exists():
    BUILD_DIR.mkdir()

if not (BUILD_DIR / "pages").exists():
    (BUILD_DIR / "pages").mkdir()


def convert(file):
    with open(file) as _file:
        data = sub("\.md", ".html", _file.read())
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
        metadata = html.metadata
        html = Template(BASE_HTML)\
            .render(
                context=html,
                title=metadata["title"]
        )

    path_for_html_file = \
        file.with_suffix(".html").parts[-1] \
        if str(file.parent) == "src" \
        else file.parts[-2] + "/" + file.with_suffix(".html").parts[-1]

    with open(ROOT_DIR / "build" / path_for_html_file, "w") as _file:
        _file.write(html)


# Convert .MD files to .HTML
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
    if d.is_dir() and "." not in d.name
    for f
    in d.iterdir()
    if f.match("*.md")
]
