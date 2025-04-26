### 🚀 Bypassing File Upload Restrictions: Exploiting Extension Blacklists Like a Pro! 🔥

> 🛠 Bypassing File Extension Exclusion Lists in Web Applications
Many web applications implement security measures that block the upload of potentially dangerous file types, such as .php or .jsp. However, attackers and penetration testers often find ways to bypass these restrictions by using alternative file extensions or exploiting misconfigurations in the system.

🧐 Why Does This Work?
- **Incomplete Blacklists** – Some web applications only block .php but forget other PHP-related extensions like .phtml or .php7.
- **MIME Type Validation Issues** – Some applications only check the MIME type, which can be spoofed.
- **Misconfigured Web Servers** – Web servers like Apache and Nginx may still execute certain alternate file extensions as code.
- **Double Extensions** – Some apps fail to properly filter filenames like shell.php.jpg, which may still execute if uploaded and accessed a certain way.

🔥 Extension Variations for Different Technologies

🔹 **PHP File Extensions (For Bypassing PHP Filters)**
- ✔️ `.phtml` – PHP interprets it as a valid script
- ✔️ `.php2`, `.php5`, `.php`7 – Older/newer PHP versions may process these
- ✔️ `.phar` – PHP Archive, sometimes executed as PHP
- ✔️ `.inc` – Intended for include files, but still processed as PHP in some setups

🔹 **ASP.NET File Extensions (For Windows/IIS Servers)**
- ✔️ .asp, .aspx – Classic and modern ASP.NET
- ✔️ .ashx, .asmx – Web handlers that may execute code
- ✔️ .cshtml, .vbhtml – Razor pages that execute server-side

🔹 **Java File Extensions (For JSP-based Servers)**
- ✔️ .jsp, .jspx – JavaServer Pages, executed by Tomcat
- ✔️ .jsw, .jsv, .jspf – Alternative JSP formats
- ✔️ .action, .do – Used in Java-based frameworks like Struts

🔹 **Other Extensions to Try**
- ✔️ .svg – Some applications allow SVG uploads, which can include JavaScript payloads
- ✔️ .html, .cgi – Might be interpreted as executable content in some configurations
- ✔️ .htaccess – Can be used to override settings and enable execution of certain files
- ✔️ .cfm – ColdFusion scripts, which may be processed if the server supports it

**🛠 Exploit Techniques**
- 🔹 Case Sensitivity – Some filters only block .php but allow .PHP
- 🔹 Double Extensions – shell.php.jpg might bypass restrictions but still execute if accessed in a certain way
- 🔹 Null Byte Injection – Some applications fail to properly handle %00, allowing uploads like shell.php%00.jpg
- 🔹 MIME Spoofing – Changing the Content-Type to image/jpeg might allow execution if validated poorly

**💡 Practical Example**
Let’s say an upload filter blocks .php, but the server still executes .phtml. You could try renaming your payload:

🚀 Original file: `shell.php`

🔄 Bypassed file: `shell.phtml`

If the web server processes `.phtml` as `PHP`, your shell will still execute!

⚠️ **How to Protect Against This?**
- ✅ Use a whitelist approach (only allow specific safe extensions like `.jpg`, `.png`, etc.)
- ✅ Check both extension and MIME type (don’t rely on one method alone)
- ✅ Deny execution in upload directories (configure web server rules to prevent execution)
- ✅ Sanitize filenames properly (remove special characters and prevent double extensions)

📢 Join [@cybersecplayground](https://t.me/cybersecplayground) for more bug bounty tips, hacking techniques, and security insights! 🚀💀
