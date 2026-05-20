#!/bin/bash

med-scraper scrape \
  --output ../../data/chunks.jsonl \
  --delay 0.7 \
  --language English
echo "Done."
