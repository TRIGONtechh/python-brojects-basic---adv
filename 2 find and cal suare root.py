# take out suare root of a var


# 1. method ---->

class sqrt():
    def __init__(self,a):
        self.a = a
        
    def sq(self):
        # print(f"square of {self.a}")
        return self.a ** 2
    
    def __str__(self):
       return f"square of {self.a}:"

    
find_sq =  sqrt(4)
print(find_sq,find_sq.sq())

# ----------------------------------------------------------------
# 2. mathod -->

var_1 = 5
print(f"\nsquare of {var_1} is:",var_1**2)
# square of 5: 25

# ----------------------------------------------------------------
# 3. user inpuer ---->

var_input = int(input("\nEnter a nmber want to square:"))
sq_var = var_input**2
print(f"square of {var_input} is:",sq_var)


# ------------------------------------------------------
# find root of var

# 1. method
num = 64
root_ = num **(1/2)
print(f"\nroot of {num} is:",root_)

# 2. method 
# using math module
import math 

num1 = int(input("\nEnter a number to root ir: "))
sr = math.sqrt(num1)
print(f"square root of {num1} is:-",sr)










