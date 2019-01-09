class Human(object):
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    adam, eve = Man(), Woman()
    return [adam, eve]