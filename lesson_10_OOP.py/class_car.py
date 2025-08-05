class Car:

    status = 'Stop'

    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def run_method(self):
        self.__class__.status = 'Run'
        print('Car started')

    def stop_method(self):
        self.__class__.status = 'Stop'
        print('Car stopped')