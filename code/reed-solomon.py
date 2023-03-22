#Création du corps de Forbenius 
n = 3
class F2n:
    def __init__(self, x):
        self.x = x & ((1 << n) - 1)
    
    def __add__(self, other):
        return F2n(self.x ^ other.x)
    
    def __sub__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        p = 0
        while other.x:
            if other.x & 1:
                p ^= self.x
            self.x <<= 1
            if self.x & (1 << n):
                self.x ^= 0b11
            other.x >>= 1
        return F2n(p)
    
    def __divmod__(self, other):
        inv = pow(other, 2**n - 2)
        q = self.__mul__(inv)
        return (q, self.__add__(q.__mul__(other).__neg__()))

    def __pow__(self, e):
        res = F2n(1)
        while e:
            if e & 1:
                res = res.__mul__(self)
            self = self.__mul__(self)
            e >>= 1
        return res
    
    def __neg__(self):
        return F2n(self.x)
    
    def __eq__(self, other):
        return self.x == other.x
    
    def __ne__(self, other):
        return self.x != other.x
    
    def __str__(self):
        return bin(self.x)[2:].zfill(n)

p = F2n(7)
q = F2n(14)
print (p.__str__())
print (p.__add__(q).__str__())
print (p.__pow__(4).__str__())
print (p.__mul__(q).__str__())