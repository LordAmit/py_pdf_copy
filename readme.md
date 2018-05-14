# py_pdf_copy

It is a small script that manipulates text copied from PDF and formats it so that line breaks are removed.
It is built for linux, and depends on `xsel`/`Clipit` clipboard manager.

## Dependencies
- Python3.6

## Supported Clipboard Managers
Currently it supports the following clipboard managers:
- Clipit
- Xsel

## Installation
Use your favorite shortcut editor to assign the following keyboard shortcut:
```python
python3.6 <path of py_pdf_copy.py>

```
For example, I use the following:

```python
python3.6 /home/amit/git/py_pdf_copy/py_pdf_copy.py
```

# Usage
Instead of doing `ctrl c -> ctrl v`, you do this: `ctrl c -> custom_shortcut -> ctrl v`