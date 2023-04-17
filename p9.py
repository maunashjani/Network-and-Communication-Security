from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import xml.etree.ElementTree as ET
import base64

# Initialize the encryption key
key = get_random_bytes(16)

# Create an example XML string
xml_string = """<user>
    <username>JohnDoe</username>
    <password>password123</password>
</user>"""

# Parse the XML string into an ElementTree object
root = ET.fromstring(xml_string)

# Get the password node
password_node = root.find('password')

# Get the password value
password = password_node.text

# Convert the password to bytes and pad to a multiple of 16 bytes (AES block size)
padded_password = pad(password.encode('utf-8'), AES.block_size)

# Generate a random nonce and encrypt the password using AES.EAX mode
nonce = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(padded_password)

# Base64 encode the encrypted password, nonce, and tag
base64_encrypted_password = base64.b64encode(ciphertext).decode('utf-8')
base64_nonce = base64.b64encode(nonce).decode('utf-8')
base64_tag = base64.b64encode(tag).decode('utf-8')

# Set the encrypted password, nonce, and tag as the node values
password_node.text = base64_encrypted_password
password_node.set('nonce', base64_nonce)
password_node.set('tag', base64_tag)

# Print the encrypted XML
print(ET.tostring(root).decode('utf-8'))

# Decrypt the password
base64_encrypted_password = password_node.text
base64_nonce = password_node.get('nonce')
base64_tag = password_node.get('tag')

encrypted_password = base64.b64decode(base64_encrypted_password.encode('utf-8'))
nonce = base64.b64decode(base64_nonce.encode('utf-8'))
tag = base64.b64decode(base64_tag.encode('utf-8'))

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
padded_password = cipher.decrypt_and_verify(encrypted_password, tag)
password = unpad(padded_password, AES.block_size).decode('utf-8')

# Print the decrypted password
print('Decrypted password:', password)
