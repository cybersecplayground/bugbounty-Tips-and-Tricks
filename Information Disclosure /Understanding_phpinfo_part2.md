# 🎓 Part 2/3: Finding Exposed phpinfo() Files - Reconnaissance Techniques 🎓
![Finding Exposed phpinfo Files](https://github.com/user-attachments/assets/2ee617a1-ff7b-4abf-ac8e-eb38959a4f6e)

Now that you understand what phpinfo() reveals, let's explore how to find these exposed files across the internet and on target applications. This part focuses on active discovery methodologies.

---

## 🔥 Common phpinfo() Filename Patterns

Developers often use predictable names for test files. These are your primary targets:

```
info.php
phpinfo.php
test.php
phpinfo()
php-info.php
system.php
server.php
debug.php
php.php
i.php
info.php.bak
phpinfo.php.old
```

---

## 🛠 Discovery Method 1: Google Dorking

Use Google's advanced operators to find exposed phpinfo() files across the web:

```google
intitle:"phpinfo()" intext:"PHP Version" site:example.com
intitle:"phpinfo()" "PHP Version 8." -site:php.net
inurl:info.php "PHP Version"
inurl:phpinfo.php "PHP Version"
ext:php "PHP Version" "System" "Loaded Modules"
```

💡 **Why These Dorks Work:** The phpinfo() output has distinctive headers like **"PHP Version"** and **"System"** that search engines index.

---

## 🛠 Discovery Method 2: Directory Brute-Forcing

Use tools like ffuf, gobuster, or dirsearch to find phpinfo() files on target domains:

```bash
# FFUF with common phpinfo filenames
ffuf -w common_phpinfo_names.txt -u https://target.com/FUZZ -mc 200 -mr "PHP Version"

# Gobuster with extensions
gobuster dir -u https://target.com -w directory-list-2.3-medium.txt -x php -t 50

# Dirsearch with recursive scanning
python3 dirsearch.py -u https://target.com -e php -w /usr/share/wordlists/dirb/common.txt
```

### Custom Wordlist for phpinfo Hunting
```text
info.php
phpinfo.php
test.php
info.php.bak
phpinfo.php.old
debug.php
status.php
phpinfo
info
i.php
systeminfo.php
serverinfo.php
php-test.php
```

---

## 🛠 Discovery Method 3: Third-Party Dependencies

Many phpinfo() exposures come from bundled third-party libraries rather than the main application.

**Check these common paths:**

```
/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php
/vendor/phpunit/phpunit/tests/
/vendor/symfony/.../Tests/
/vendor/laravel/framework/tests/
/vendor/doctrine/tests/
/tests/
/test/
/examples/
/docs/
```

---

## ⚡️ Case Study: CVE-2023-49282 Exploitation Path

The vulnerable Amelia plugin exposed phpinfo() at:

```text
/wp-content/plugins/ameliabooking/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php
```

This demonstrates why you must scan deep into directory structures—not just the web root.

---

## 🛠 Discovery Method 4: Wayback Machine and Historical Data

Use tools like gau, waybackurls, or the Wayback Machine to find old phpinfo() files that might still exist:

```bash
# Gau (Get All URLs)
gau target.com | grep -i "phpinfo\|info.php"

# Waybackurls
echo target.com | waybackurls | grep "\.php" | sort -u

# Manual Wayback search
https://web.archive.org/web/*/target.com/*.php
```

---

## 🛠 Discovery Method 5: Automated Scanners

Security tools and vulnerability scanners actively detect phpinfo() files:

- Nessus Plugin ID 11229 — Web Server info.php / phpinfo.php Detection
- Tenable WAS Plugin 98223 — PHPinfo disclosure
- Nikto — includes phpinfo checks
- WPScan — detects vulnerable plugins exposing phpinfo()

**Detection indicators include:**

```
<title>phpinfo()</title>
<title>PHP Version ... - phpinfo()</title>
PHP Version
System
Configure Command
```

---

## 🎯 Priority Testing Checklist

When hunting for phpinfo() files, prioritize:

- Root directories — `/info.php`, `/phpinfo.php`, `/test.php`
- Framework paths — `/public/info.php`, `/app/webroot/info.php`
- Vendor directories — `/vendor/*/tests/*.php`
- Backup files — `.bak`, `.old`, `~`
- Documentation folders — `/docs/`, `/examples/`, `/samples/`
- CMS paths — `/wp-content/plugins/*/vendor/*/tests/*.php`

---

🔔 **Follow @cybersecplayground for Part 3: Exploiting phpinfo() — From Information Disclosure to Full Compromise!**

✅ **Like & Share if you're ready to turn recon into exploitation! 🚀**

```
#phpinfo #Reconnaissance #BugBounty #WebSecurity #InfoDisclosure #OSINT #FFUF #DirectoryBruteforce
```

⚠️ **Pro Tip:** Always check for backup extensions like `.bak`, `.old`, and `.~` — developers sometimes rename the file instead of deleting it!
