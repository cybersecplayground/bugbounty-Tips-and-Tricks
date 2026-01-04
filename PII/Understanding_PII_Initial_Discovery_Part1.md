# 🎓 Understanding PII and Initial Discovery Techniques (Part 1/3) 
<img width="1400" height="600" alt="image" src="https://github.com/user-attachments/assets/51ddfb54-5e98-43ca-84ce-6d9d9b8a2ae4" />

Personally Identifiable Information (PII) is any data that can identify an individual. In security testing and bug bounty hunting, finding exposed PII is a critical high-impact discovery. This series will cover discovery, validation, and reporting across three parts.

PII is categorized by how directly it identifies a person and its sensitivity. Core categories include direct identifiers like SSN or passport numbers, and indirect identifiers that identify a person when combined with other data.

PII is also classified as sensitive or non-sensitive based on the potential harm caused by a leak. Sensitive PII, such as financial or medical records, requires strong protection. Non-sensitive PII, like public phone numbers or email addresses, typically poses a lower risk.

---

## 🔥 What Actually Qualifies as PII?

### 🔸 Direct Identifiers (Highest Risk)
- National ID (SSN)  
- Passport Number  
- Full Name + Date of Birth  
- Driver's License Number  

### 🔸 Digital Identifiers
- Email Address  
- IP Address  
- Account Username  
- Device ID  
- Social Media Profile with identifying details  

### 🔸 Financial Identifiers
- Full Credit/Debit Card Number (PAN)  
- Bank Account Number  

### 🔸 Contextual Identifiers
- Information that, when combined (e.g., Job Title + Company + City), can identify a person.

---

## 💡 Why PII Hunting is Critical for Security & Bounty

- **Legal & Compliance:** Exposing PII violates major regulations like GDPR, CCPA, and HIPAA, leading to massive fines.  
- **High-Impact Findings:** A single leak can affect thousands of users, making it a high-severity bug bounty issue.  
- **Real-World Harm:** Exposed data fuels identity theft, financial fraud, and phishing attacks.

---

## 🛠 Part 1: The Reconnaissance & Initial Discovery Phase

**Goal:** Identify data entry points and potential leak sources.

### 1️⃣ Target Surface Mapping
- Map all subdomains: `assetfinder`, `subfinder`, `amass`  
- Identify technologies: `wappalyzer`, `builtwith`  
- Find parameters: `arjun`, `paramspider`  

### 2️⃣ Google Dorking for Obvious Leaks
```text
site:example.com filetype:csv | filetype:xlsx | filetype:pdf
site:example.com "confidential" | "internal" | "employee list"
intitle:"index of" "backup" site:example.com
```

### 3️⃣ Basic Fuzzing for Common Files
Look for common backup or configuration files that may contain sensitive data:

```bash
ffuf -w ~/SecLists/Discovery/Web-Content/common.txt -u https://target.com/FUZZ -e .bak,.old,.txt,.sql,.tar.gz
```

**Other important tools:**  
`subfinder`, `amass`, `httpx`, `gobuster`

---

## 🔔 What’s Next?
Follow **@cybersecplayground** for **Part 2: Deep-Dive PII Hunting Techniques**.

✅ Like & Share if you're ready to hunt for data leaks! 🔍

⚠️ **Pro Tip:** Always check `/robots.txt` and `/.git/` for clues about hidden directories containing data!

---

### 🏷 Hashtags
#PII #Reconnaissance #BugBounty #OSINT #CyberSecurity #DataLeak #InfoSec
