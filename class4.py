import random
score = 0
level = 2
fail = 0
module = 2
while True:
    a = int(input())
    b = random.randint(1, level)
    if b == a:
        print('Good job')
        score += 1
        print ('your score')
        print(score)
        level = 2 + int(score/module)
        print('your level')
        print(level)
    elif b != a:
        fail += 1
        print('your fails')
        print(fail)
        score -= 1
        print ('your score')
        print(score)
        print('poprobui eshe raz!')





