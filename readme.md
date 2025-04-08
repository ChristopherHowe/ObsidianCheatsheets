# Markdown Cheat Sheet Generator

A Python script that combines multiple Markdown files into a single structured cheat sheet. The script processes Markdown files from a specified directory and converts them into a JSON-like structure while handling special formatting.

## Purpose
Commonly college professors allow the use of a cheat sheet for exams, while this commonly takes a lot of maual work to copy over all your notes and format it exactly how you want, what if you could just take all your structured obsidian notes and get a perfectly condensed single page containing all your hard thought out notes?

## Features

- Combines multiple `.md` files into a single output file
- Converts Markdown headings into a hierarchical structure
- Handles Obsidian-style image references
- Converts double-dollar math notation (`$$`) to single-dollar notation (`$`)
- Preserves heading hierarchy in the output

## Usage

```bash
python generate_cheat_sheet.py <input_directory> <output_file>
```
### Example
```bash
python generate_cheat_sheet.py "./math_notes" "./math_cheatsheet.md"
```

# Warning
Please only use as is allowed by instructor. Please use this at your own risk.