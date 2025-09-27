# 🐧 Tor IP Changer Setup Guide
![Tor IP Changer Setup Guide](https://github.com/user-attachments/assets/834688fe-eed6-4ccf-a3c6-74bd916ec486)

Automate IP rotation for penetration testing and privacy

**Repo:** https://github.com/isPique/Tor-IP-Changer

---

## 🔧 Step 1: Start Tor Service
First, ensure Tor is installed and running as a background service:

```bash
sudo apt install tor          # Install Tor
sudo systemctl start tor      # Start Tor service
sudo systemctl status tor     # Verify it's running
```

Tor runs on SOCKS port `9050` by default.  
Use `sudo systemctl restart tor` if you encounter connectivity issues.

---

## ⚡️ Step 2: Configure Tor IP Changer
The Python script automates IP rotation by signaling Tor's control port.

1. Clone the repository:
```bash
git clone https://github.com/isPique/Tor-IP-Changer.git
```

2. Navigate to the project directory:
```bash
cd Tor-IP-Changer
```

3. Install required libraries:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
sudo python3 IP-Changer.py
```

The script uses the Tor control port and sends the `SIGNAL NEWNYM` command to obtain a new circuit (new exit IP). Ensure the control port is enabled/configured in your Tor config if needed.

---

## 🔄 Step 3: Route Traffic with ProxyChains
ProxyChains redirects any application's traffic through Tor.

Edit `/etc/proxychains4.conf` and ensure these lines are set:

```
dynamic_chain
proxy_dns
socks5 127.0.0.1 9050
```

### ⚡ Usage Examples:
```bash
proxychains nmap -sT target.com
proxychains firefox example.com
```

ProxyChains works with most CLI and GUI applications and prevents DNS leaks by routing DNS queries through Tor.

---

## 💡 Pro Tips
- Check your IP: `proxychains curl https://icanhazip.com`
- Avoid rapid rotation: Tor may throttle `NEWNYM` requests faster than every ~10 seconds.
- Combine with VPNs or additional proxies for advanced chaining (see `proxychains.conf`).
- If ControlPort is disabled, enable and secure it in `/etc/tor/torrc` before using automation scripts.

---

## ⚠️ Important Notes
- Use only for authorized testing and legal privacy purposes.
- Tor exit nodes may be blocked by some services.
- No tool guarantees perfect anonymity.

---

Like/Give star if this helped! 🚀  
Follow **@cybersecplayground** for more tool guides.

#Tor #Privacy #PenTesting #ProxyChains #CyberSecurity
