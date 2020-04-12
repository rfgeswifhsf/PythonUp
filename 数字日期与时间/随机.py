import random

values=[1,2,3,4,5,6]
print(random.choice(values)) #1
print(random.sample(values,2)) #[6,3]
random.shuffle(values) # 洗牌
print(values)

print(random.randint(0,10))
print(random.random())
print(random.randrange(100,1,-2))

