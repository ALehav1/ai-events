#!/usr/bin/env python3
"""Check all parsers for missing emerging_flagship field"""
import os
import re
from pathlib import Path

parsers_dir = Path("src/ai_events/fetch/parsers")
missing_field = []
total_parsers = 0

for parser_file in parsers_dir.glob("*.py"):
    if parser_file.name == "__init__.py":
        continue
    
    content = parser_file.read_text()
    
    # Check if file creates Event objects
    if "Event(" in content:
        total_parsers += 1
        # Check if emerging_flagship is mentioned
        if "emerging_flagship" not in content:
            missing_field.append(parser_file.name)
            print(f"Missing in {parser_file.name}")

print(f"\nTotal parsers checked: {total_parsers}")
if missing_field:
    print(f"Parsers missing emerging_flagship field: {len(missing_field)}")
    for parser in sorted(missing_field):
        print(f"  - {parser}")
else:
    print("All parsers have emerging_flagship field!")
