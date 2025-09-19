
class Smartphone:
    def __init__(self,color,type,storage):
        self.color=color
        self.type=type
        self.__storage=storage #encapsulation-private

    def describe_phone(self):
        return f"This is a {self.color} {self.type} with {self.__storage}GB storage."

    def get_storage(self):
        return self.__storage
    
    def upgrade_storage(self,extra):
        if extra>0:
            self.__storage+=extra
            return f"You have upgraded your {self.type} to {self.__storage}GB successfully"
        else:
            print("Invalid upgrade amount!")

phone1=Smartphone('white','samsung', 8)
print(phone1.describe_phone()) 
print(phone1.upgrade_storage(64))

#Polymorphism
class car:
    def move(self):
        return "Car is driving"
class plane:
    def move(self):
        return "Plane is cruising"
for c in [car(),plane()]:
    print(c.move())