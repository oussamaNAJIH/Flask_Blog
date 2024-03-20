import secrets

# Generate a random string of 24 bytes
secret_key = secrets.token_hex(16).decode('utf-8')

print(secret_key)
