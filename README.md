# Importing Data — Class Starter

This repository contains a **demo** and **practice** set for a short lesson on importing different data types into Python (primarily with Pandas).

## Structure

```
importing-data-class/
├─ data/
│  ├─ demo/            # instructor-led
│  └─ practice/        # student exercise
├─ notebooks/
│  ├─ 01_demo.ipynb
│  └─ 02_exercises.ipynb
├─ src/
│  └─ util.py
├─ requirements.txt
└─ README.md
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate  # or use conda
pip install -r requirements.txt
```

## Demo outline

1. **CSV/TSV** — `pd.read_csv` with `sep`, `usecols`, `dtype`, `nrows`, `compression`.
2. **Excel** — `pd.read_excel` one sheet vs `sheet_name=None` for all sheets.
3. **JSON** — Python's `json` + `pd.json_normalize` for nested data.
4. **Plain text** — `open()` / context manager & `.read()` vs `.readlines()`.
5. **HTML tables** — `pd.read_html()` returns a *list* of DataFrames; select one by index or with `match=` / `attrs=`.

## Practice tasks (10–15 min)

Open *notebooks/02_exercises.ipynb* and complete the TODO cells:
- Load `practice/tsv/air_quality.tsv` as a DataFrame (tab-delimited), set `date` as the index.
- Read `practice/json/events.json`, flatten attendees to one row per person.
- Count lines that contain `"ERROR"` in `practice/text/log.txt`.
- Read all tables from `practice/html/wiki_table.html` and select the one with id `awards`.
- Load `practice/csv_gz/movies.csv.gz` (gzipped) and compute the average `imdb_rating`.
- (Optional) Read `practice/excel/sales_regions.xlsx` and join both sheets on `region`.

## Notes
- If Excel engines are unavailable in your environment, the Excel files may be omitted; install `openpyxl` to enable reading/writing `.xlsx`.
- Everything is small and self-contained so it works without internet access.
