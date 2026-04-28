# 🎓 COMMON HTTP ERROR CODES & Bypass Techniques 🎓
<img width="1400" height="600" alt="COMMON HTTP ERROR CODES   Bypass Techniques" src="https://github.com/user-attachments/assets/158f2846-1186-4a3d-8143-d3332c26fe67" />

HTTP error codes are not just roadblocks—they're clues. Understanding what each code means and how to bypass them is essential for web penetration testing and bug bounty hunting. This guide covers the most common error codes and practical bypass techniques.

---

## 🔥 1xx: Informational Responses (Rarely Seen in Testing)

| Code | Name | What It Means |
|------|------|--------------|
| 100 | Continue | Server received headers, client should send body |
| 101 | Switching Protocols | Server agrees to upgrade protocol (WebSocket, etc.) |
| 102 | Processing | Server is processing request (WebDAV) |

**Bypass Value:** Minimal—these are transitional responses.

---

## 🔥 2xx: Success Codes (What We Want to See)

| Code | Name | What It Means |
|------|------|--------------|
| 200 | OK | Request succeeded |
| 201 | Created | Resource successfully created |
| 204 | No Content | Success but no response body |
| 206 | Partial Content | Range request successful |

**Bypass Value:** These are your targets—finding 200s where you should get 403s is a win.

---

## 🔥 3xx: Redirection Codes (Follow the Trail)

| Code | Name | What It Means | Bypass Technique |
|------|------|--------------|------------------|
| 301 | Moved Permanently | Resource moved permanently | Follow Location header |
| 302 | Found | Temporary redirect | Follow Location header |
| 307 | Temporary Redirect | Preserve HTTP method | Follow with same method |
| 308 | Permanent Redirect | Preserve HTTP method | Follow with same method |

### Bypass Techniques:
```bash
# Follow redirects automatically
curl -L https://target.com/old-path

# Check if redirects bypass access controls
# Sometimes /admin redirects to /login, but /admin/ (with trailing slash) might not
```

---

## 🔥 4xx: Client Errors (The Most Common Roadblocks)

| Code | Name | What It Means | Bypass Techniques |
|------|------|--------------|------------------|
| 400 | Bad Request | Malformed syntax | Fix request formatting, check encoding |
| 401 | Unauthorized | Authentication required | Add/modify Authorization header, try default creds |
| 403 | Forbidden | No permission | See detailed bypass section below |
| 404 | Not Found | Resource missing | Fuzz for hidden paths, check case sensitivity |
| 405 | Method Not Allowed | Method blocked | Try switching methods (GET→POST→PUT→PATCH→DELETE) |
| 429 | Too Many Requests | Rate limited | Add delays, rotate IPs/user-agents |
| 431 | Header Too Large | Too big headers | Reduce header size, split requests |

---
## 🔥 403 Forbidden - The Most Important Bypass Section


### Technique 1: HTTP Method Switching

```http
GET /admin → 403 Forbidden
POST /admin → 200 OK (data exposed)
PUT /admin → 200 OK
```

### Technique 2: Path Traversal with Encoding

```http
GET /admin → 403
GET //admin → 200
GET /admin/ → 200
GET /./admin → 200
GET /anything/../admin → 200
GET /%2e/admin → 200 (%2e = .)
GET /admin%2f → 200 (trailing slash encoded)
```
### Technique 3: Header-Based Bypasses

```http
# Add these headers to bypass IP-based restrictions
X-Forwarded-For: 127.0.0.1
X-Original-URL: /admin
X-Rewrite-URL: /admin
X-Real-IP: 127.0.0.1
X-Client-IP: 127.0.0.1
```

---

### Technique 4: Case Manipulation

```http
GET /Admin → 200 (if case-insensitive routing but WAF case-sensitive)
GET /ADMIN → 200
GET /aDmIn → 200
```  

---

### Technique 5: URL Encoding Variations


```http
GET /%61dmin → 200 (hex encoding)
GET /%2561dmin → 200 (double encoding)
GET /%41dmin → 200 (uppercase hex)
```

---

### Technique 6: Parameter Pollution

```http
GET /admin?admin=true → 200
GET /admin?debug=1 → 200
GET /admin?bypass=1 → 200
```
### 🔥 404 Not Found Bypasses

- Try different file extensions: `admin.php` , `admin.asp` , `admin.jsp`
- Check backup files: `admin.php.bak` , `admin.php~` , `admin.old`
- Test with trailing slashes: `/api/users/` → `/api/users`
- Remove path segments: `/api/v1/users` → `/api/users`


### 🔥 401 Unauthorized Bypasses

```bash
# Try default credentials
admin:admin, admin:password, root:root

# Add Authorization headers
Authorization: Basic YWRtaW46YWRtaW4= (base64 admin:admin)
Authorization: Bearer [known-valid-token]

# Check for OAuth misconfigurations
```


---

## 🔥 5xx Errors

| Code | Name | What It Means | Exploitation Potential |
|------|--------|-------------|--------------------| 
| 500 | Internal Server Error | Generic server error | HIGH - Indicates unexpected input |
| 501 | BNot Implemented | Server lacks functionality | Check for version-specific CVEs |
| 502 | Bad Gateway | Upstream server error | Potential SSRF or misrouting |
| 503 | Service Unavailable | Server overload/maintenance | HIGH - May indicate security controls crashing |
| 504 | Gateway Timeout | Upstream timeout | Check for SSRF or DoS  |

---

## 💡 500 Errors = Goldmine
### A 500 error often means the server's security controls crashed while trying to process your request. This can reveal:

- SQL injection points  
- Command injection vulnerabilities  
- Path traversal opportunities  
- Deserialization issues  

Testing Approach:

```bash
# Start with basic payloads
GET /api/user?id=' → 500 (SQL injection potential)
GET /api/user?id=../../ → 500 (path traversal potential)
GET /api/user?id=;ls → 500 (command injection potential)

# Fuzz parameters that trigger 500s
ffuf -w payloads.txt -u https://target.com/api/endpoint?param=FUZZ -mc 500

```

---

## 💡 💡 Pro Testing Methodology

- Map the Error Landscape: Document which endpoints return which error codes  
- Test Each Bypass Technique: Systematically apply the bypasses above  
- Chain Findings: A 401 + 403 bypass might lead to admin access  
- Monitor 500s Closely: They often point to the most severe vulnerabilities  
- Automate with FFUF: Use status code filtering to find bypasses  

```bash
# Example: Find endpoints that respond differently to method switching
ffuf -u https://target.com/FUZZ -w common_paths.txt -X POST -mc 200 -ac
```

---

🔔 🔔 Follow @cybersecplayground for more web security techniques!

✅ Like & Share if you've bypassed a 403 with these tricks! 🚀

#HTTP #WebSecurity #BugBounty #403Bypass #PenTesting #CyberSecurity #InfoSec #Hacking

⚠️ Pro Tip: When you see a 500 error, don't ignore it—fuzz that parameter aggressively. Many critical vulnerabilities are hiding behind server errors!

