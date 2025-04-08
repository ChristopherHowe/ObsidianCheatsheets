# Markdown Cheat Sheet Generator

A Python script that combines multiple Markdown files into a single structured cheat sheet. The script processes Markdown files from a specified directory and converts them into a JSON-like structure while handling special formatting.

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