class Person:
    def __init__(self,name):
        self.name=name
    
    def greet(self,greetings):
        return print("Hello {}, my name is {}".format(greetings,self.name))

jack = Person("Jack")
jill = Person("Jill")

jack.greet("Jill")
jack.greet("Mary")

jack.name