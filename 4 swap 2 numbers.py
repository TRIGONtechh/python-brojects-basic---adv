# swap two numbers

# 1. easy method

a = 3
b = 7
print("before swap:",b,a)

a,b = b,a
print("after swap:",a,b)

# ----------------------------------
# 2. method by 3rd variable
x = 7
y = 9
print(x,y)

temp = x
print("temp:",temp)
x = y
print(x,y)
y = temp
print(x,y)


#-----------------------------------
# 3. by class method
class swap_var():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def swap_(self):
        temp = self.x
        self.x = self.y 
        self.y = temp
        return self.x,self.y
    
    def __str__(self):
        return f"values are swaped:"
        
        
sw = swap_var(2,5)
print(sw,sw.swap_())


# ---------------------------------------
# 4. user input swap

var_1 = int(input("Enter the var 1:"))
var_2 = int(input("Enter the var 2:"))
print("before swaped values are:", var_1,var_2)
var_1,var_2 = var_2,var_1

# ------------ or ----------
# temp = var_1
# var_1 = var_2
# var_2 = temp

print("after swaped values are:", var_1,var_2)        
        
    
    
     