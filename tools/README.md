# tools

- `check_index.py <x>_index.md <x>_full.md`: verifies every index line number points at the matching entry/heading in the full file and that every full-file entry is indexed. Run with `python3 -I`.
- `assemble_categories.py <dir>`: builds `<cat>_full.md` + `<cat>_index.md` from section files `<dir>/g/<cat>/s*.md` then `g*.md` (run from repo root; drops malformed or duplicate-name lines). Used to generate the 24 game-element categories.
