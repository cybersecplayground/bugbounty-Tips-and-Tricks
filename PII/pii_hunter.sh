#!/bin/bash
# THEMSTER PII HUNTER - Recon & Leak Detection

domain=$1
mkdir -p pii-hunter/$domain && cd pii-hunter/$domain
gau $domain | tee all_urls.txt
cat all_urls.txt | grep -Ei '\.pdf|\.csv|\.zip|\.xls' > sensitive_files.txt
cat all_urls.txt | grep -Ei 'billing|invoice|account|contract|statement' > pii_paths.txt
cat pii_paths.txt | httpx -silent -mc 200 > live_pii.txt
mkdir -p downloads
while read url; do curl -s "$url" -o downloads/$(basename "$url"); done < sensitive_files.txt
grep -E -i -r 'email|@|address|ssn|iban|card|zip|payment|name|phone' downloads/ > suspected_pii.txt
