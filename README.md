# markengine

Very simple website engine with pages as markdown files. Let's look at it!

## Main things

* Markdown2
* Pygments ([CSS colors](https://github.com/richleland/pygments-css))
* Jinja 2

## How to generate HTML files

In CLI (generate one selected .md file):

```bash
markdown2 --extras break-on-newline,tables,header-ids,code-friendly,fenced-code-blocks,footnotes,smarty-pants,metadata,tag-friendly,wiki-tables,cuddled-lists src/INDEX.md > build/INDEX.html
```

Python app (generate all .md files in all dirs):

```bash
python build.py
```

## My goals

* After pushing generate HTML files and test them in GitHub Actions.
* If tests are okay, deliver HTML files to server and start a Docker container.