import re
import pathlib
import markdown2

ROOT_DIR = pathlib.Path(".")
SRC_DIR = ROOT_DIR / "src"
BUILD_DIR = ROOT_DIR / "build"

# Create dirs
if not BUILD_DIR.exists():
    BUILD_DIR.mkdir()

if not (BUILD_DIR / "pages").exists():
    (BUILD_DIR / "pages").mkdir()


def convert(file):
    with open(file) as _file:
        data = _file.read()

        # Change .md to .html
        [
            re.sub("\.md", ".html", data)
            for x
            in re.finditer("\[.+\]\(.+(\.md|\.MD)\)", data)
        ]

        print(data)  # TODO: don't change data... Hm...

        html = markdown2.markdown(
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


    path_for_html_file = file.with_suffix(".html").parts[-1] if str(file.parent) == "src" else file.parts[-2] + "/" + file.with_suffix(".html").parts[-1]
    with open(ROOT_DIR / "build" / path_for_html_file, "w") as _file:
        _file.write(html)


# Convert .MD files to .HTML
# [
#     convert(x)
#     for x
#     in SRC_DIR.iterdir()
#     if x.match("*.md")
# ]

[
    convert(f)
    for d
    in SRC_DIR.iterdir()
    if d.is_dir() and "." not in d.name
    for f
    in d.iterdir()
    if f.match("*.md")
]
