#Day_3:

"""
User login application:
    - Get Username and Password values from the user.
    - Check the values in an if statement and tell the user if they were successful.

"""


users=["Ahmet","Mehmet","Ayşe"]
passwords=["qwerty"]

username=input('Please enter username? ')
password=input('Please enter password? ')


if username in users and password in passwords:
    print('Succesfully login!')
else:
    print('Incorrect!')

