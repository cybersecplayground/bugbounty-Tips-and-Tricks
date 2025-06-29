# File Upload Vulnerabilities - Tips and Tricks

This repository contains a collection of techniques, payloads, and tricks related to file upload vulnerabilities encountered during bug bounty hunting and penetration testing.

## Contents

- **File Upload Bypass Techniques**: Various methods to bypass file upload restrictions
- **Malicious File Samples**: Example malicious files for testing upload functionality
- **Content-Type Bypasses**: Manipulating Content-Type headers to bypass checks
- **File Extension Tricks**: Uncommon file extensions and transformation techniques
- **Polyglot Files**: Files that are valid in multiple formats

## Common File Upload Bypass Methods

1. **Extension Blacklist Bypass**:
   - `file.php` → `file.php5`, `file.pHp`, `file.php%00.jpg`
   - Using uncommon extensions: `.phtml`, `.phar`, `.inc`

2. **Content-Type Manipulation**:
   - Changing `Content-Type: image/jpeg` for PHP files
   - Using `multipart/form-data` boundary manipulation

3. **Magic Byte Injection**:
   - Adding image headers (GIF, PNG, JPEG) to malicious files

4. **Path Traversal in Filename**:
   - `../../../malicious.php` in filename parameter

5. **Double Extension**:
   - `image.jpg.php`, `file.php.jpg`

## 🔥 Content Section
1 - [🧠 Unsafe File Upload → MIME Type Bypass](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/File%20upload/unsafe-file-upload.md)

## Disclaimer

These techniques should only be used on systems you have permission to test. Always get proper authorization before testing file upload functionality.
