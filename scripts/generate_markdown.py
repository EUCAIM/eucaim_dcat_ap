"""Convert class sheets of a DCAT-AP Excel workbook into Markdown tables."""

import argparse
from pathlib import Path

import pandas as pd

VOCAB_COLUMN = "Controlled vocabulary (if applicable)"

COLUMNS = [
    "Property label",
    "Definition",
    "Property URI",
    "Range",
    "Cardinality",
    "Usage note",
    VOCAB_COLUMN,
]

# Included after "Cardinality" when present in a sheet.
OPTIONAL_COLUMNS = ["Occurence", "EUCAIM Modification"]


def select_columns(df):
    """Return the output columns, adding optional ones present in the sheet."""
    optional = [col for col in OPTIONAL_COLUMNS if col in df.columns]
    pos = COLUMNS.index("Cardinality") + 1
    return COLUMNS[:pos] + optional + COLUMNS[pos:]


def merge_vocab_rows(df):
    """Merge continuation rows that only contain a controlled vocabulary value."""
    merged = []
    current = None

    for _, row in df.iterrows():
        vocab = row[VOCAB_COLUMN]

        is_cont = pd.notna(vocab) and all(
            pd.isna(v) or str(v).strip() == ""
            for col, v in row.items()
            if col != VOCAB_COLUMN
        )

        if is_cont and current is not None:
            existing = current[VOCAB_COLUMN]
            current[VOCAB_COLUMN] = (
                str(existing) + "\n" + str(vocab) if pd.notna(existing) else str(vocab)
            )
        else:
            if current is not None:
                merged.append(current)
            current = row.copy()

    if current is not None:
        merged.append(current)

    return pd.DataFrame(merged).reindex(columns=df.columns)


def to_markdown_cell(value):
    if pd.isna(value):
        return ""

    text = str(value).strip()
    text = text.replace("|", "\\|")
    text = text.replace("\n", "<br>")
    return text


def convert(excel_file, output_dir, classes_sheet="classes", sheets=None):
    output_dir.mkdir(parents=True, exist_ok=True)

    classes_df = pd.read_excel(excel_file, sheet_name=classes_sheet)
    sheet_names = sheets or classes_df["sheet_name"].tolist()

    for sheet_name in sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        df = df[select_columns(df)]
        df = merge_vocab_rows(df)
        df = df.map(to_markdown_cell)

        output_file = output_dir / f"{sheet_name}.md"
        output_file.write_text(df.to_markdown(index=False) + "\n", encoding="utf-8")

        print(f"Generated {output_file}")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("excel_file", type=Path, help="Path to the Excel workbook.")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("./markdown"),
        help="Directory for generated Markdown files (default: ./markdown).",
    )
    parser.add_argument(
        "--classes-sheet",
        default="classes",
        help="Sheet listing class sheets in a 'sheet_name' column (default: classes).",
    )
    parser.add_argument(
        "-s",
        "--sheet",
        action="append",
        dest="sheets",
        help="Convert only this sheet (repeatable). Defaults to all listed classes.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.excel_file.is_file():
        raise SystemExit(f"Error: file not found: {args.excel_file}")
    convert(args.excel_file, args.output_dir, args.classes_sheet, args.sheets)


if __name__ == "__main__":
    main()
