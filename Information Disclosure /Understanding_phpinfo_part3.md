# 🎓 Part 3/3: Exploiting phpinfo() - Turning Information into Compromise 🎓
<img width="1200" height="400" alt="Part 3 3 - Exploiting phpinfo" src="https://github.com/user-attachments/assets/6aed30e5-39b3-4051-a30b-c8266b69dc7b" />

 
Finding a phpinfo() file is just the beginning. The real value comes from analyzing its contents and using that data to advance your attack. This final part covers post-exploitation analysis and real-world attack chains.

---
## 🔥 What to Look For: The phpinfo() Checklist

### When you access a phpinfo() page, systematically extract these high-value items :

## 1. Version Information

- PHP version (e.g., 8.2.12) → Check for known CVEs 
- Server software version (Apache/Nginx/IIS) 
- OS version and architecture 

## 2. Path Disclosures (Critical for File Upload/Inclusion)

- `DOCUMENT_ROOT` → Web root path (e.g., /var/www/html) 
- `SCRIPT_FILENAME` → Current file path 
- `SESSION_SAVE_PATH` → Where session files are stored 
- `OPEN_BASEDIR` → Restrictions on file access 
- `INCLUDE_PATH` → Where PHP looks for includes 

## 3. Security Configuration

- `disable_functions` → What's blocked (empty means dangerous!) 
- `allow_url_fopen` → If On, potential for RFI 
- `allow_url_include` → If On, remote file inclusion possible 
- `display_errors` → If On, verbose errors help debugging 
- `safe_mode` → Old but sometimes still enabled 

## 4. Loaded Extensions

- mysql, mysqli, pdo_mysql → Database access 
- curl → SSRF potential 
- gd, imagick → Image processing vulnerabilities 
- session → Session handling 
- soap, xmlrpc → API endpoints 

## 5. Environment Variables 

- $_ENV and $_SERVER arrays 
- Database credentials (DB_PASSWORD, MYSQL_PASSWORD) 
- API keys (AWS_ACCESS_KEY_ID, STRIPE_SECRET_KEY) 
- Application secrets 
- Internal IP addresses 

## ⚡️ Advanced Exploitation Chains

### Scenario 1: Path Disclosure + File Upload

1. phpinfo() reveals DOCUMENT_ROOT = /var/www/html
2. Find a file upload feature
3. Upload a PHP webshell
4. Access at /var/www/html/uploads/shell.php
5. Execute system commands

## Scenario 2: Session File Inclusion 

1. phpinfo() shows session.save_path = /var/lib/php/sessions
2. SESSION_USE_TRANS_SID might be enabled
3. Find a Local File Inclusion (LFI) vulnerability
4. Include /var/lib/php/sessions/sess_[valid_session_id]
5. Session hijacking or RCE via session file injection

## Scenario 3: Environment Variable Secrets

1. phpinfo() displays $_ENV with DB_PASSWORD = SuperSecret123
2. Database accessible externally or via SSRF
3. Connect and extract sensitive data
4. Lateral movement using stolen credentials

## Scenario 4: RFI via allow_url_include 

1. phpinfo() shows allow_url_include = On
2. Find any include() or require() with user input
3. Include remote PHP file with malicious code
4. Direct RCE achieved

## Scenario 5: Version-Specific Exploits

1. phpinfo() shows PHP 5.6.40 (end-of-life)
2. Check for known vulnerabilities (CVE-2019-11043, etc.)
3. Target with matching exploit
4. Gain shell access

# 🛠 Real-World Attack Chain: WordPress Plugin Exposure 

> Using CVE-2023-49282 as a template:


### Step 1: Discover vulnerable path
```
GET /wp-content/plugins/ameliabooking/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php
```

### Step 2: Extract from phpinfo():
```
- PHP version: 7.4.33 (known vulnerabilities)
- Document root: /var/www/html
- Environment variables: Contains AWS_ACCESS_KEY_ID
- disable_functions: empty (system() available)
```

### Step 3: Leverage findings
```
- Use stolen AWS keys to access cloud resources
- Upload webshell to /var/www/html/wp-content/uploads/
- Execute system commands via vulnerable plugin
```

### Step 4: Full compromise
```
- Reverse shell back to attacker
- Pivot to internal network
- Data exfiltration
```

# 📊 CVSS Impact Assessment

Exposed phpinfo() typically rates as :


| Metric | CVSS v3 Value |
|----------|---------|
| Attack Vector	| Network |
| Attack Complexity | Low |
| Privileges Required | None |
| User Interaction | None |
| Scope | Unchanged |
| Confidentiality | Low |
| Integrity | None |
| Availability | None |
| Base Score | 5.3 (Medium) |

While the direct impact is information disclosure only, the practical impact can be much higher when chained with other vulnerabilities .

# 🛡️ Defense & Remediation

### If you're a defender, here's how to eliminate phpinfo() exposure :

- Delete all phpinfo() files from production servers 
- Block access to /vendor/, /tests/, /examples/ directories via .htaccess or web server config 
- Disable phpinfo() function in php.ini if not needed:
``` disable_functions = phpinfo ``` 
- Scan dependencies for test files before deployment
- Use Composer with --no-dev in production to exclude development dependencies
- Regular security audits with tools like Nessus that detect these files 

🔔 Follow @[cybersecplayground](https://t.me/cybersecplayground) for more advanced exploitation techniques!

✅ Like & Share if you've ever chained phpinfo() into a critical finding! 🔥

#phpinfo #Exploitation #BugBounty #RCE #WebSecurity #PenTesting #InfoDisclosure #RedTeam

#### ⚠️ Final Pro Tip: When you find a phpinfo() page, take screenshots of everything before it gets patched. The information can be used for months afterward to identify vulnerable components!
