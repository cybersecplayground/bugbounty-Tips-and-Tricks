# 🎓 File Upload Bypass Techniques
![File Upload Bypass Techniques](https://github.com/user-attachments/assets/a8184def-c882-4d72-9be6-f247faf58c34)

**Advanced File Upload Security Bypasses**

---

## 🔥 The Challenge
Many web apps implement weak file upload validation that's surprisingly easy to bypass. Below are advanced techniques attackers use and how defenders should respond.

---

## 🛠 Common Weak Defenses
- **Content-Type Checking Only** — Trusts the `image/jpeg` header.
- **File Extension Filtering** — Blocks `.php` but misses tricks.
- **Client-Side Validation** — Easily bypassed with proxy tools.
- **Magic Bytes Only** — Checks file signature but may miss prepended payloads.

---

## ⚡️ Advanced Bypass Methods

### 1. Content-Disposition Double Extensions
```
Content-Disposition: form-data; name="file"; filename="image.jpg.php"
```
Some parsers treat the filename as `image.jpg` while the server uses the last extension `.php` for execution.

### 2. Case Manipulation
Try variants like:
- `file.pHp`
- `file.PHP`
- `file.PhP`

Some filters are case-sensitive.

### 3. Special Characters & Encoding
- `file.php%00.jpg` (null byte tricks in legacy parsers)
- `file.php.jpg` (parser confusion)
- `file.phphpp` (double extension obfuscation)

### 4. MIME Type Spoofing
Set `Content-Type: image/jpeg` while the file contains PHP:
- Prepend valid image headers (magic bytes) then add PHP payload.

---

## 🎯 Detection & Exploitation — Red Flags
Look for:
- Files containing `<?php` or `<%` in upload directories.
- Executable files in image/media folders.
- Filenames with double extensions or mixed-case extensions.
- Responses that include file processing output (errors, stack traces).

**Magic bytes limitations:**
- Detects file type but not executable content.
- Attackers can prepend valid image headers to bypass simple checks.

---

## 🛡 Secure Implementation Guide
1. **Server-Side File Type Verification** — Use robust libraries to inspect file contents, not just headers.
2. **Whitelist Extensions** — Only allow a small set of safe types (e.g., `.png`, `.jpg`, `.pdf`).
3. **Remove Execute Permissions** — Ensure upload directories cannot execute code.
4. **File Renaming** — Store files with generated names and discard original filenames.
5. **Content Scanning** — Scan for suspicious tokens like `<?php`, `<script>`, `eval(`.
6. **Virus/AV Scanning** — Integrate malware scanning for uploaded files.
7. **Serve via CDN or Object Storage** — Do not serve uploads directly from the web root.

---

## 💡 Pro Tips for Testers
- Test with mixed-case extensions (e.g., `pHp`, `AsPx`).
- Try Unicode/normalization attacks and URL-encoded payloads.
- Fuzz filename parsing and headers.
- Use Burp Suite, Postman, or curl to bypass client-side checks.

---

## ⚠️ Ethics & Legal
Use these techniques **only** on systems you own or are explicitly authorized to test. Unauthorized testing may be illegal and harmful.

---

🔔 Follow **@cybersecplayground** for daily security learning content!

**Tags:** `#WebSecurity` `#BugBounty` `#PenTesting` `#FileUpload` `#SecurityTesting`
