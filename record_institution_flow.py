import argparse
import csv
from datetime import date

from config import INSTITUTION_FLOW_FILE
from market_scanner import FLOW_COLUMNS, ensure_institution_flow_file, get_latest_institution_flow


def append_flow_row(args):
    ensure_institution_flow_file()
    row = {
        "date": args.date,
        "source_label": args.source,
        "source_url": args.source_url,
        "egyptian_institutions_net": args.egyptian_inst,
        "arab_institutions_net": args.arab_inst,
        "foreign_institutions_net": args.foreign_inst,
        "egyptian_individuals_net": args.egyptian_ind,
        "arab_individuals_net": args.arab_ind,
        "foreign_individuals_net": args.foreign_ind,
        "notes": args.notes,
    }
    with INSTITUTION_FLOW_FILE.open("a", newline="", encoding="utf-8") as handle:
        csv.DictWriter(handle, fieldnames=FLOW_COLUMNS).writerow(row)
    return row


def main():
    parser = argparse.ArgumentParser(description="Record EGX institution-flow data for the deterministic scanner.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Trading date, for example 2026-05-20.")
    parser.add_argument(
        "--source",
        choices=["OFFICIAL", "PUBLIC_REPORT", "MANUAL_IMPORT"],
        default="MANUAL_IMPORT",
        help="Source quality label.",
    )
    parser.add_argument("--source-url", default="", help="Optional official/report URL.")
    parser.add_argument("--egyptian-inst", type=float, required=True, help="Egyptian institutions net buy/sell in EGP.")
    parser.add_argument("--arab-inst", type=float, required=True, help="Arab institutions net buy/sell in EGP.")
    parser.add_argument("--foreign-inst", type=float, required=True, help="Foreign institutions net buy/sell in EGP.")
    parser.add_argument("--egyptian-ind", type=float, default=0, help="Egyptian individuals net buy/sell in EGP.")
    parser.add_argument("--arab-ind", type=float, default=0, help="Arab individuals net buy/sell in EGP.")
    parser.add_argument("--foreign-ind", type=float, default=0, help="Foreign individuals net buy/sell in EGP.")
    parser.add_argument("--notes", default="", help="Optional short note.")
    args = parser.parse_args()

    append_flow_row(args)
    flow = get_latest_institution_flow()
    print(f"Recorded institution flow for {args.date}.")
    print(f"Regime: {flow.get('regime')} | status: {flow.get('status')} | total institutions: {flow.get('total_institution_net'):.2f} EGP")


if __name__ == "__main__":
    main()
