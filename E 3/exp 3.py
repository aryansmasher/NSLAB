import hashlib
import time
import random

SECRET = "network_key"
MAX_TIME_GAP = 5

def make_challenge():
    return str(random.randint(100000, 999999))

def get_hash(data, key):
    return hashlib.sha256((data + key).encode()).hexdigest()

def auth_basic():
    print("BASIC AUTH")

    challenge = make_challenge()
    print(f"Server challenge: {challenge}")

    client_hash = get_hash(challenge, SECRET)
    print(f"Client response: {client_hash}")

    server_hash = get_hash(challenge, SECRET)

    if client_hash == server_hash:
        print(" Auth OK")
        return True
    else:
        print(" Auth Failed")
        return False

def auth_secure():
    print("\nSECURE")

    challenge = make_challenge()
    print(f"Server challenge: {challenge}")

    timestamp = str(int(time.time()))
    client_data = challenge + timestamp
    client_hash = get_hash(client_data, SECRET)

    print(f"Client timestamp: {timestamp}")
    print(f"Client response: {client_hash}")

    server_time = int(time.time())
    client_time = int(timestamp)
    time_diff = abs(server_time - client_time)

    print(f"Time gap: {time_diff}s")

    if time_diff > MAX_TIME_GAP:
        print(" Replay attack!")
        return False

    server_hash = get_hash(challenge + timestamp, SECRET)

    if client_hash == server_hash:
        print(" Auth OK with replay protection")
        return True
    else:
        print(" Auth Failed")
        return False

def show_attack():
    print("\nATTACK DEMO")

    challenge = make_challenge()
    timestamp = str(int(time.time()))
    real_hash = get_hash(challenge + timestamp, SECRET)

    print(f"Real transaction: {real_hash}")

    time.sleep(2)
    server_time = int(time.time())
    time_diff = abs(server_time - int(timestamp))

    print(f"Replay after {time_diff}s")

    if time_diff > MAX_TIME_GAP:
        print(" Attack blocked!")
    else:
        print(" Attack might work!")

if __name__ == "__main__":
    print("Auth System")
    print("=" * 20)

    auth_basic()
    auth_secure()
    show_attack()
