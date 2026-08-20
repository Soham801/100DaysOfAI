class Person:
    def __init__(self,name,age,gender):
        self.__name=name # Protected Variable
        self.__age=age # Proteted Variable
        self.gender=gender

        # Getter Method 

    def get_name(self):
        return self.__name

        # Setter Method
    def set_name(self,name):
        self.__name=name

person = Person("Soham",22,"Male")

print(person.get_name())
print(person.set_name("Sohammm"))

print(person.get_name())


