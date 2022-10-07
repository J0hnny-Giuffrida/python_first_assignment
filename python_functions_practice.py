def hello():
    print('Wassup man')


hello()
# ---------------------------------------


def pack(a, b, c):
    pack_list = [a, b, c]
    print(pack_list)


pack(1, 2, 3)

# ---------------------------------------


def eat_lunch(lunch):
    if len(lunch) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(lunch)):
            if i == 0:
                print('First I eat my', lunch[i])
            elif i > 0:
                print('Next I eat my', lunch[i])


my_lunch = ['sandwich', 'apple', 'crackers', 'walnuts', 'bananas']
eat_lunch(my_lunch)
