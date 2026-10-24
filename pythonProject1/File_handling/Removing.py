import os
if os.path.exists("ABC.py"):
    os.remove("ABC.py")
    print("file removed successfully!")
else:
    print("file does not exist!")