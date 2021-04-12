#Day_3:

"""
Extra:
    - Try building tha same user login application but this time, use a dictionary.
    
"""


dic = {"Ahmet":"111","Mehmet":"222","Ayşe":"333"}

username=input('Please enter username? ')
password=input('Please enter password? ')

for k, v in dic.items():
    if username == k and password == v: 
        print('Succesfully login!')
    elif username != k or password != v:
        print('Unsuccesfully login!')
    break
