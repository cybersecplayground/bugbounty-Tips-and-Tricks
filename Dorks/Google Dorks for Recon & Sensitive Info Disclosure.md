# 🕵️‍♂️ Google Dorks for Recon & Sensitive Info Disclosure

Quickly discover exposed admin panels, backup files, configuration leaks, and other juicy targets using these crafted Google Dorks 🔥

---

## 🔍 Top Dorks to Try

```
intitle:"index of" inurl:ftp intext:admin
intitle:"index of" "system/config"
intitle:"index of" "admin/config"
"index of" "/config/sql"
intitle:"index of" "api/admin"
intitle:"index of" "tinyfilemanager.php"
intitle:"index of" "test/storage/framework/sessions/"
intitle:"index of" "symfony/config"
intitle:"index of" "graphql/subscription"
intitle:"index of" "/admin/backup"
intitle:"index of" "admin/json"
intitle:"index of" "/admin_backup"
intitle:"index of" "git-jira-log"
intitle:"index of" db.frm
intitle:"index of" "/db_backups/"
intitle:"index of" "common.crt" OR "ca.crt"
intitle:"index of" "global.asa"
intitle:"index of" "proxy.pac" OR "proxy.pac.bak"
intitle:"index of" "MySQL-Router"
intitle:"index of" "owncloud/config/*"
site:*.target.com "@gmail.com"
```

> ⚠️ **Use responsibly.** These dorks may lead to sensitive systems or internal files. Only test on authorized targets!

---

## 💻 Recommended Tools

- [🔗 Google Search](https://www.google.com)
- [🔗 Faisal Ahmed's Dork Index](https://dorks.faisalahmed.me)
- [🔗 BullsEye Google Dork Scanner](https://github.com/BullsEye0/google-dork-scanner)

---

## 🎯 Bonus Tips

- Combine dorks with `site:example.com` for targeted hunting
- Use quotes to refine exact matches
- Chain with tools like [waybackurls](https://github.com/tomnomnom/waybackurls), `gau`, and `hakrawler` for even deeper discovery

---

📢 **Follow [@cybersecplayground](https://t.me/cybersecplayground)** for daily recon dorks, PoCs, CVEs, and red teaming content!

#recon #bugbountytips #googlehacking #osint #bugbounty #cybersecplayground #indexof #admin #securityt
