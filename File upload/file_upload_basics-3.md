# 🔐 File Upload Bypass Techniques

**Uploading a web shell isn’t dead — just harder.**  
Here are **smart techniques** to bypass file upload restrictions and exploit insecure file handling on the backend.

---

## 🔎 1. Content-Type Bypass

Fake your file type with headers like:

```http
Content-Type: image/png
```

Then upload a `.php` or `.jsp` payload.  
Works if backend trusts headers blindly.

---

## 🧩 2. Double Extension Trick

```bash
shell.php.jpg  
shell.asp;.jpg  
shell.php%00.jpg  
```

Some servers check **only the last extension** or fail to handle null bytes properly.

---

## 📛 3. File Name Obfuscation

Try encoding or using special characters:

```
shell.pHp  
shell.ph%70  
```

Some filters are **case-sensitive** or don’t decode `%XX` values.

---

## 📂 4. MIME Sniffing Abuse

Upload as `.txt` or `.jpg` — but insert a **magic header** for interpretable content.  
Example: PHP payload inside a `.jpg`:

```php
<?php system($_GET['cmd']); ?>
```

If executed or served unsafely (e.g., Apache misconfig), it may run.

---

## 🚫 5. Extension Whitelist Bypass

Try using **allowed extensions** like:

```
.htaccess  
.shtm  
.svg  
.phtml  
.asp  
```

Some of these are **executable** on certain stacks (Apache, IIS, NGINX).

---

## 🧬 6. Polyglot Payloads

Build files that are **both valid images and code**:

- Image with PHP code appended
- PDF with JS payload
- GIF89a header + PHP backdoor

Works if server validates image by magic bytes only.

---

## 🚪 7. Upload to External Storage (S3, Cloudinary)

Sometimes upload is secure, but **URL is public and executable**.  
Check for direct-access URLs, bucket misconfigs, or SSRF chains.

---

## 🔐 Pro Tip

Always test for where the file is stored **AND** how it is handled or rendered.

---

## ✅ Stay Connected

Follow for more: **@cybersecplayground**

---

### 🏷️ Tags

`#FileUpload #FileUploadBypass #BugBountyTips #WebSecurity #CyberSecurity #HackingTools #InfoSec #Pentest #EthicalHacking #Payloads #CybersecPlayground`