#Day_4

"""
Course Grade Application:
    - Create 5 students. Ask these students from the user.
    - Each of these students should have a midterm grade, project grade, and final grade.
    - Each student will have a course passing grade.
    - passingGrade=midterm*(0.3)+project*(0.3)+final*(0.4) passing grade should be determined like this.
    - Create a dictionary that keeps these students' information.
    - Calculate the students' grades and transfer them to the list with the help of indexing.
    - Finally, set the students with the highest grade to be in the first index and the student with the lowest grade to be in the last index of the list.
"""

students_list=[]
users=["Ahmet","Mehmet","Ayşe","Fatma","Ali"]

while len(users)>0:
    name=input("Please enter your name:  ")
    # \n Attention! All information can be entered only once.
    
    if name in users:
        student_dict={}
        student_dict["name"]=name
        try:
            name = str(name)  
            print("Hello {}!".format(name))
            
            ID=str(input("Please enter your student ID:  "))
            ms=int(input("Please enter your midterm score:  "))
            ps=int(input("Please enter your project score:  "))
            fs=int(input("Please enter your final score:  "))
            pg = int(ms*0.3 + ps*0.3 + fs*0.4) 
            
            student_dict["ID"]=ID
            student_dict["midterm_score"]=ms
            student_dict["project_score"]=ps
            student_dict["final_score"]=fs
            student_dict["passing_grade"]=pg
            
            students_list.append(student_dict)
            users.remove(name)
            
            print(name)
            print("Your total score:  ", student_dict["passing_grade"])
            print(users)
            print(student_dict)
            
            print("The original dictionary (list with dictionary) is : " + str(students_list))
            print ("The dictionary printed sorting by passing grade: ")
            print (sorted(students_list, key = lambda i: i['passing_grade'], reverse=True))
            
        except (ValueError, TypeError):
            print("Please enter valid information!")
               
    else:
        print("The name is not registered in this course.")
    break
