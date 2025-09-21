# 📣 Weird Endpoint Behavior — What it tells you
![Weird Endpoint Behavior](https://github.com/user-attachments/assets/393f00a6-6c3c-4e8a-822e-71008432a331)

Observed responses for `GET /res-api/<ID>/...`:

- `/res-api/<ID>/qwertyasdf` → **404 Not Found**
- `/res-api/<ID>/` → **403 Forbidden**
- `/res-api/<ID>/?anyparam` → **200 OK**

---

## 🧠 What this pattern suggests
- `status` is a public sub-resource (returns data).  
- Unknown subpaths return 404 — normal routing.  
- The base path without query → 403 (auth required / forbidden).  
- Adding any query param to the base path flips it to 200 OK — indicates the backend treats the presence of a query string differently (possible routing, auth bypass, or fallback behavior).

---

## ⚠️ Why this is interesting (attack surface)
- **Auth/Access bypass:** If `/res-api/<ID>/?anyparam` returns 200 while `/res-api/<ID>/` is 403, a parameter-driven bypass might let unauthenticated users access resources.  
- **Logic differences:** The app may route requests differently when a query string is present (different middleware, different handler). That discrepancy can reveal misconfigurations.  
- **Hidden behavior:** Could be leftover debug/feature flags, permissive caching layer, or an API gateway quirk.

---

## 🛠 Quick tests to run (ethically, with permission)
- Try different params: `?a=1`, `?debug=1`, `?preview=true` — see if content changes.  
- Test HTTP methods: `GET`, `POST`, `PUT`, `HEAD` on `/res-api/<ID>/?anyparam`.  
- Inspect headers returned for `200` vs `403` (cookies, auth, server, `x-powered-by`).  
- Check response body for sensitive fields (IDs, emails, tokens).  
- Attempt parameter-based escalation: `?id=<other-id>`, `?user=admin`.  
- Try path normalization or encoding: `/res-api/%3CID%3E/?anyparam` or trailing slashes.  
- Use Burp Repeater + Intruder to fuzz params & headers; grep for differences.  
- Test whether query param bypass works for sensitive endpoints (write/delete actions) — only on authorized test targets.

---

## 🛡 How developers should fix this
- Normalize request handling: apply the same auth logic for `path/` and `path/?` variants.  
- Ensure middleware/auth runs for all route variants (with or without query params).  
- Add consistent canonicalization (redirect or 403) and document expected behaviour.  
- Audit API gateway/proxy rules for query-string based routing.

---

💬 Found this useful? Follow **@cybersecplayground** for daily bug-hunting tips, payloads, and defensive checklists.

🔁 Share with your team — small quirks like this lead to big finds.

#bugbounty #infosec #apitesting #recon #authbypass #cybersecplayground
