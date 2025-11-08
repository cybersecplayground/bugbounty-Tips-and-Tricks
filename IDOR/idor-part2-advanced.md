# IDOR Part 2 — Advanced Bypass Techniques 🎓
![IDOR Part 2 - Advanced Bypass Techniques](https://github.com/user-attachments/assets/a9c2f8cf-4193-4406-a534-4a2a200aeb0e)

This guide covers advanced techniques for discovering and exploiting Insecure Direct Object Reference (IDOR) issues, with a focus on UUID-based tricks, encoding variations, batch testing, and bypassing common protections.

---

## 🔐 UUID-Based IDOR Tricks

**Null / Special UUIDs**
Try these special UUID values — they sometimes map to default/test objects or admin accounts:
- `00000000-0000-0000-0000-000000000000`  
- `11111111-1111-1111-1111-111111111111`  
- `ffffffff-ffff-ffff-ffff-ffffffffffff`

**UUID Pattern Prediction**
If you see a UUID like `550e8400-e29b-41d4-a716-446655440000`, try incrementing/decrementing segments:
- `550e8400-e29b-41d4-a716-446655440001`  
- `550e8400-e29b-41d4-a716-446655440002`  
- `550e8400-e29b-41d4-a716-446655439999`

---

## 🎯 Advanced Bypass Methods

### 1. Case Manipulation
Some systems treat identifiers case-sensitively or inconsistently:
- `/user/ABC123` → `/user/abc123`  
- `/user/AbC123` → `/user/aBc123`

### 2. Encoding Variations
**URL Encoding**
- `user%32` → `user2`  
- `%31%32%33` → `123`

**Unicode / Normalization**
- Encoded dot/traversal: `%C0%AE%2E` → `..` (useful in weird parsers)

### 3. Parameter Shifting
Modify adjacent parameters to influence access logic:
- `/api/user?id=123&type=profile`  
- Try `/api/user?id=123&type=admin` or `/api/user?id=124&type=admin`

---

## 💡 Creative IDOR Discovery

### 1. Batch Request IDOR
Batch endpoints can leak multiple objects at once:
```http
POST /api/batch
[
  {"method": "GET", "path": "/users/101"},
  {"method": "GET", "path": "/users/102"},
  {"method": "GET", "path": "/users/103"}
]
```

### 2. GraphQL IDOR
Look for `id` or similar arguments:
```graphql
query {
  user(id: "101") { email }
  user(id: "102") { email }
}
```

### 3. WebSocket IDOR
Inspect WS messages for object references:
```js
ws.send('{"action":"getUser","id":"101"}')
ws.send('{"action":"getUser","id":"102"}')
```

---

## ⚡️ Pro-Level Testing Strategies

### 1. Timing-Based Detection
Compare response times:
- Faster responses often indicate cached/valid objects  
- Slower responses may indicate DB lookups for non-existent items

### 2. Error Message Analysis
Different responses can reveal object state:
- `200 OK` → object accessible (your data)  
- `403 Forbidden` → object exists, no access  
- `404 Not Found` → object doesn't exist  
- `500 Error` → unexpected input / possible parsing bug

### 3. Mass IDOR Testing with FFUF
**Numeric ranges**
```bash
ffuf -w ranges.txt -u https://target.com/api/user/FUZZ
```
**UUID lists**
```bash
ffuf -w uuids.txt -u https://target.com/docs/FUZZ
```
**Method variations**
```bash
ffuf -X POST -w ids.txt -u https://target.com/api/delete/FUZZ
```

---

## 🛡 Bypassing Common Protections

**Against Rate Limiting**
- Rotate IPs or user agents  
- Use small delays between requests  
- Abuse batch endpoints to check multiple IDs in one request

**Against Token Validation**
- Try removing tokens or using other users' tokens  
- Manipulate token expiry or token fields if predictable

**Against Referer / Origin Checks**
- Spoof Referer headers  
- Use `null` referer or chain with XSS to bypass

---

## 🔗 Real-World Impact Scenarios

**Horizontal → Vertical Escalation**
- User A accesses User B's data (horizontal)  
- Discover admin UUID → access admin features (vertical)

**Data Correlation Attacks**
- Correlate IDs across endpoints and API versions  
- Chain with info leaks (error messages, metadata) to map object graphs

**Pro Tip:** Always test the NULL UUID `00000000-0000-0000-0000-000000000000` — default objects are surprisingly common!

---

## ⚠️ Ethics & Rules of Engagement
Only test systems you own or are explicitly authorized to assess. Unauthorized testing is illegal and unethical. When you find issues, follow responsible disclosure or bounty program processes.

---

Follow **@cybersecplayground** for **Part 3: IDOR Automation & Bug Bounty Reports** 🔥

#IDOR #WebSecurity #BugBounty #UUID #APISecurity #PenTesting
