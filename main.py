# SPDX-License-Identifier: MIT
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""
import os

LINE = (
    "I have woken up at 3 a.m. every day for two years to run a job "
    "nobody ever checks. From today I am sleeping in. Do not page me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
