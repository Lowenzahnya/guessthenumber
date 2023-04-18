import random
length = 5
passwd = list('abc')
print(random.choice(passwd))
passwd = ''.join([random.choice(passwd) for x in range(length)])
print(passwd)
