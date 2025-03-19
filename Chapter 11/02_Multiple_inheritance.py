class Employee:
    company = "ITC"
    name = "Raj"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printLanguages(self):
        print(f"Out of all Language here is your Language: {self.language}")


class Programmer(Employee, coder):
    company= "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and it  is good with {self.language} language")

a= Employee()
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()

