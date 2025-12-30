c_username = "admin"
c_password = "python123"

in_username = input("Enter yoru user name: ")
in_password = input("Enter your password:")

if in_username == c_username and in_password == c_password :
    print(f"Login successful!")

elif in_username != c_username and in_password == c_password :
    print(f"Invalid Username!")

elif in_username == c_username and in_password != c_password :
    print(f"Invalid password!")

else:
    print(f"Invalid Credentials!")