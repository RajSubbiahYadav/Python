from random import randint

class Train:
    
    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to} is {randint(250,5555)}")

t = Train(21200)
t.book("Dadar","Tirunelveli")
t.getStatus()
t.getFare("Dadar","Tirunelveli")