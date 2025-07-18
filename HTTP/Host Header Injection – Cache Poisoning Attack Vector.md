## 📌 Host Header Injection – Cache Poisoning Attack Vector
![Host Header Injection – Cache Poisoning Attack Vector - Cybersecplayground](https://github.com/user-attachments/assets/6d2e596d-240c-4106-95ad-25282db9e96a)

### 💨 Exploit Host Headers for Misconfig, SSRF & Cache Hijacking

Host header injection is a commonly overlooked vulnerability that can lead to severe consequences like cache poisoning, open redirects, email spoofing, and even SSRF.

---

### 💥 Attack Scenario

Most apps reflect or trust the `Host` header without verification. If there's a reverse proxy (CDN, load balancer, etc.), and the app uses the header in logic (like password reset links or cache keys), you can inject malicious behavior.

#### ⚩️ Common Headers to Manipulate:

```
Host: evil.com
X-Forwarded-Host: evil.com
X-Host: evil.com
Forwarded: host=evil.com
```

#### 🧪 Try this in Burp:

```
GET / HTTP/1.1
Host: evil.com
X-Forwarded-Host: evil.com
```

### ✅ If the app:

* Generates password reset links
* Renders absolute URLs in responses
* Performs redirects or caching based on Host

🔪 Then you're in business.

---

### 🔥 Real Exploits:

* **Cache Poisoning**: Poison CDN by caching response under a fake host.
* **SSRF**: In internal services, Host might control routing.
* **Email Poisoning**: Reset links emailed to users can contain attacker’s domain.

---

### 🔍 Detection Tips:

* Check if any headers are reflected in responses.
* Look at password reset emails.
* Test behaviors on CDN-cached pages.
* Combine with `X-Forwarded-Host`, `X-Original-URL`, etc.

---

### 🛡 Mitigation:

* Don’t trust user-controlled Host headers.
* Whitelist acceptable Host values on server-side.
* Avoid using headers in logic or links unless validated.
* Ensure caching layers (e.g. Varnish, Cloudflare) don’t vary on Host.

---

### 🧠 Pro Tip:

If you're getting 403 or weird behavior, try header smuggling techniques or tamper with casing (`HoSt`, `HOST`), spacing, or duplicate headers.

---

📢 Follow 👉 **[@cybersecplayground](https://t.me/cybersecplayground)** for more advanced tips & exploits daily.

💬 Dont forget to give STAR and FOLLOW for more...

---

\#bugbounty #hostheader #cachepoisoning #ssrf #infosec #cybersecplayground #burpsuite #websecurity #exploit
