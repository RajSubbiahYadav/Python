class Employee:
    language= "py"          #This is a class attribute
    salary= "1200000"

raj= Employee()
raj.name= "Raj"             #This is a instance (object) attribute
print(raj.name, raj.language, raj.salary)

#Here name is instance (object) attribute and salary and language are class attributes as they directly belong to class 

kaushik = Employee()
kaushik.name= "Kaushik Yadav"
print(kaushik.name, kaushik.salary, kaushik.language)

