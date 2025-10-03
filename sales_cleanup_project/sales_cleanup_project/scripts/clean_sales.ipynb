#!/usr/bin/env python3
"""
clean_sales.py
Reads raw CSVs from ./data_raw, cleans and merges them into ./data_clean/clean_sales.csv
Also writes ./data_clean/summary_report.csv with basic KPIs.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import re

RAW_DIR = Path(__file__).resolve().parent.parent / "data_raw"
OUT_DIR = Path(__file__).resolve().parent.parent / "data_clean"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def parse_money_like(x):
    if pd.isna(x):
        return np.nan
    s = str(x).strip()
    # remove currency symbols and spaces
    s = re.sub(r'[\$\€\£]', '', s)
    s = s.replace(' ', '')
    # handle commas as thousand separators or decimal separators
    # if there are two separators, first try standard, then swap
    try:
        return float(s.replace(',', ''))
    except:
        try:
            return float(s.replace('.', '').replace(',', '.'))
        except:
            return pd.NA

def normalize_qty(x):
    if pd.isna(x):
        return pd.NA
    s = str(x).strip()
    s = re.sub(r'[^\d]', '', s)
    return pd.to_numeric(s, errors='coerce')

def coalesce_columns(df, mapping):
    # mapping: canonical -> list of possible variants
    for canon, variants in mapping.items():
        for v in variants:
            if v in df.columns and canon not in df.columns:
                df.rename(columns={v: canon}, inplace=True)
    # if canon is still missing, create it
    for canon in mapping.keys():
        if canon not in df.columns:
            df[canon] = pd.NA
    return df

def load_and_clean_one(path):
    df = pd.read_csv(path, dtype=str, encoding="utf-8")
    # strip header whitespace
    df.columns = [c.strip() for c in df.columns]

    # coalesce column names
    mapping = {
        "order_id": ["order_id", " order_id "],
        "date": ["date", "Date"],
        "product": ["Product", "product"],
        "qty": ["qty", "quantity"],
        "unit_price": ["unit_price", "price"],
        "line_total": ["TOTAL", "TOTAL "],
        "customer_name": ["customer_name", "Customer", "customer"],
    }
    df = coalesce_columns(df, mapping)

    # trim whitespace in string columns
    for c in ["order_id","product","customer_name","date"]:
        df[c] = df[c].astype(str).str.strip()

    # parse numbers
    df["qty"] = df["qty"].apply(normalize_qty)
    df["unit_price"] = df["unit_price"].apply(parse_money_like)
    df["line_total"] = df["line_total"].apply(parse_money_like)

    # parse dates to ISO
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=False, infer_datetime_format=True)
    # fallback: try dayfirst if many NaT
    if df["date"].isna().mean() > 0.2:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    # recompute correct line_total when possible
    mask_ok = df["qty"].notna() & df["unit_price"].notna()
    df.loc[mask_ok, "line_total_clean"] = (df.loc[mask_ok, "qty"].astype(float) * df.loc[mask_ok, "unit_price"].astype(float)).round(2)
    # if original line_total missing or far off, replace
    def choose_total(row):
        t_orig = row.get("line_total", pd.NA)
        t_new = row.get("line_total_clean", pd.NA)
        try:
            if pd.isna(t_new):
                return t_orig
            if pd.isna(t_orig):
                return t_new
            # replace if difference > 2% or > 0.05 absolute
            if abs(float(t_orig) - float(t_new)) > max(0.05, 0.02*float(t_new)):
                return t_new
            return t_orig
        except:
            return t_new if not pd.isna(t_new) else t_orig
    df["line_total"] = df.apply(choose_total, axis=1)

    # final types
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce").astype("Int64")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["line_total"] = pd.to_numeric(df["line_total"], errors="coerce")
    df["date"] = df["date"].dt.date

    # Drop rows missing critical fields
    df = df.dropna(subset=["order_id","date","product","qty","unit_price"])

    # Standardize product casing
    df["product"] = df["product"].str.title()

    # Remove leading/trailing spaces on customer
    df["customer_name"] = df["customer_name"].str.strip()

    return df[["order_id","date","product","qty","unit_price","line_total","customer_name"]]

def main():
    paths = sorted(RAW_DIR.glob("*.csv"))
    if not paths:
        raise SystemExit("No raw CSVs found in ./data_raw")

    frames = [load_and_clean_one(p) for p in paths]
    df = pd.concat(frames, ignore_index=True)

    # Deduplicate exact duplicates
    before = len(df)
    df = df.drop_duplicates()
    exact_removed = before - len(df)

    # Deduplicate by business key (order_id + product + date)
    before = len(df)
    df = df.sort_values(["order_id","date","product"]).drop_duplicates(subset=["order_id","date","product"], keep="first")
    key_removed = before - len(df)

    # Save clean file
    out_path = OUT_DIR/"clean_sales.csv"
    df.to_csv(out_path, index=False)

    # Summary report
    summary = {}
    summary["rows_clean"] = int(len(df))
    summary["duplicates_removed_exact"] = int(exact_removed)
    summary["duplicates_removed_by_key"] = int(key_removed)
    summary["date_range"] = [str(df["date"].min()), str(df["date"].max())]
    summary["unique_customers"] = int(df["customer_name"].nunique())
    summary["unique_products"] = int(df["product"].nunique())
    summary["total_revenue"] = float(df["line_total"].sum(skipna=True))

    # KPIs by month
    df_month = df.copy()
    df_month["month"] = pd.to_datetime(df_month["date"]).dt.to_period("M").astype(str)
    kpi = df_month.groupby("month", as_index=False).agg(
        orders=("order_id","nunique"),
        revenue=("line_total","sum"),
        items=("qty","sum"),
    )
    kpi.to_csv(OUT_DIR/"summary_report.csv", index=False)

    # Write JSON summary
    pd.Series(summary).to_json(OUT_DIR/"summary.json")

    print("Wrote:", out_path)
    print("Wrote:", OUT_DIR/"summary_report.csv")
    print("Wrote:", OUT_DIR/"summary.json")

if __name__ == "__main__":
    main()
