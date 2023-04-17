import paramiko
import os

# Generate a DSA key pair
key = paramiko.DSSKey.generate(2048)

# Save the private key to a file
private_key_file = os.path.expanduser('id_dsa')
key.write_private_key_file(private_key_file)

# Save the public key to a file
public_key_file = os.path.expanduser('id_dsa.pub')
with open(public_key_file, 'w') as f:
    f.write(key.get_base64())