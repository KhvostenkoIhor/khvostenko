from random import randint

def symm_dif(A, B):
    return (A ^ B)
    
def intersect(A, C):
    return (A & C)
    
def uni(A, B, C):
    return (A | B | C)
    
A = {randint(1, 20) for i in range(15)}
B = {randint(1, 20) for i in range(15)}
C = {randint(1, 20) for i in range(15)}

print("Set A", A, "Set B", B, "Set C", C, sep="\n")
print("-"*40)
print("Unique elements of A and B", symm_dif(A, B), sep="\n")
print("-"*40)
print("Common elements of A and C", intersect(A, C), sep="\n")
print("-"*40)
print("Union of all sets", uni(A, B, C), sep="\n")
