import os
from sys import platform
if os.path.isdir("venv"):
    if not os.path.isdir("migrations"):
        os.system("flask db init")
        os.system("flask db migrate")
        os.system("flask db upgrade")
    else:
        pass
    os.system("flask run")
else:
    os.system("python -m venv venv")
    print("\nplease activate virtual environment, and then install requirements.txt using pip before running this program again!\n\nTo activate virtual environment;")
    if not (platform == "win32"): 
        print("if you are on linux, type `venv/bin/activate`")
    else:  
        print("if you are on windows, type `venv/Scripts/activate`")
    

