from random import randint

class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(250,5555)}")

t = Train(21200)
t.book("Dadar","Tirunelveli")
t.getStatus()
t.getFare("Dadar","Tirunelveli")