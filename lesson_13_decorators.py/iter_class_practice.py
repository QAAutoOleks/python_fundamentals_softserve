class ClassIter:

    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        
        if self.a < 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    

iter_obj = ClassIter()
iter(iter_obj)

print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
