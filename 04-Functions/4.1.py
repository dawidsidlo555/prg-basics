import math
def triangle_area(a,b,c):
    d = ((a + b + c) /2)
    pole = math.sqrt(d*(d-a)*(d-b)*(d-c))
    return pole

print(triangle_area(3, 4, 5))
print(triangle_area(5, 12, 13))
print(triangle_area(7, 24, 25))