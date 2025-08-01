class Singltone():

    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            # If it doesn't exist yet, then
            # call __new__ of the parent class
            cls.obj = object.__new__(cls, *args, **kwargs)

        return cls.obj # returns Singltone
    

object1 = Singltone()
print(object1)

object1.attribute = 10

object2 = Singltone()
print(object1)
print(object2)
print('Attribute of object2:', object2.attribute)