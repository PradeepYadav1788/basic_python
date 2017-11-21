class X:

    #def __init__(self):
            
    def insert(self, a, b):
        self.a=1000
        self.b=2000

    def display(self):
        return { 
            'a': self.a,
            'b': self.b
        }

    def modify (self, b, c):
        self.a = self.a + b
        self.b = self.b + c
        return { 
            'a': self.a,
            'b': self.b
        }