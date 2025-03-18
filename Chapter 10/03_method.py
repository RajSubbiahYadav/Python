class Employee:
    language= "py"          #This is a class attribute
    salary= "1200000"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod           #we marked this function as staticmethod bec we are not using any object inside so we can directly access this function without self
    def greet():
        print(f"Good morning")

raj= Employee()
raj.language= "Javascript"             #This is a instance (object) attribute
raj.greet()
raj.getInfo() #this is converted into Employee.getInfo(raj) thats why we added self attribute in function