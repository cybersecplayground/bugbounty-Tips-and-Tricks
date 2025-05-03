# 🔍 Advanced Bug Bounty Recon Playbook (2025)

Welcome to the **Ultimate Recon Pipeline** for serious bug bounty hunters. This playbook is designed for those who want to go beyond the basics and uncover vulnerabilities others miss.

> 💡 *"Deep recon isn't optional—it's essential."*

---

## 📌 Table of Contents
1. [Scope Review](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
2. [Subdomain Enumeration](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
3. [Alive Host Detection](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
4. [Crawling Endpoints](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
5. [Visual Recon (Screenshots)]](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
6. [Automated Vulnerability Scanning](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
7. [Tech Stack Fingerprinting](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
8. [Finding Low-Hanging Fruits](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
9. [URL & Parameter Discovery](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
10. [Google Dorking](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
11. [GitHub Recon](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)
12. [Bonus: Mass Param Testing](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/TIPS/Advanced-Bug-Bounty-Recon%20-Playbook.md#1-scope-review-)

---

## 1. Scope Review 🌍
Understand the rules before hacking.

```txt
Scope: *.target.com
```

Ensure your targets are in-scope to stay compliant and avoid legal trouble.

---

## 2. Subdomain Enumeration 🧹
Tools: `bbot`, `subfinder`, `amass`

```bash
bbot -d target.com
subfinder -d target.com -o subfinder.txt
amass enum -d target.com -o amass.txt
cat *.txt | sort -u > subdomains.txt
```

🔄 Combine passive and active techniques for maximum subdomain coverage.

---

## 3. Alive Host Detection ⚡
Tool: `httpx`

```bash
cat subdomains.txt | httpx -silent -o alive.txt
```

Focus your testing only on reachable domains.

---

## 4. Crawling Endpoints 🕷️
Tool: `katana`

```bash
katana -list alive.txt -o endpoints.txt
```

Reveal hidden endpoints and sensitive paths.

---

## 5. Visual Recon (Screenshots) 📸
Tool: `eyewitness`

```bash
eyewitness --web -f alive.txt --threads 10 -d screenshots
```

Quickly identify admin panels, login forms, and juicy interfaces.

---

## 6. Automated Vulnerability Scanning 🚨
Tools: `nuclei`, `nmap`, `nikto`

```bash
cat alive.txt | nuclei -t templates/ -o nuclei.txt
nmap -sVC -T4 -iL alive.txt -oN nmap.txt
nikto -h alive.txt -output nikto.txt
```

Early detection of common vulnerabilities and misconfigurations.

---

## 7. Tech Stack Fingerprinting 🔬
Tools: `wappalyzer`, `builtwith`, `whatruns`

Understanding the tech stack helps tailor your attacks with precision.

---

## 8. Finding Low-Hanging Fruits 🍯
Tools: `subzy`, `socialhunter`

```bash
subzy run --targets alive.txt
socialhunter -f alive.txt
```

Look for subdomain takeovers and broken link hijacking opportunities.

---

## 9. URL & Parameter Discovery 🌐
Tools: `waybackurls`, `gau`, `paramspider`

```bash
cat alive.txt | waybackurls >> urls.txt
cat alive.txt | gau >> urls.txt
paramspider -d target.com -o params.txt
```

Dig into archived paths and legacy endpoints.

---

## 10. Google Dorking 🧙
```txt
site:target.com ext:sql
site:target.com ext:bak
site:target.com inurl:admin
```

Find exposed files, backup archives, and sensitive interfaces via search engines.

---

## 11. GitHub Recon 🗂️
Search for secrets in public code:

```txt
"target.com" in:code
```

Discover accidentally committed API keys, credentials, and configurations.

---

## Bonus: Mass Param Testing 🎯
Tools: `gf`, `qsreplace`, `httpx`

```bash
gf xss urls.txt | qsreplace '"/><script>alert(1)</script>' | httpx -silent
```

Blast through URL parameters to detect reflected XSS and other injection points.

---

## 🚀 Final Notes
This recon workflow puts you ahead of 90% of hunters.
- ✅ Combine automation with manual review
- ✅ Prioritize exposed and archived data
- ✅ Leverage public intelligence for private targets

---

📌 **Follow [@cybersecplayground](https://t.me/cybersecplayground)** on Telegram for:
- Daily hacking tutorials
- Real-world CVEs & POCs
- Advanced bug bounty tips

💬 Questions, tools, or requests? Open an issue or join the community.

---

> 📁 Clone this repo, tweak it, and stay dangerous.

---

**License:** MIT
