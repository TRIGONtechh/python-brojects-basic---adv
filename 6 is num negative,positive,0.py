# write a program to check if a num is =ve,-ve, or 0

# 1.method 

class check_vr():
    
    def __init__(self,val):
        self.val = val
    
    def check(self):
        if self.val < 0:
         print("negative value- ")
         return self.val
        
        elif self.val > 0:
         print("positive value- ")
         return self.val
        
        else:
         print("0")
         return self.val


user_vaule = float(input("Enter a value 'm1': "))
ch = check_vr(user_vaule)
print(ch.check())





# 2. method
while True:
    value = float(input("\nEnetr a value ;m2' : "))

    if value < 0:
        print("negative value- ")
        
    elif value > 0:
        print("positive value- ")
        
    else:
        print("0")
        
    