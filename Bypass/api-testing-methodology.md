# 🔥 4-Step API Testing Methodology
![4-Step API Testing Methodology](https://github.com/user-attachments/assets/caabe074-27b4-4e94-8ba1-535cf18f12c7)
**Advanced API Vulnerability Discovery**  
_Use Case: Bug Bounty & API Security Testing_

---

## 1️⃣ Find Sensitive API Endpoints
Target endpoints that commonly leak sensitive data:
- User PII (emails, phone numbers, addresses)
- Financial data (transactions, balances)
- Authentication tokens & session data
- Internal system information
- Admin-level data in user endpoints

**Common sensitive endpoints**
```
/api/v1/users/[ID]
/api/admin/config
/api/internal/metrics
/api/orders/[ID]
/api/transactions
/api/profile/private
```

---

## 2️⃣ Cache Headers Analysis
Check response headers for caching indicators:
- `Cache-Control: public, max-age=3600` ← CACHED
- `CF-Cache-Status: HIT` ← Cloudflare cached
- `X-Cache: HIT` ← Generic cache hit
- `Age: 300` ← 5 minutes in cache
- `ETag: "abc123"` ← Entity tag for cache validation
- `Via: 1.1 varnish` ← Proxy caching

If cached → try Web Cache Deception:
```
Legitimate: /api/users/me/profile
Deception:  /api/users/me/profile.css
Deception:  /api/users/me/profile/
```

---

## 3️⃣ HTTP Method Changing
Bypass auth/validation with method switching. Examples:
```
GET /api/admin/users → 403 Forbidden
POST /api/admin/users → 200 OK + user list

GET /api/config → 404 Not Found
HEAD /api/config → 200 OK

POST /api/search → 403 Forbidden
PUT /api/search → 200 OK + results
```

---

## 4️⃣ Array-Based IDOR Testing
When you find `/api/users/123` test these array/IDOR patterns:
```
/api/users/[123,124]
/api/users/123,124
/api/users/123&124
/api/users/?id[]=123&id[]=124
/api/users/?ids=123,124
/api/users/?user_ids=123,124
/api/batch/users?ids=123,124
```

---

## 🎯 Real-World Attack Chain (Example)
1. Discover endpoint `/api/v1/users/456`  
2. Check headers → `X-Cache: HIT`, `max-age=300`  
3. Change `GET` to `POST` → bypass rate limiting  
4. Test array IDOR → `/api/v1/users/[456,457,458]`  
**Result:** Mass user data leakage + cached responses

---

## 🛡 Defense Recommendations
- **Consistent Authorization** — Apply same checks across all HTTP methods  
- **Input Validation** — Reject array parameters unless explicitly allowed  
- **Cache Control** — Use `Cache-Control: private` for sensitive data  
- **API Schema Enforcement** — Validate against OpenAPI specification  
- **Audit Logging** — Monitor for unusual parameter patterns

---

## 💡 Pro Testing Tips
- Use Burp's "Change Request Method" extension  
- Automate with tools like `katana` or `ffuf` for endpoint discovery  
- Always test both authenticated and unauthenticated contexts  
- Combine techniques (cache analysis + method change + IDOR) for maximum impact

---

🔔 Follow **@cybersecplayground** for advanced API hacking techniques!  
Like & Share if you found your first IDOR with this! 💰

#APISecurity #BugBounty #IDOR #WebCacheDeception #CyberSecurity #APITesting #Hacking #SecurityResearch
