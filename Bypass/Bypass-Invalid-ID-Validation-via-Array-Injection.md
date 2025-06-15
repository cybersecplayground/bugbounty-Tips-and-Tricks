# 🚨 Bug Bounty Trick: Bypass Invalid ID Validation via Array Injection 🧠

> Sometimes a small change makes a big difference!

🔍 Original Request:

```
DELETE /api/bookings?bookings=3777104
```

> ❌ Response: 400 Bad Request — "Invalid Bookings"


**✅ Modified Request:**
```
DELETE /api/bookings?bookings[]=3777104
```
> 💥 Response: 200 OK — Booking successfully deleted!

**📌 Why This Works:**   
Some backends treat bookings= as a scalar (single ID), while bookings[]= is interpreted as an array of IDs.

If the API logic expects an array, this simple tweak can bypass input validation or authorization checks, potentially leading to:

🛑 IDOR (Insecure Direct Object Reference)
🗑 Unauthorized Deletion of Bookings
📬 Mass Resource Tampering (loop over IDs)

🔧 Tip: Always test both forms:  
`param=value`   
`param[]=value`

…and watch how the backend responds differently 🔎

📢 Stay sharp, test weird inputs, and keep hacking smart.
Follow @cybersecplayground for more tips like this.
👍 Like & 🔁 Share to help the community grow!

#bugbounty #api #idor #infosec #cybersec #websecurity #bypass #cybersecplayground
