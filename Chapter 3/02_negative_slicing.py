name = "Hanuman"
#slice [start : end-1] #name[0:4] =>Hanu
print(name[0:4])

print(name[-4:-1]) #uma
print(name[3:6]) #uma

print(name[:6]) # is same as print(name[0:6])
print(name[1:]) # is same as print(name[1:7])
print(name[1:7])


#Slice with Skip Value [ start: end-1 :skip value]
print(name[:6:2]) #Hnm
print(name[:6:3]) #Hu

a = "abcdefghijklmnopqrstuvwxyz"
print(a[1:14:3])# behkn