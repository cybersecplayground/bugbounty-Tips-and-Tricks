
# 🧩 How to Collect GET-Based Parameters (Like a Pro)

## 🔍 Overview
A solid recon phase is the foundation of every successful bug bounty. Here’s my full methodology to collect GET parameters for deeper vulnerability testing like XSS, SSRF, Open Redirect, and more.

---

## 📌 Step-by-Step Breakdown

### 🔸 1. Subdomain + Endpoint Discovery
First, gather as many live subdomains and endpoints as possible:

```bash
subfinder -d vulnweb.com -all | tee subs.txt
cat subs.txt | httpx -paths /robots.txt,/sitemap.xml -silent -mc 200 | tee live_hosts.txt
```

### 🔸 2. URL Collection
Use multiple tools for maximum coverage:

```bash
cat subs.txt | waybackurls > wayback.txt
cat subs.txt | gau --threads 5 > gau.txt
cat subs.txt | hakrawler > hakrawler.txt
```

🧪 Merge everything:

```bash
cat wayback.txt gau.txt hakrawler.txt | sort -u > all_urls.txt
```

### 🔸 3. Extract GET Parameters
Now filter only the URLs that have query parameters:

```bash
grep -aE "\?.*=" all_urls.txt | grep -aiEv "\.(css|ico|png|jpg|js|json|svg|pdf|xml|webp)" | anew > get_params.txt
```

🔥 You can also clean and fuzz with qsreplace:

```bash
cat get_params.txt | qsreplace "FUZZ" > fuzzable_params.txt
```

### 🔸 4. BONUS: Extract Unique Param Names
For custom wordlists or targeted attacks:

```bash
cat get_params.txt | unfurl keys | sort -u > param_names.txt
```

---

## 🎯 Why This Matters
Finding hidden or unused parameters gives you prime entry points to test for:

- ✅ Reflected & Stored XSS
- ✅ SSRF attacks via internal URL redirects
- ✅ Open Redirects and IDORs

---

## 💻 Want more?
Real-world recon tips and hacking methods shared daily!

📢 **Join us** 👉 [@cybersecplayground](https://t.me/cybersecplayground)

---

### 📌 Tags
#BugBounty #CyberSecurity #InfoSec #GETparameters #XSS #SSRF #OpenRedirect #BugBountyTips #EthicalHacking #Recon #Pentesting #HackingTools #OSINT #HackerLife #CybersecPlayground
