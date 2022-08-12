import random
print("**Password Generator**")
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']
spl_char=['!','@','#','$','%','^','&','*','(',')','+','=','*']
x=int(input("Number of Alphabets  you  Need in your Password :"))
y=int(input("Total Number of Special Characters You need in your Password :"))
z=int(input("Total No of Numbers You need in your password :"))
g=[]
for char in range(0,x):
    r_char=random.choice(Alphabet)
    g+=r_char
#print(g)

for spl in range(0,y):
    r_spl=random.choice(spl_char)
    g+=r_spl
#print(h)

for num in range(0,z):
    r_num=random.choice(number)
    g+=r_num



random.shuffle(g)
i=""
for x in g:
    i+=x
print(f"The Recommended Strong Password is  :{i}")
