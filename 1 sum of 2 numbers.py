# sum of 2 numbers



# 1. pre defined variables
class sum_2var:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b

a = sum_2var(1,4)
print(a.add())

# -------------------------------------------------
# 2. user input variables

var1_input = int(input("Enter 1st var:- "))
var2_input = int(input("Enter 1st var:- "))
print("sum of two number is: ", (var1_input + var2_input))


# ---------------------------------------------------
# 3. var given during the construction

a  = 12
b = 24
c = a+b
print("sum of a and b is: ", (a))
