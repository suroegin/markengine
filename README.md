# markengine

Very simple website engine with pages as markdown files. Let's look at it!

## Main things

* Markdown2
* Pygments ([CSS colors](https://github.com/richleland/pygments-css))

## How to generate HTML files

`markdown2 --extras break-on-newline,tables,header-ids, src/INDEX.md > build/INDEX.html`code-friendly,fenced-code-blocks,footnotes,smarty-pants,metadata,tag-friendly,wiki-tables,cuddled-lists