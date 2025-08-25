## Comprehensive Web Application Security Testing Checklist

Introduction
This checklist provides a structured approach to web application security testing, covering reconnaissance, vulnerability assessment, and exploitation techniques based on OWASP Top 10 2023 and other critical security risks.

--- 
## Phase 1: Reconnaissance & Information Gathering
### 1.1 Passive Reconnaissance
- [ ] DNS Enumeration
  - [ ] Perform WHOIS lookup
  - [ ] Extract DNS records (A, AAAA, MX, TXT, NS, SOA)
  - [ ] Check for DNS zone transfers
  - [ ] Identify subdomains using OSINT tools
- [ ] Search Engine Discovery
  - [ ] Google dorking for sensitive files
  - [ ] Review cached pages
  - [ ] Identify exposed documents and directories
- [ ] Infrastructure Analysis
  - [ ] Identify IP ranges and network blocks
  - [ ] Check for exposed services and ports
  - [ ] Analyze SSL/TLS certificates
  - [ ] Check for past data breaches

### 1.2 Active Reconnaissance
- [ ] Service Fingerprinting
  - [ ] Identify web server technologies
  - [ ] Detect application frameworks (CMS, JS frameworks)
  - [ ] Determine server-side technologies
- [ ] Content Discovery
  - [ ] Directory and file brute-forcing
  - [ ] Check for common backup files
  - [ ] Identify hidden parameters and endpoints
  - [ ] Check for exposed development files
- [ ] Application Mapping
  - [ ] Spider/crawl entire application
  - [ ] Identify all input points and parameters
  - [ ] Map authentication and authorization flows

## Phase 2: Configuration & Deployment Testing
### 2.1 Infrastructure Configuration
- [ ] HTTP Headers Analysis
  - [ ] Check security headers (CSP, HSTS, X-Frame-Options)
  - [ ] Analyze server header information leakage
  - [ ] Verify cookie security attributes
- [ ] SSL/TLS Testing
  - [ ] Check certificate validity and configuration
  - [ ] Test for weak ciphers and protocols
  - [ ] Verify certificate transparency
- [ ] HTTP Methods Testing
  - [ ] Test allowed HTTP methods
  - [ ] Check for dangerous methods (PUT, DELETE, TRACE)
  - [ ] Test HTTP method overriding

### 2.2 Application Configuration
- [ ] Error Handling
  - [ ] Provoke and analyze error messages
  - [ ] Check for information leakage in errors
  - [ ] Verify custom error pages
- [ ] File Extensions Handling
  - [ ] Test for unexpected file processing
  - [ ] Check for source code leakage
- [ ] Backup and Unreferenced Files
  - [ ] Check for backup files (.bak, .old, .tmp)
  - [ ] Identify orphaned or unreferenced pages

## Phase 3: Identity & Access Management Testing
### 3.1 Authentication Testing
- [ ] User Enumeration
  - [ ] Test for username enumeration via login, registration, and password reset
- [ ] Default Credentials
  - [ ] Test for default accounts and weak passwords
- [ ] Brute Force Protection
  - [ ] Check for account lockout mechanisms
  - [ ] Test rate limiting on authentication endpoints
- [ ] Password Policy
  - [ ] Test password complexity requirements
  - [ ] Check password recovery process security
- [ ] Multi-Factor Authentication
  - [ ] Test bypass techniques for 2FA/MFA
  - [ ] Check for MFA bypass using session manipulation

### 3.2 Session Management Testing
- [ ] Session Token Analysis
  - [ ] Check token randomness and predictability
  - [ ] Test for token fixation vulnerabilities
  - [ ] Verify token expiration after logout and inactivity
- [ ] Cookie Attributes
  - [ ] Verify Secure, HttpOnly, and SameSite flags
  - [ ] Check scope and path attributes
- [ ] Session Hijacking
  - [ ] Test for session exposure in URLs
  - [ ] Check for session sidejacking possibilities

### 3.3 Authorization Testing
- [ ] Vertical Privilege Escalation
  - [ ] Test access to administrative functions
  - [ ] Check for parameter-based authorization bypass
- [ ] Horizontal Privilege Escalation
  - [ ] Test access to other users' data
  - [ ] Verify IDOR (Insecure Direct Object Reference) vulnerabilities
- [ ] Missing Function Level Access Control
  - [ ] Test direct access to privileged endpoints

## Phase 4: Input Validation Testing
### 4.1 Injection Testing
- [ ] SQL Injection
  - [ ] Test for error-based, union-based, blind SQLi
  - [ ] Test for time-based SQL injection
  - [ ] Test second-order SQL injection
- [ ] NoSQL Injection
  - [ ] Test MongoDB injection vectors
  - [ ] Test CouchDB injection vectors
- [ ] OS Command Injection
  - [ ] Test for command execution via application inputs
- [ ] LDAP Injection
  - [ ] Test LDAP query manipulation
- [ ] XPath Injection
  - [ ] Test XPath query manipulation

### 4.2 Cross-Site Scripting (XSS) Testing
- [ ] Reflected XSS
  - [ ] Test all input vectors with XSS payloads
- [ ] Stored XSS
  - [ ] Test all data storage points with XSS payloads
- [ ] DOM-based XSS
  - [ ] Analyze client-side code for DOM manipulation vulnerabilities
- [ ] Bypass Techniques
  - [ ] Test WAF and filter bypass techniques
  - [ ] Test in different contexts (HTML, JavaScript, CSS)

### 4.3 Other Input Validation Tests
- [ ] File Upload Vulnerabilities
  - [ ] Test for unrestricted file upload
  - [ ] Verify file type restrictions bypass
- [ ] XML External Entity (XXE) Injection
  - [ ] Test for XXE in XML processors
  - [ ] Test for XXE via file uploads
- [ ] Server-Side Request Forgery (SSRF)
  - [ ] Test for SSRF in URL parameters
  - [ ] Test for cloud metadata service access

## Phase 5: Business Logic Testing
### 5.1 Workflow Validation
- [ ] Process Timing Tests
  - [ ] Test for race conditions
  - [ ] Check for time-of-check to time-of-use (TOCTOU) flaws
- [ ] Pricing Manipulation
  - [ ] Test for cart/price manipulation
  - [ ] Verify coupon/discount abuse scenarios
- [ ] Quantity Manipulation
  - [ ] Test for negative values, decimal values, extremely large values

### 5.2 Application Specific Logic
- [ ] Authentication Bypass
  - [ ] Test for alternative authentication paths
  - [ ] Check for parameter manipulation in multi-step processes
- [ ] Privilege Escalation
  - [ ] Test for hidden functionalities
  - [ ] Check for client-side controls bypass

## Phase 6: Client-Side Testing
### 6.1 DOM-based Vulnerabilities
- [ ] DOM XSS
  - [ ] Test sources and sinks in client-side code
- [ ] JavaScript Execution
  - [ ] Test for client-side code injection
- [ ] Client-Side Storage
  - [ ] Check localStorage, sessionStorage for sensitive data
  - [ ] Verify client-side caching mechanisms

### 6.2 Cross-Origin Issues
- [ ] Cross-Origin Resource Sharing (CORS)
  - [ ] Test CORS configuration weaknesses
  - [ ] Check for overly permissive CORS headers
- [ ] JSONP Endpoints
  - [ ] Test JSONP endpoints for sensitive data leakage
- [ ] PostMessage Communication
  - [ ] Test postMessage implementation for security issues

## Phase 7: Other Tests
### 7.1 API Testing
- [ ] REST/GraphQL Testing
  - [ ] Test for broken object level authorization (BOLA)
  - [ ] Test for excessive data exposure
  - [ ] Check for mass assignment vulnerabilities
  - [ ] Test for injection in API endpoints
- [ ] Rate Limiting
  - [ ] Test for lack of rate limiting on API endpoints

### 7.2 Third-Party Components
- [ ] Known Vulnerabilities
  - [ ] Identify and test third-party libraries for known vulnerabilities
- [ ] Component Misconfiguration
  - [ ] Test default configurations of third-party components

## Phase 8: Post-Exploitation
### 8.1 Evidence Collection
- [ ] Proof of Concept
  - [ ] Document steps to reproduce vulnerabilities
  - [ ] Capture screenshots and videos
- [ ] Impact Assessment
  - [ ] Evaluate business impact of each finding
  - [ ] Determine exploitability and prevalence

### 8.2 Reporting
- [ ] Vulnerability Documentation
  - [ ] Write clear vulnerability descriptions
  - [ ] Provide remediation recommendations
  - [ ] Assign risk ratings based on CVSS

## Tools Checklist
###  Reconnaissance Tools
- Amass, Subfinder, Sublist3r (subdomain enumeration)   
- Nmap, Masscan (port scanning)   
- Waybackurls, Gau (content discovery)   
- FFuF, Dirsearch (directory brute-forcing)   

### Vulnerability Scanners
- OWASP ZAP, Burp Suite (general testing)   
- Nuclei (template-based scanning)   
- SQLmap (SQL injection testing)   
- XSStrike (XSS testing)   

### Manual Testing Tools
- Burp Suite (proxy and manual testing)   
- Browser developer tools (client-side analysis)   
- Curl, Postman (API testing)   
- Custom scripts (for specific tests)   


## Appendix: OWASP Top 10 2023 Mapping
| OWASP Top 10 2023 Category | Checklist Section |
|-----|-------|	
| A01: Broken Access Control | 3.3 Authorization Testing |
| A02: Cryptographic Failures | 2.1 SSL/TLS Testing, 4.2 Input Validation |
| A03: Injection | 4.1 Injection Testing |
| A04: Insecure Design | 5. Business Logic Testing |
| A05: Security Misconfiguration | 2. Configuration & Deployment Testing |
| A06: Vulnerable Components | 7.2 Third-Party Components |
| A07: Identification Failures | 3.1 Authentication Testing |
| A08: Software Integrity Failures | 7.2 Third-Party Components |
| A09: Security Logging & Monitoring Failures | 8.2 Reporting |
| A10: Server-Side Request Forgery | 4.3 Other Input Validation Tests |
--- 

## Conclusion
This comprehensive checklist covers the complete web application security testing process from reconnaissance to post-exploitation. Remember that security testing should be an iterative process, and this checklist should be adapted based on the specific application being tested.

Note: Always ensure you have proper authorization before testing any application. Unauthorized testing is illegal and unethical.
