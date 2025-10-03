
# Sales CSV Cleanup — Runbook

This project demonstrates turning **5 messy sales CSVs** into **one clean master file** plus a basic **summary report**.

## Structure
```
sales_cleanup_project/
├─ data_raw/      # 5 messy CSV files (you can add more)
├─ data_clean/    # outputs will be written here
├─ scripts/
│  └─ clean_sales.py
└─ docs/
   └─ runbook.md  # this file
```

## Requirements
- Python 3.9+
- pip packages: `pandas`, `numpy`

## How to Run
1. Open a terminal in the `sales_cleanup_project/scripts` folder.
2. (Optional) Create a virtual env.
3. Install deps:
   ```bash
   pip install pandas numpy
   ```
4. Run the cleaner:
   ```bash
   python clean_sales.py
   ```

## What it does
- Standardizes column names, trims whitespace, fixes encodings
- Parses mixed date formats into ISO (YYYY-MM-DD)
- Normalizes quantities and currency-like numbers
- Recomputes incorrect line totals when possible
- Removes duplicates (exact + business-key level)
- Merges all raw CSVs into one: `data_clean/clean_sales.csv`
- Exports `data_clean/summary_report.csv` with month KPIs

## Deliverables to upload on Upwork
- **Before**: a small screenshot from `data_raw/*.csv`
- **After**: a snippet from `data_clean/clean_sales.csv` or `summary_report.csv`
- **Script**: show `scripts/clean_sales.py` (screenshot of top section)
- **Runbook**: this file

## Notes
- Add or replace files in `data_raw/` anytime—just rerun the script.
- Adjust thresholds or logic inside `clean_sales.py` to match a client's rules.
