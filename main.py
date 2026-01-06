import argparse
from fetch_news import fetch_news
from deduplicate import deduplicate
from storage import save_to_json
from exporter import export_csv, export_excel

parser = argparse.ArgumentParser(description="News Aggregator CLI")
parser.add_argument("--keyword", help="Search keyword")
parser.add_argument("--source", help="News source")
parser.add_argument("--from-date", help="Start date (YYYY-MM-DD)")
parser.add_argument("--to-date", help="End date (YYYY-MM-DD)")
parser.add_argument("--export", choices=["csv", "excel"], help="Export format")

args = parser.parse_args()

articles = fetch_news(
    keyword=args.keyword,
    source=args.source,
    from_date=args.from_date,
    to_date=args.to_date
)

articles = deduplicate(articles)
save_to_json(articles)

if args.export == "csv":
    export_csv(articles)
elif args.export == "excel":
    export_excel(articles)

print(f"Fetched {len(articles)} unique articles")
