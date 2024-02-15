#  password generator
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="{}$%#&!?@^*()+"
all=lower+upper+numbers+symbols
length=int(input("enter length to generate password:"))
password="".join(random.sample(all,length))
#for i in range(5):
 # password="".join(random.sample(all,length)) 
print(password)