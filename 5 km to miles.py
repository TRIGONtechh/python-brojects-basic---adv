# convert kilometer to miles

# 1 kilometer = 0.621 miles 

# 1. method 

class kilom_to_miles():
    
    def __init__(self,kilometer):
            self.kilometer = kilometer
            
            
    def km_to_m(self):
        miles1 = 0.62137119
        return f"\n{self.kilometer} km = {self.kilometer * miles1} miles"

class miles_to_kilom():
    
    def __init__(self,miles):
        self.miles = miles
    
    def miles_to_km(self):
        
        mile1  =  0.62137119
        return f"\n{self.miles} miles = {self.miles/mile1} km"        
  

    
    
    
    
demo = kilom_to_miles(10)
print(demo.km_to_m())

demo2 = miles_to_kilom(4)
print(demo2.miles_to_km())







# 2. user input method
user_ask = int(input("To convet km to miles (1), \nand to convert miles to km (2): "))
if (user_ask < 1 or user_ask > 2):
    raise ValueError("1 or 2")

elif  (user_ask == 1 ):
    kilometer1 = float(input("Enter km value to convrt it to miles: "))
    miles1 = 0.62137119
    km_to_miles = kilometer1 * miles1
    print(km_to_miles)
    
elif(user_ask == 2):
    miles2 = float(input("Enter value to convert miles to km: "))
    miles_to_km = miles2/0.62137119
    print(miles_to_km)
    
    