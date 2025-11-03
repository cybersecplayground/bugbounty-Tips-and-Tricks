# 🔥 What is IDOR?
![What is IDOR](https://github.com/user-attachments/assets/e9e0db2b-4827-4926-a1de-d0fb707a2fe3)

**Insecure Direct Object Reference (IDOR)** occurs when an application uses user-supplied input to access objects directly without proper authorization checks. Attackers can manipulate references (IDs, filenames, tokens) to access other users' data or functionality.

---

## 📌 Definition
An IDOR vulnerability happens when a web application uses user-controlled input (such as an ID, filename, or database key) to directly access internal objects without verifying that the requester is authorized to access that object.

---

## 🎯 Common IDOR Examples

**Simple IDOR**
- Normal: `/api/user/123/profile`  
- Attack: `/api/user/124/profile`

**Parameter-Based IDOR**
- Normal: `/download?file=user123.txt`  
- Attack: `/download?file=admin.txt`

**API Endpoint IDOR**
- Normal: `GET /api/orders/456`  
- Attack: `GET /api/orders/789`

---

## 🛠 Advanced IDOR Techniques

1. **Array-Based IDOR**
```
/api/users/[101,102,103]
/api/users/?ids[]=101&ids[]=102
/api/batch?users=101,102,103
```

2. **HTTP Method Switching**
```
GET /api/admin/users → 403 Forbidden
POST /api/admin/users → 200 OK + Data
```

3. **UUID / Hash Prediction**
```
/documents/550e8400-e29b-41d4-a716-446655440000
```
Try incrementing or predicting other UUIDs (where predictable patterns exist).

4. **HTTP Parameter Pollution**
```
?user_id=123&user_id=124
?account=123&account=124
```

---

## 🔍 Testing Methodology

**Step 1 — Find Object References**
- Look for numeric IDs, UUIDs, usernames in URLs and API responses.  
- Inspect JavaScript files for API calls and client-side patterns.

**Step 2 — Test Authorization**
- Change IDs while authenticated as User A.  
- Attempt access to other users' resources.  
- Test with alternate HTTP methods (GET/POST/PUT/DELETE).

**Step 3 — Escalate Impact**
- Move from read-only access to write/delete actions.  
- Chain with other bugs (SSRF, XSS, logic flaws) to escalate privileges.

---

## ⚡ Pro Tips for Bug Bounty Hunters

**Bypass Common Defenses**
- URL encode values: `%32` for `2`.  
- Try alternate formats: hex, decimal, base64.  
- Test trailing slashes, dot segments, and parameter ordering.

**Automate Discovery**
- Use `ffuf` or custom scripts for mass IDOR testing:
```bash
ffuf -w user_ids.txt -u https://target.com/api/user/FUZZ
```

**What to look for**
- Sequential numeric IDs or predictable patterns.  
- Endpoints returning too much data.  
- Missing authorization tokens or weak session controls.

---

## 🛡 Defense Strategies (For Developers)

- **Indirect References:** Use opaque identifiers that map to internal IDs.  
- **Per-request Authorization:** Always verify permissions for each object access.  
- **Random UUIDs:** Avoid sequential IDs that are easy to predict.  
- **Input Validation:** Sanitize and validate all user input.  
- **Audit Logging:** Log accesses and monitor for abnormal patterns.

---

## 🎯 Real-World Impact
- Access other users' personal data (PII).  
- Retrieve confidential documents.  
- Modify or delete other users' content.  
- Potential privilege escalation to admin access.

---

## 🔔 Follow & Credits
Follow **@cybersecplayground** for more vulnerability deep-dives and bug bounty workflow tips.

**Tags:** `#IDOR #WebSecurity #BugBounty #APISecurity #PenTesting #InfoSec`
