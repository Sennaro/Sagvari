be= input("Kérem a robot parancsait:")
ki = ""
E = 0
N= 0
D = 0
K = 0

for n in str(be):
        if n == "E":
            E += 1

for n in str(be):
        if n == "N":
            N += 1
            
for n in str(be):
        if n == "D":
            D += 1

for n in str(be):
        if n == "K":
            K += 1

print("E betűk száma: ", E)
print("N betűk száma: ", N)
print("D betűk száma: ", D)
print("K betűk száma: ", K)

x = N-K
y = E-D

for i in range(x):
        if x > 0:
                ki += "K"
                x -= 1
        if x < 0:
                ki += "N"
                x += 1

for i in range(y):
        if y > 0:
                ki += "E"
                y -= 1
        if y < 0:
                ki += "D"
                y += 1

print(ki)
                



