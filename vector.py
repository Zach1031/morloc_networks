class Vector():
    '''
    def __init__(self):
        self.vector = []
        self.length = 0
    '''
    
    '''
    def __init__(self, length):
        self.vector = [0] * length
        self.length = length
    '''
    
    def __init__(self, vector):
        self.vector = vector
        self.length = len(vector)
    
    def scale(self, k):
        for i in range(self.length):
            self.vector[i] = k * self.vector[i]
        return self
    
    def get(self, pos):
        return self.vector[pos]
    
    def __str__(self):
        return ' '.join(str(num) for num in self.vector)

    
    def add(vector1, vector2):
        if not (vector1.length == vector2.length):
            return -1
        
        new_vector = [0] * vector1.length
        for i in range(vector1.length):
            new_vector[i] = vector1.get(i) + vector2.get(i)
        
        return Vector(new_vector)


#vec1 = Vector([1,2,3])
#vec2 = Vector([2,3,4, 5])
#print(vec1)
#print(vec1.scale(12))
#print(Vector.add(vec1, vec2))