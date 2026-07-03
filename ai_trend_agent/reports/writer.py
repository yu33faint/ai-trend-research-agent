from datetime import date
from pathlib import Path


def save_report(report):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    today = date.today()
    report_path = reports_dir / f"{today}.md"

    report_path.write_text(report, encoding="utf-8")

    return report_path