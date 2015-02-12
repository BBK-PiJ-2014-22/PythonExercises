class Person:
    'This is a person'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayName(self):
        print("My name is ", self.name)

    def sayAge(self):
        print("I am",str(self.age)," years old")

    def getOlder(self):
        self.age += 1


person = Person("Jamie", 29)
person.sayName()
person.sayAge()
person.getOlder()
person.sayAge()
    
person2 = Person("Bob",50)
person2.sayName()
person2.sayAge()
person2.getOlder()
person2.sayAge()

person.sayAge()
                 
