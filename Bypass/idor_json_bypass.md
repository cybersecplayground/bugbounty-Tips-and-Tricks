# 🔓 IDOR in Disguise – Bypass with .json Suffix
## How a 403 turned into a 200 OK with a single trick

### 📍 Vulnerability: Insecure Direct Object Reference (IDOR)
You’re blocked by a 403? Try appending `.json` or `.xml` — and boom 💥

### 🧪 Discovery
While testing an endpoint:

```
PUT /my_day/jobs/4 HTTP/2 → ❌ 403 Forbidden
```

But then, using this slight variation:

```
PUT /my_day/jobs/4.json HTTP/2 → ✅ 200 OK
```

🔐 Authorization checks were bypassed.

### 💡 Why this works:
Many frameworks (Rails, Django, older Node APIs):

- Treat `/resource.json` as a different route
- Apply different middlewares or access checks
- Sometimes, JSON API routes are under-tested or forgotten

### 🚨 Impact:
✅ Edit or delete other users' jobs/tasks  
✅ Privilege escalation  
✅ Potential full account takeover if used on critical endpoints

### 🛠 Tips for Hunters:
Try `.json`, `.xml`, `.html`, `.txt`, `.pdf`, etc.

Fuzz URL paths with suffixes using:

```
ffuf -u https://target.com/jobs/4FUZZ -w extensions.txt
```

Always compare HTTP status codes & response body  
Use Burp Repeater to replay both versions

### 🧠 IDORs are everywhere — especially in:

- To-do apps
- Calendars
- Project management tools
- RESTful APIs

---

📣 Keep Testing. Keep Winning.  

🔗 Follow us for more: [@cybersecplayground](https://t.me/cybersecplayground)  
❤️ Like | 🔁 Share | 🧠 Learn daily!

#IDOR #BugBounty #CyberSecurity #InfoSec #HackingTips #AuthorizationBypass #WebSecurity #Recon #CTF #cybersecplayground
