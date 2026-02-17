# 🎓 Part 1/3: Understanding phpinfo() - The Accidental Goldmine 🎓
<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/03f11264-31d4-43d0-b651-be64cd368745" />

## What is phpinfo()?

**phpinfo()** is a built-in PHP function that outputs extensive information about the PHP environment on a server.

Developers commonly create files like `info.php` or `phpinfo.php` during installation, testing, or debugging, and unfortunately, these files often remain on production servers long after they're needed.

---

## ⚠️ The Warning Developers Ignore

The official PHP documentation and security-conscious tutorials always include a warning:

> Delete this file after use because it contains sensitive information that could help attackers compromise your server.

Yet, exposed phpinfo() files remain one of the most common information disclosure vulnerabilities found in the wild.

---

## 🔥 What a phpinfo() Page Reveals

A single phpinfo() page exposes a treasure trove of server information:

- **System Information:** OS, hostname, architecture, kernel version  
- **PHP Version:** Exact version number (critical for identifying known vulnerabilities)  
- **Server Software:** Apache/Nginx version, loaded modules  
- **Document Root:** Absolute path to web root (`/var/www/html`, etc.)  

### Configuration Directives
- `allow_url_fopen` / `allow_url_include` status (RFI potential)  
- `disable_functions` list  
- `display_errors` / `display_startup_errors`  
- `open_basedir` restrictions  

### Additional Exposure
- Loaded Extensions (mysql, curl, gd, etc.)  
- Environment Variables (may contain API keys or credentials)  
- Server API configuration  
- HTTP Headers revealing infrastructure info  

---

## 💡 Why Attackers Love phpinfo()

- Reconnaissance shortcut — hours of fingerprinting reduced to seconds  
- Precise exploit targeting via exact versions  
- Path disclosure for payload placement  
- Security control inventory visibility  
- Session data leaks (e.g., `session.save_path`)  
- Credential exposure via environment variables  

---

## 🛠 Real‑World Impact: Bug Bounty Example

A researcher discovered an exposed phpinfo() page on a NASA VDP target through a guessable endpoint. It revealed:

- Exact PHP version  
- Internal paths  
- Internal IP addresses  
- Loaded modules (`pdo_mysql`, `mongodb`)  
- Empty `disable_functions` directive  
- SSL info listing multiple subdomains  

**Impact:** Attackers could craft targeted exploits and map internal infrastructure.

---

## ⚡ CVE Examples: When phpinfo() Becomes a Vulnerability

### CVE-2023-49282 — Amelia WordPress Plugin
- Bundled Microsoft Graph PHP SDK contained `/tests/GetPhpInfo.php`
- If `/vendor` directory was web-accessible, anyone could access it
- Over **90,000+ installations** affected

### CVE-2025-63738 — Xinhu Rainrock RockOA
- Version **2.7.0** allowed triggering phpinfo() via `a` parameter in `index.php`
- Low‑privileged users could access server configuration
- **CVSS 4.3 (Medium)**

### CVE-2009-2160 — TorrentTrader Classic
- Direct requests to `phpinfo.php` exposed configuration data
- One of many historical cases proving this is a persistent issue

---

## 🔔 Follow @cybersecplayground
For **Part 2: How to Find Exposed phpinfo() Files**

---

✅ **Like & Share** if you've ever found a phpinfo() file in the wild!

---

### #phpinfo #InfoDisclosure #BugBounty #WebSecurity #CyberSecurity #Reconnaissance #PenTesting

---

⚠️ **Pro Tip:** Never delete phpinfo() files during testing—report them.  
But if you create one for your own testing, use an obscure filename and delete it immediately afterward.
