# 🚨 Advanced XSS WAF Bypass in JavaScript Context

**👨‍💻 Discovered by:** [@thelilnix](https://twitter.com/thelilnix)

A clever JavaScript-based XSS payload designed to **bypass WAF filters** that look for standard `alert()` patterns, `<script>` tags, or suspicious keywords.

---

## 💣 Payload
```js
''.replace.call`1${/.../}${alert}`
```
🧠 How It Works
- `Template Literals ( )`: Used to dynamically inject code, which often avoids pattern-based filters.

- `.replace.call` Method Hijacking: This tricks the JS engine to evaluate code via tagged template literals.

- `${/.../}`: Can be any regex or dummy code; included to further obfuscate the logic.

- `${alert}`: Dynamically references the global alert function in modern browsers without needing ().

🧪 Practical Example
Inject into any inline JavaScript context where code execution is allowed:

```
<script>
  let x = ''.replace.call`1${/.*/}${alert}`
</script>
```
✅ Result: Executes alert(1) without using alert(1) directly.

🔍 Why This Bypass Works

🔒 Commonly Blocked by WAFs:
```
<script>alert(1)</script>
```
😈 Rarely Blocked (This Payload):
```
''.replace.call`1${/.*/}${alert}`
```
🔐 Security Impact

**This bypass:**

- Avoids keyword-based detection (e.g., alert(, onerror=, <script>)
- Exploits parsing quirks and JavaScript expression evaluation
- Is valuable in bug bounty, pentesting, and CSP/DOM bypass scenarios

**🔥 Test this in controlled environments like:**

- XSS Hunter
- JSFiddle with CSP disabled
- Burp Collaborator

**📢 Stay Updated**
For more WAF bypasses, real-world CVEs, and bug bounty payloads:
👉 - [@cybersecplayground](https://t.me/cybersecplayground)

➕ (Payload added to [xss Payload list](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/Payloads/XSS_Payload.txt))

🏷 Tags

#XSS #BugBounty #WAFBypass #JavaScript #Cybersecurity #thelilnix #Infosec #Payloads #WebSecurity #CybersecPlayground
