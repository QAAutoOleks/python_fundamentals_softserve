class Singltone():

    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            # If it doesn't exist yet, then
            # call __new__ of the parent class
            cls.obj = object.__new__(cls, *args, **kwargs)

        return cls.obj # returns Singltone