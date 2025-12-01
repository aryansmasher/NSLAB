import hashlib

msg1 = input("Enter original message:")
msg2 = input("Eneter recieved message:")

hash1 = hashlib.sha256(msg1.encode()).hexdigest()
hash2 = hashlib.sha256(msg2.encode()).hexdigest()

print("\nOriginal Hash:", hash1)
print("\nReceived Hash:", hash2)

if hash1 == hash2:
    print("\n[+] Integrity verified (Hash Matched!)")
else:
    print("\n[-] Tampering detected (Hash Do not Match!!)")
