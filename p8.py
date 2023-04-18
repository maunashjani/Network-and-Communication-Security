import os

# Define the available security clearance levels
security_levels = {
    'top secret': 3,
    'secret': 2,
    'confidential': 1,
    'unclassified': 0
}

# Prompt the user for their security clearance level
print("Enter your security clearance level:")
for clearance in security_levels.keys():
    print(f"  {clearance}")
user_clearance = input("> ").lower()

# Make sure the user's clearance level is valid
if user_clearance not in security_levels.keys():
    print("Invalid security clearance level.")
    exit()

# Open the file and read its contents
filename = "demo.txt"
with open(filename, "r") as f:
    contents = f.read()

# Restrict access to the file based on the user's clearance level
file_clearance = security_levels['secret']
#print(user_clearance)
#print(file_clearance)

if security_levels[user_clearance] >= file_clearance:
    print("Access granted.")
    print(contents)
else:
    print("Access denied.")
