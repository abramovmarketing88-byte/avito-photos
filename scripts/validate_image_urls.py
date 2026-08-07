#!/usr/bin/env python3
"""Validate Avito ImageUrls cells: cloud-api format, count, varied firsts.

Usage:
  python validate_image_urls.py --xlsx path/to.xlsx --sheet "Кухонные гарнитуры-Кухни"
"""

from __future__ import annotations

import argparse
import re
from collections import Counter

import openpyxl

PREFIX = "https://cloud-api.yandex.net/v1/disk/resources/download?path="
CYRILLIC = re.compile(r"[А-Яа-яЁё]")


def headers_map(ws):
    return {
        str(ws.cell(2, c).value).strip(): c
        for c in range(1, ws.max_column + 1)
        if ws.cell(2, c).value
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--xlsx", required=True)
    p.add_argument("--sheet", required=True)
    p.add_argument("--expect", type=int, default=10)
    args = p.parse_args()

    wb = openpyxl.load_workbook(args.xlsx, data_only=True)
    ws = wb[args.sheet]
    h = headers_map(ws)
    url_col = h.get("Ссылки на фото") or h.get("ImageUrls")
    if not url_col:
        raise SystemExit("No ImageUrls column")

    firsts = Counter()
    bad = 0
    rows = 0
    for r in range(5, ws.max_row + 1):
        raw = ws.cell(r, url_col).value
        if not raw:
            continue
        parts = [x.strip() for x in str(raw).split("|") if x.strip()]
        rows += 1
        if len(parts) != args.expect:
            bad += 1
            print(f"R{r}: count={len(parts)}")
        for u in parts:
            if not u.startswith(PREFIX):
                bad += 1
                print(f"R{r}: bad prefix {u[:80]}")
            if CYRILLIC.search(u):
                bad += 1
                print(f"R{r}: cyrillic in path")
        if parts:
            firsts[parts[0].rsplit("/", 1)[-1]] += 1

    print(f"rows={rows} bad={bad} unique_firsts={len(firsts)}")
    if firsts:
        print("top firsts:", firsts.most_common(5))
        if len(firsts) == 1 and rows > 3:
            print("FAIL: all ads share the same first photo")
            raise SystemExit(1)
    wb.close()
    if bad:
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
