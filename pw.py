#! python3
# A very insure password manager
import sys, pyperclip

passwords = {"email": "password1", 
             "steam":"password2", 
             "airline": "password3"}

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()
account = sys.argv[1]       # First command line arg is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for " + account + " copied to clipboard.")
else:
    print("There is no account by the name of: " + account)
