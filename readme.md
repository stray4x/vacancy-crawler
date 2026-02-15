# Djinni parser

A CLI tool that parses Djinni job listings and generates a top 15 recommended vacancies list based on selected filters and keyword scoring.

## Options

```bash
options:
  -h, --help            show this help message and exit
  --no-headless         Run browser in visible mode (default: headless)
  --path PATH           Set directory to save the output JSON file (default: ./)
  --out {file,print,both}
                        Output mode: save to file, print in terminal, or both (default: file)
  --limit NUMBER        Set number of recommended vacancies to return (default: 15)
```
