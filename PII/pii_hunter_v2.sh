#!/bin/bash

# THEMSTER PII HUNTER - Enhanced Recon & PII Leak Detection Tool
# Requires: gau, httpx, ffuf, curl, grep, jq, parallel

# Color logging
info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
success() { echo -e "\033[1;32m[SUCCESS]\033[0m $1"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# Input validation
domain="$1"
if [[ -z "$domain" ]]; then
    error "Usage: $0 <domain>"
    exit 1
fi

# Directory setup
output_dir="pii-hunter/$domain"
mkdir -p "$output_dir/downloads"
cd "$output_dir" || exit 1

# Step 1: Grab archived URLs using gau
info "Fetching URLs from gau for $domain..."
gau "$domain" | sort -u | tee all_urls.txt > /dev/null

# Step 2: Extract sensitive filetypes
info "Filtering URLs with sensitive filetypes (.pdf, .csv, .zip, .xls)..."
grep -Ei '\.pdf|\.csv|\.zip|\.xls' all_urls.txt | sort -u > sensitive_files.txt

# Step 3: Extract PII-related paths
info "Extracting PII-related paths (billing, invoice, account, etc.)..."
grep -Ei 'billing|invoice|account|contract|statement|payment|userdata' all_urls.txt | sort -u > pii_paths.txt

# Step 4: Check which endpoints are live
info "Checking live URLs with httpx..."
httpx -silent -mc 200 < pii_paths.txt > live_pii.txt

# Step 5: Download sensitive files
info "Downloading exposed files..."
cat sensitive_files.txt | sort -u | parallel -j10 "curl -s {} -o downloads/\$(basename {})"

# Step 6: Scan for PII indicators
info "Scanning files for possible PII leaks (email, SSN, card data, etc.)..."
grep -E -i -r 'email|@|address|ssn|iban|card|zip|payment|name|phone|dob' downloads/ > suspected_pii.txt

# Optional summary
success "Scan complete for: $domain"
echo "--------------------------------------------------"
echo "Total URLs scanned: $(wc -l < all_urls.txt)"
echo "Sensitive files found: $(wc -l < sensitive_files.txt)"
echo "Live PII-related endpoints: $(wc -l < live_pii.txt)"
echo "Potential PII indicators: $(wc -l < suspected_pii.txt)"
echo "Results saved in: $output_dir"
echo "--------------------------------------------------"
