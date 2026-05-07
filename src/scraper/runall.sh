#!/bin/bash

vendors=$(hw-scraper vendors)
IFS=', ' read -ra vendors_arr <<< "$vendors"
for i in "${vendors_arr[@]}"; do
  output_file="../../data/$i.json"
  hw-scraper scrape --vendor "$i" --limit 9999 --delay 0.7 --output "$output_file" &
done
wait
echo "Done."