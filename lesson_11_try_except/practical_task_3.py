class InputError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

def test_input(text):
    try:
        if not isinstance(text, (str, int, float)):
            raise ImportError('Type text error')
        elif len(text) < 3:
            raise ImportError('Short text error')
        elif len(text) > 15:
            raise ImportError('Long text error')
        else:
            return True
    except ImportError as error:
        return error
    
print(test_input({}))