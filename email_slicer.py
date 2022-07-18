# Email Slicer with Python
email = input("Enter your email address : ").strip()
# using strip() function to remove white spaces
username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]
print("your username is ", username, "," "and your domain name is ", domain_name)
