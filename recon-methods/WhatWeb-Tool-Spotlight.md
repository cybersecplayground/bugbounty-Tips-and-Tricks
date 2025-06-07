# 🔍 Tool Spotlight: WhatWeb – Website Fingerprinting Like a Pro

Want to know what’s running behind a website without touching the source code?  
Meet WhatWeb — your go-to recon tool for fingerprinting technologies used on websites 🔧🌐

## 💡 WhatWeb Features:
- Detects CMS (WordPress, Joomla, etc.)  
- Identifies Server software (Apache, Nginx, IIS)  
- Shows Frameworks, Platforms, and Scripts  
- Plugin-based, supports aggressive & passive modes  
- Supports proxy, cookie injection, custom headers, and verbose debugging  

## 🚀 Basic Usage Examples:

```bash
whatweb target.com
```

### 📚 Multiple URLs Input:
```
whatweb -i live.txt
```
### 🎭 Aggressive Fingerprinting:
```
whatweb -a 3 target.com
```
### 🕵️‍♂️ Proxy Support for Anonymity:
```
whatweb --proxy 127.0.0.1:8080 target.com
```
🔥 Pro Tips for Bug Bounty & Recon:
Combine with waybackurls or gau output

> Use with `-i live.txt` to mass scan for tech stacks

## Grep for admin/login panels:

```
whatweb -i live.txt | grep -i "admin\|login"
```
Perfect for fingerprinting targets before deeper enumeration and exploitation!

🛠 Install:
```
git clone https://github.com/urbanadventurer/WhatWeb  
cd WhatWeb && ruby whatweb.rb --help
```
📢 Follow [@cybersecplayground](https://t.me/cybersecplayground) for more daily recon tools, CVE exploits, and bug bounty tricks!

👍 Like & 🔁 Share to support the channel!
#bugbounty #recon #infosec #whatweb #cybersecurity #tools #cybersecplayground
