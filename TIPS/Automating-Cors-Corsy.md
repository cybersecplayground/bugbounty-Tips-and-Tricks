# 🔍 Automating CORS Vulnerabilities with Corsy

CORS (Cross-Origin Resource Sharing) misconfigurations can lead to serious security issues such as data leaks, session hijacking, and unauthorized access to sensitive resources. **Corsy** is a lightweight and powerful tool that automates the discovery of such vulnerabilities.

---

## 🛠 Tool: Corsy
**GitHub:** [https://github.com/s0md3v/Corsy](https://github.com/s0md3v/Corsy)

### ⚙️ Features:
- Detects common CORS misconfigurations
- Lightweight and written in Python3
- Supports multithreading, delays, and custom headers
- Outputs results in JSON format

---

## 🧪 Getting Started

### 📦 Installation
```bash
git clone https://github.com/s0md3v/Corsy
cd Corsy
pip3 install -r requirements.txt
```

### 🚀 Usage
Scan a single target:
```bash
python3 corsy.py -u https://example.com
```

Scan multiple targets with threading and custom headers:
```bash
python3 corsy.py -u https://example.com -t 20 --headers "User-Agent: GoogleBot\nCookie: SESSION=Hacked"
```

Scan a list of domains:
```bash
python3 corsy.py -i ./targets.txt
```

---

## 🔎 Recon + Automation Workflow

### 1. Subdomain Enumeration
Use tools like [Amass](https://github.com/owasp-amass) or [Subfinder](https://github.com/projectdiscovery/subfinder):
```bash
amass enum -d target.com -o targets.txt
```

### 2. CORS Scan with Corsy
```bash
python3 corsy.py -i targets.txt
```

### 3. Analyze Results
Look for:
- `Access-Control-Allow-Origin: *`
- `null` origins accepted
- Reflecting malicious origins
- Sensitive endpoints: `/api/user`, `/profile`, etc.

### 4. Craft PoCs
Use Burp or a browser-based attack to demonstrate unauthorized data access.

---

## 💡 Pro Tips
- Check login portals and API subdomains
- CORS misconfig + token-based auth = jackpot
- Use automation during recon sweeps for better efficiency

---

## 🧠 References
- [Corsy GitHub Repository](https://github.com/s0md3v/Corsy)
- [CORS Security Primer - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

---

📡 Stay updated with cutting-edge recon tips, PoCs, and CVEs:
**Telegram:** [@cybersecplayground](https://t.me/cybersecplayground)

---

**Like, Share & Star this repo if it helps!** 🌟

#bugbounty #cors #infosec #automation #cybersecurity #recon #cybersecplayground
