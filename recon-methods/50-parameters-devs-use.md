# 50+ Parameters Devs Actually Use (and Hunters Forget)
![50+ Parameters Devs Actually Use (and Hunters Forget)](https://github.com/user-attachments/assets/7db137fe-f485-4a9f-99ef-2b4f9aea40da)

A curated list of real-world parameters that can be abused for privilege escalation, SSRF, information disclosure, and other vulnerabilities. Move beyond basic `id` fuzzing.

![Bug Bounty](https://img.shields.io/badge/Bug-Bounty-red) ![Pentest](https://img.shields.io/badge/Penetration-Testing-blue) ![Parameters](https://img.shields.io/badge/Web-Parameters-green)

### Why?
*   Real applications hide sensitive functionality behind parameters that are often missed by automated scanners.
*   Flipping a single boolean or changing an environment can unlock admin panels or debug modes.
*   To provide a concrete list of parameters actually used in development for manual testers and hunters.

---

### The List
Try flipping, appending, or injecting payloads into these common parameters.

#### 🔐 Authentication & Roles
```
debug=true
test=1
admin=1
isAdmin=true
isPremium=true
superuser=1
role=user
roleId=1
uid=42
userid=42
account=42
profile=42
type=user
level=1
rank=1
flag=0
```

#### 🔗 Redirects & SSRF
```
redirect=/dashboard
redir=/home
url=http://evil.com
next=/secret
returnUrl=http://evil.com
callback=https://attacker.com
continue=/admin
dest=http://evil.com
path=/images/1.png
```

#### 📁 File & Resource Manipulation
```
file=report.pdf
doc=123
documentId=999
reportId=999
page=1
view=profile
```

#### ⚙️ Application Config & Mode
```
config=prod
settings=default
mode=live
env=production
stage=dev
preview=true
draft=1
beta=1
source=external
origin=trusted
cache=0
nocache=1
```

#### 📤 Output & Format
```
format=json
output=pdf
```

#### ⚡ Miscellaneous Actions
```
module=payments
tab=users
section=dashboard
action=edit
method=get
operation=read
step=1
feature=off
theme=dark
style=default
ref=partner
partnerId=1
affiliate=evil
```

---

### How to Use
1.  Intercept a request with **Burp Suite** or **ZAP**.
2.  Use the **"Send to Intruder"** function.
3.  For each parameter in the list, try these primary payloads:

**Payloads to Test:**
```bash
# Boolean Flip
true, false, 1, 0, on, off, yes, no

# Role Escalation
admin, superuser, superadmin, administrator

# Environment
dev, development, test, testing, stage, staging, prod, production

# Format
json, xml, yaml, php, html

# Path Traversal
../../../../etc/passwd

# SSRF
http://169.254.169.254/
http://burpcollaborator.net
```

**Example Intruder Setup:**
*   **Attack type:** Sniper
*   **Parameter:** `admin`
*   **Payloads:** `[0, 1, true, false, yes, no, admin]`

---

### 🛡️ Defensive Note
*   **Parameter allowlisting is crucial.** Sanitize and validate all input, including query and body parameters, not just those you explicitly use.
*   Unused parameters can be a silent path to privilege escalation. Audit them regularly.

🔗 Wordlist : [LINK](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/wordlist/bugbounty_params_wordlist.txt)

📢 Follow @CyberSecPlayground on Telegram for more daily Linux hacking lessons, red team tips, and pentesting tricks!

