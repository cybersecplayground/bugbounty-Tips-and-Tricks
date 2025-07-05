
# 🔓 File Upload Bypass – Ultimate Tricklist for Hackers
**(Part 4 of file upload series)**

Many apps restrict certain file types to prevent RCE or LFI. But clever tricks can bypass blacklists & whitelists. Let's break it down 🧠👇

---

## 🔥 1. Blacklisting Bypass – Using Alternative Extensions

If `.php` is blocked, try:

```
.php, .php2, .php3, .php4, .php5, .php7, .phtml, .phar, .pht, .pgif, .shtml, .htaccess, .inc
```

**For other languages:**

- **ASP**: `.asp, .aspx, .asa, .cshtml`
- **JSP**: `.jsp, .jspx`
- **Coldfusion**: `.cfm, .cfc`
- **Perl**: `.pl, .cgi`

🌀 **Random capitalization also helps**:
```
.pHp, .pHP5, .PhAr
```

---

## ⚠️ 2. Whitelisting Bypass – Tricks That Confuse Filters

If `.php` is only allowed when disguised, try:

```
file.png.php
file.php%20
file.php%00
file.php%0a
file.php/
file.php.
file.php....
file.png.jpg.php
file.php#.png
file.php%00.png
file.phpJunk123png
```

📌 *Some filters only validate the extension before `%`, `#`, or null-byte (`%00`). Use it to your advantage!*

---

## 📁 Goal

Execute your payload on the server by bypassing faulty validation logic in the upload function.

Used with web shells or command injection for **Remote Code Execution (RCE)** 💥

---

💡 Share this with your hunting partner. Share it with someone who still thinks `.php` alone is enough 😏

🔐 Follow [@cybersecplayground](https://t.me/cybersecplayground) for more real-world web hacking tactics and tips.

---

#fileupload #bugbounty #cybersecurity #pentest #infosec #cybersecplayground #websecurity #rce #bypass #webhacking #tricks
