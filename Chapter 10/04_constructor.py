class Employee:
    language= "py"          #This is a class attribute
    salary= "1200000"

    def __init__(self, name, salary,language):                     #This is dunder method which is automatically called when ever a object is made
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod          
    def greet():
        print(f"Good morning")

raj= Employee("Raj",1300000,"C++")
# raj.name = "Raj"
raj.language= "Javascript"            
print(raj.name, raj.salary, raj.language)