import random


class Queue:  # a line, obviously
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # someone entering the line must pass every person in line O(n)
        self.items.insert(0, item)

    def dequeue(self):  # the first person in line just steps forward O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)

    # def __str__(self):        not subscriptable, need a different way to return all elements in Queue
    #    return self[:]


slst = random.sample(range(100, 1000), 15)

# print(slst)


# print(int("321"[len("321") - 1]))     ones place
# print(int("321"[len("321") - 2]))     tens place
# print(int("321"[len("321") - 3]))     hundreds place


def randix(lst):
    main_bin = Queue()
    for i in lst:
        main_bin.enqueue(i)
    print(f"main_bin start = {main_bin}")
    print(f"size = {main_bin.size()}")
    bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9 = Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()
    # I know theres a better way to format this ^^^^ look up later
    while main_bin.size() > 0:
        num = main_bin.dequeue()
        print(f"num = {num}")
        num_s = str(num)
        print(f"num_s = {num_s}")
        ones_place = int(num_s[len(num_s) - 1])
        # ^^^ issue right here ^^^
        print(ones_place)
        if ones_place == 0:
            bin_0.enqueue(num)
        elif ones_place == 1:
            bin_1.enqueue(num)
        elif ones_place == 2:
            bin_2.enqueue(num)
        elif ones_place == 3:
            bin_3.enqueue(num)
        elif ones_place == 4:
            bin_4.enqueue(num)
        elif ones_place == 5:
            bin_5.enqueue(num)
        elif ones_place == 6:
            bin_6.enqueue(num)
        elif ones_place == 7:
            bin_7.enqueue(num)
        elif ones_place == 8:
            bin_8.enqueue(num)
        else:
            bin_9.enqueue(num)
    print(main_bin)
    print(bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9)
    # realizing I should have made a bin class with a value characteristic, but oh well next time
    main_bin.enqueue(bin_0[:])
    main_bin.enqueue(bin_1[:])
    main_bin.enqueue(bin_2[:])
    main_bin.enqueue(bin_3[:])
    main_bin.enqueue(bin_4[:])
    main_bin.enqueue(bin_5[:])
    main_bin.enqueue(bin_6[:])
    main_bin.enqueue(bin_7[:])
    main_bin.enqueue(bin_8[:])
    main_bin.enqueue(bin_9[:])
    print(main_bin)
    # this is all for sorting first digit only so far

    return main_bin


print(randix(slst))
