import random
import time
while True:
    a = ''
    for i in range(0, 5):
        a += str(random.randint(0, 9))
    print(a)
    time.sleep(2)
    print('\n'*100)
    b = input()
    if b == a:
        print('yes')
    elif b != a:
        print('poprobui eshe raz')



