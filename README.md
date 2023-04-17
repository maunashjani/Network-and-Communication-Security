# Network-and-Communication-Security
Network and Communication Security - Python programs


Python Packages:

pip install pymysql
pip install pycryptodome
pip install cryptography
pip install dkimpy
pip install paramiko

1 - Write a program to store username and password in an encrypted form in a database to implement integrity lock.
=> File(s): p1.py   
=> Create a MySQL database table users (schema: id, username, password) for a database named test     
=> The program uses AES algorithm to encrypt the password and store in database.   
   
2 - Write a program to implement SSL.   
=> File(s): p4.py, p4_1.py   
=> p4_1.py code generates server.crt and server.key for a localhost self signed SSL certificate   
=> SSL certficate files can also be generated using openssl    
=> >openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt   
   
3 - Write a program to send an encrypted email.   
=> File(s): p5.py   
=> The code uses cryptography package Fernet module to generate key for encryption.   
   
4 - Write a program to digitally sign MIME to create an 'opaque' signature.   
=> File(s): p6.py   
=> The code uses dkim package to generate a digital signature using RSA algorithm   
   
5 - Write a program to generate a DSA SSH key.   
=> File(s): p7.py   
=> The code uses paramiko package to generate DSA key   
=> >Note: DSA keys are no longer recommended for use due to security concerns. It's recommended to use RSA or Ed25519 keys instead.   
   
6 - Write a program to implement multilevel security.   
=> File(s): p8.py, demo.txt   
=> The code has 4 security levels: top secret, secret, confidential, unclassified.   
=> demo.txt is a sample text file used to grant/deny access to the file based on security level given as input.   
   
7 - Write a program to demonstrate how to encrypt and decrypt the content of an XML node using 128-bit CBC AES encryption.   
=> File(s): p9.py   
=> For, the xml data:   
   ```xml
   <user>  
      <username>JohnDoe</username>  
      <password>password123</password>  
   </user>
   ```
   
The password node is encrypted and decrypted.
