class A:

    def __init__(self, name, colour, kind='None'):
        self.name = name
        self.colour = colour
        self.kind = kind

    def sing_song(self, name_song):        
        print(f'Parrot {self.name} sing song {name_song}')