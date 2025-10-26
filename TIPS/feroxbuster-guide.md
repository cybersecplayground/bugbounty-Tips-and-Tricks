# 🔥 What is Feroxbuster?
![What is Feroxbuster](https://github.com/user-attachments/assets/469e5bdb-9fa5-41af-9489-24cd9ea15502)


Feroxbuster is a fast, recursive content discovery tool written in Rust. It's designed to brute-force directories and files on web servers, making it essential for bug bounty hunting and penetration testing.

---

## 🚀 Key Features
- **Blazing Fast** - Multi-threaded performance  
- **Recursive Scanning** - Automatically follows discovered directories  
- **Flexible Filtering** - Filter by status codes, word counts, etc.  
- **Multiple Extensions** - Test with various file extensions  
- **Resume Capability** - Pause and resume scans  
- **Auto-Tune** - Adjusts performance based on server response

---

## 🛠️ Basic Usage Examples

**Simple Directory Bruteforce:**
```bash
feroxbuster -u https://target.com -w wordlist.txt
```

**Advanced Scan with Extensions:**
```bash
feroxbuster -u https://target.com -w wordlist.txt -x php,html,js,txt -t 50
```

**Recursive Scan with Filters:**
```bash
feroxbuster -u https://target.com -w wordlist.txt --recursive -n
```

---

## ⚡ Pro Commands

**Aggressive Scan:**
```bash
feroxbuster -u https://target.com -w big_wordlist.txt -t 100 -x php,asp,aspx,jsp -C 404,403 --auto-tune
```

**Scan with Authentication:**
```bash
feroxbuster -u https://target.com -w wordlist.txt -H "Authorization: Bearer token123"
```

**Save Results & Resume:**
```bash
feroxbuster -u https://target.com -w wordlist.txt -o results.json --json
```

---

## 🎯 Why Choose Feroxbuster?
- Faster than most traditional directory busters  
- Smart filtering reduces false positives  
- Easy to use with sensible defaults  
- Continuous development and updates  
- Great for both beginners and pros

---

## 💡 Pro Tips
- **Start Small** - Use common wordlists first (e.g., `/usr/share/wordlists/dirb/common.txt`)  
- **Adjust Threads** - Use `-t` to control concurrent requests  
- **Filter Noise** - Use `-C` to hide common status codes  
- **Use Extensions** - `-x` parameter dramatically increases findings  
- **Monitor Performance** - Watch for server rate limiting

---

## 📚 Installation
```bash
# Kali Linux
sudo apt install feroxbuster

# Using Cargo
cargo install feroxbuster

# GitHub Releases
wget https://github.com/epi052/feroxbuster/releases/latest/download/feroxbuster -O feroxbuster
```

---

🔔 Follow [**@cybersecplayground**](https://t.me/cybersecplayground) for more tool tutorials and hacking techniques!  
Like & Share if you discovered new directories with this! 🚀

#CyberSecurity #PenTesting #BugBounty #WebSecurity #Feroxbuster #Reconnaissance #HackingTools #InfoSec
