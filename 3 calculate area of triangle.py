# cal area of triangle

# 1. method

class triangle():
    def __init__(self,b,h):
        self.b = b
        self.h = h
        
    def cal_ar_tri(self):
        return (1/2)* self.b * self.h
    
    def __str__(self):
        return "area of triangle is 'm1':"
    
    
value_ = triangle(3,5)
print(value_,value_.cal_ar_tri())


# -------------------------------------------
# 2. method user input
length = int(input("\nEneter the lenth of triangle 'm2':-"))
breth = int(input("Enter the breth of the triangle 'm2':-"))
ar_of_tri = (1/2) * length * breth
print("area of trianglr is:-",ar_of_tri)


# -----------------------------------------------------
# 3. value during execution

length = 44
breth = 23
ar_of_tri = (1/2) * length * breth
print("\narea of trianglr is 'm3':-",ar_of_tri)

