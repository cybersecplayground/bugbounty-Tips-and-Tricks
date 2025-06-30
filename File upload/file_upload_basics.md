
# 📂 Beginner's Guide (Part 1 of File Upload Week): File Upload Vulnerability

💣 _“It’s just a profile picture… or is it?”_

## 🔍 What is a File Upload Vulnerability?
Some websites let users upload files — like images, documents, or PDFs. But if the website doesn’t check the uploaded file properly, an attacker might upload a dangerous file — like a script — that gets executed on the server!

This can lead to:
- ❗️ Website defacement
- 🐚 Remote Code Execution (RCE)
- 🔓 Server access or full control

## 🧪 Real Example:
A user uploads `cat.jpg`, but the attacker uploads:
- `cat.php.jpg`
- `rce.php`

If the server:
- ✅ Accepts the file
- ✅ Saves it to a public folder
- ✅ Doesn’t validate it properly

Then the attacker can access `http://target.com/uploads/rce.php` and run commands directly on the website!

## ⚠️ Why Does This Happen?
- 🔸 Server trusts the file extension (.jpg, .pdf, etc.)
- 🔸 Server doesn’t check content inside the file
- 🔸 Upload folder has execution permissions

## 🛡 How to Stay Safe (for Developers):
- ✅ Only allow specific file types
- ✅ Rename uploaded files on the server
- ✅ Store them in folders without execution rights
- ✅ Scan uploaded files for malicious content
- ✅ Use proper libraries for file handling

## 🎯 Why Should Bug Hunters Care?
This is a very common issue in older CMS, custom admin panels, and web apps. If you find a file upload function — test it! It might be your way to RCE 😈

📚 Stay sharp. Learn vulnerabilities. Hack smart.  
🔐 Follow **@cybersecplayground** for more beginner-to-advanced security tips!

---

#cybersecurity #bugbounty #fileupload #beginner #infosec #websecurity #webapp #cybersecplayground
