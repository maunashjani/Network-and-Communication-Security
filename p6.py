import dkim
from email.mime.text import MIMEText

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate a new RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Serialize the private key to PEM format
pem_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# The message to sign
msg = MIMEText("This is a test message.")

# Add headers
msg['From'] = 'sender@example.com'
msg['To'] = 'recipient@example.com'
msg['Subject'] = 'Test Message'

# Set up the DKIM signature
selector = b'myselector'
domain = b'example.com'

headers = ['From', 'To', 'Subject']
signature = dkim.sign(
    message=msg.as_bytes(),
    selector=selector,
    domain=domain,
    privkey= pem_bytes,
    identity= None,
    canonicalize=(b'relaxed', b'simple'),
    signature_algorithm=b'rsa-sha256',
    include_headers=headers
)

# Add the signature header to the message
msg['DKIM-Signature'] = signature.decode()

# Print the signed message
print(msg.as_string())