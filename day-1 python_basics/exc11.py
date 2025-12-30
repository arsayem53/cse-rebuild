"""
User has 3 attempts to enter correct password.
Correct password: "secure123"

After each wrong attempt, show remaining attempts.
If they get it right, print "Access granted!"
If they fail 3 times, print "Account locked!"

Example:
Enter password: wrong1
Incorrect! 2 attempts remaining.
Enter password: wrong2
Incorrect! 1 attempt remaining.
Enter password: secure123
Access granted!

Hint: Use a while loop with an attempt counter

"""
cpass = "secure123"
attempt = 1
while attempt < 4:
    epass = input("Enter password: ")
    if epass == cpass :
        print("Access Granted!")
        break
    else:
         print(f"Incorrect! {3-attempt} attempts remaining.")

    attempt = attempt + 1
else:
    print("Account locked!")