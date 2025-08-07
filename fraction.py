# Fraction
import math
class Fraction():
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
        

    def simplify(self):
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    def __add__(self,other):
        tem_num = self.num * other.den + other.num * self.den
        tem_den = self.den * other.den  
        return '{}/{}'.format(tem_num,tem_den)
    def __sub__(self,other):
        tem_num = self.num * other.den - other.num * self.den
        tem_den = self.den * other.den
        return '{}/{}'.format(tem_num,tem_den)
    def __mul__(self,other):
        tem_num = self.num * other.num 
        tem_den = self.den * other.den
        tem_gcd = math.gcd(tem_num, tem_den)
        tem_num //= tem_gcd
        tem_den //= tem_gcd
        return '{}/{}'.format(tem_num,tem_den)
    def __truediv__(self,other):
        tem_num = self.num * other.den
        tem_den = self.den * other.num
        tem_gcd = math.gcd(tem_num, tem_den)
        tem_num //= tem_gcd
        tem_den //= tem_gcd
        return '{}/{}'.format(tem_num,tem_den)
    