## 🚨 XSS to Account Takeover via Cookie Theft 🍪

Simple WAF bypass trick = full account pwn 🔥

---

### 🧪 Scenario

You're testing for XSS. Payload like `alert(1)` returns **403 Forbidden** — classic WAF behavior.

But with a little evasion:

```js
frames ; // ✅ Bypasses the WAF
```

Now, let’s go beyond PoC and grab the cookie:

```js
frames['alert'](document["cookie"]); // ✅
```

---

### 🔐 Result

Steal the cookie → Use it for session hijack → **Full account takeover!**

---

### 💡 Pro Tips

* Always try JS property access patterns like `obj['prop']` to dodge WAF rules
* Replace `document.cookie` with `document["cookie"]`
* Wrap alert in `frames['alert']()` or even iframe-based tricks for obfuscation

---

### 👀 Why It Matters

XSS is still **highly underestimated** — especially when:

* Leading to **session hijacking**
* Combined with **CSRF** or chained with **privilege escalation**

---

### 🧠 Key Lesson

Don’t stop at `alert(1)`.
**Think like a bypasser**.
One bracket, one quote, one nested context — and you’ve bypassed a firewall into a working exploit. 💥

---

### 📢 Stay Sharp

Join [@cybersecplayground](https://t.me/cybersecplayground) for:

* Real-world exploitation tips
* Bypass payloads
* Elite recon workflows

---

\#XSS #BugBountyTips #CookieTheft #WebSecurity #Pentesting #Infosec #Cybersec #cybersecplayground
