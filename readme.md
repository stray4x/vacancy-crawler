# Djinni parser

A CLI tool for parsing Djinni job listings, ranking vacancies by keyword relevance, and analyzing technology trends via Stack Statistics mode.

## Options

```console
options:
  -h, --help            show this help message and exit
  --no-headless         Run browser in visible mode (default: headless)
  --path PATH           Set directory to save the output JSON file (default: ./)
  --out {file,print,both}
                        Output mode: save to file, print in terminal, or both (default: file)
  --limit NUMBER        Set number of recommended vacancies to return (default: 15)
  --stackstat, -sst     Stack statistics mode: show popularity stats for selected technologies.
```
