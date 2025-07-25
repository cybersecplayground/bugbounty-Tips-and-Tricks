## 🔥 **Bug Bounty Tip – HTTP Parameter Pollution (HPP)**
![HTTP Parameter Pollution (HPP) - cybersecplayground](https://github.com/user-attachments/assets/fe88b78d-7d7f-48b7-92ad-96125f1854aa)

🧠 **Bypass logic, elevate privileges, or even trigger hidden features with duplicate parameters!**

---

### 🚣 What is HPP?

HTTP Parameter Pollution occurs when an application fails to properly handle **duplicate parameters** in a URL or request body.

This can lead to:

* ✅ Logic bypass
* ⚠️ Privilege escalation
* 🔓 Access control flaws
* 💳 Financial manipulation

---

### 💥 Real-World Example:

```
GET /transfer?amount=100&admin=true&amount=1
```

* Server might use the **first `amount=100`** for logging
* But the **second `amount=1`** for actual transfer
* Result: Trick the system to log 100 but only transfer 1

---

### 🌟 Always Try These Patterns:

1. **Duplicate parameter:**

```
param=value1&param=value2
```

2. **Encoded version:**

```
param=value1%26param=value2
```

3. **Injected into body (POST):**

```
username=admin&role=user&role=admin
```

---

### 🛠 Useful Targets:

* Payment systems (`amount`, `price`)
* Role/privilege fields (`admin`, `is_admin`)
* API calls with query params
* Legacy PHP or Java apps (common in multi-param mishandling)

---

### 🛠 Tools to Use:

* **Burp Suite Intruder** → brute and fuzz parameter combos
* **Param Miner (Burp Extension)** → automatic HPP discovery
* **Custom Python Scripts** → for manual testing with `requests`

---

📢 **Follow [@cybersecplayground](https://t.me/cybersecplayground)** for more daily bounty tips, bypass payloads, and real-world examples!

\#bugbounty #HPP #websecurity #bypasstips #infosec #cybersecurity #cybersecplayground
