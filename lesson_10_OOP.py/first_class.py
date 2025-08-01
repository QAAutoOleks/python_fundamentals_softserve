class A:

    def __init__(self, name, colour, kind='None'):
        self.name = name
        self.colour = colour
        self.kind = kind

    def sing_song(self, name_song):        
        return f'Parrot {self.name} sings song {name_song}'
    

parrot = A('Ra', 'turquoise')
print(parrot.sing_song('Lalala'))

# A.sing_song('happy') - TypeError because odject is not created
print(A.sing_song(parrot, 'happy')) # Parrot Ra sings song happy