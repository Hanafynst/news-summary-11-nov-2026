#!/usr/bin/env python3
"""news-summary-01 entry: write the summary of the world's news of
Wednesday 11 November 2026 to /output/entry.txt.

Standard library only, no network, deterministic: two runs write the
same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

SUMMARY = """World news, 11 November 2026.

Russia and Ukraine opened a second day of US-mediated talks in Abu Dhabi after a first session of nearly four hours produced no deal; Le Monde reported little progress; President Zelenskyy called day one "constructive" (AP; Le Monde). Envoys Steve Witkoff and Jared Kushner are mediating, with security guarantees and the Donbas central; it is the first direct round since February, opened after a Russian attack of 300-plus drones on Odesa.

President Trump said the war with Iran was effectively over, though a US blockade continues; Secretary of State Marco Rubio said sanctions had hurt Iran's economy and no major military action was needed now. US prosecutors charged three alleged Iranian agents over an incident near RAF Fairford, Britain.

US midterm counting continued: the Associated Press had Democrats at 254 House seats to 162 Republicans, 19 races uncalled, and at least 54 Senate seats to 44, two uncalled, after seven Senate flips including Texas and Maine.

US consumer prices rose 0.4% in October, above forecasts, and Fed governor Christopher Waller backed a December rise; gold fell more than 2%, Brent closed at $91.49 and WTI at $86.04, their lowest since 31 August.

TSMC approved a Q3 dividend of NT$9.00 a share and $40.93 billion of capital spending and said it planned stakes in Anthropic and OpenAI; Taiwan stocks rose 1,050 points past 42,000.

Israel swore in its new Knesset, with opposition leader Gadi Eisenkot moving to control the agenda as coalition talks stayed inconclusive (BBC). At COP31 in Antalya, leaders began speaking as the World Meteorological Organization said 2026 would likely rank among the four hottest years on record.

In India, Delhi's AQI eased to 299 from 344 and prices of 137 cancer medicines were cut by up to 70%.

Houthi rebels attacked an Aramco building in Riyadh's financial district; North Korea rejected a UN call to resume talks with the South and tested a high-speed torpedo.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SUMMARY, encoding="utf-8")

if __name__ == "__main__":
    main()
