import pymysql.cursors
from Crypto.Cipher import AES

# key must be 16, 24, or 32 bytes long
key = b'0123456789abcdef0123456789abcdef'
cipher = AES.new(key, AES.MODE_EAX)

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='test',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Get username and password from user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Convert password to bytes
password_bytes = password.encode('utf-8')

# Encrypt the password
ciphertext, tag = cipher.encrypt_and_digest(password_bytes)

# Insert the encrypted username and password into the database
try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, ciphertext.hex()))
    connection.commit()
    print("Username and password saved successfully!")
except:
    connection.rollback()
    print("Error occurred while saving username and password.")

# Decrypt the password
cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
plaintext_bytes = cipher.decrypt_and_verify(ciphertext, tag)

# Convert plaintext to string
plaintext = plaintext_bytes.decode('utf-8')

# Print the decrypted password
print("Saved username: ", username)
# Print the decrypted password
print("Decrypted password: ", plaintext)

# Close the database connection
connection.close()