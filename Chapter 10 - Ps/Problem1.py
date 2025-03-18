class Programmer:
    company = "Microsoft"
    def __init__(self,name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Raj","12LPA",400053)
print(p.name,p.salary,p.pin,p.company)
k = Programmer("Kaushik","12LPA",400053)
print(k.name,k.salary,k.pin,k.company)