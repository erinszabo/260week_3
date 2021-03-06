import random


class Queue:  # a line, obviously
    def __init__(self, title):
        self.items = []
        self.title = title

    def name(self):
        return self.title

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # someone entering the line must pass every person in line O(n)
        self.items.insert(0, item)

    def dequeue(self):  # the first person in line just steps forward O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def contents(self):  # not subscriptable, need a different way to return all elements in Queue
        return self.items


slst = random.sample(range(100, 1000), 15)


# print(slst)


# print(int("321"[len("321") - 1]))     ones place
# print(int("321"[len("321") - 2]))     tens place
# print(int("321"[len("321") - 3]))     hundreds place


def randix(lst):
    main_bin = Queue("main_bin")
    place = 0
    count = 0
    ordered = False
    ones_done = False
    tens_done = False
    hunds_done = False

    for i in lst:
        main_bin.enqueue(i)
    print(f"main_bin start = {main_bin.contents()}")
    bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9 \
        = Queue("bin_0"), Queue("bin_1"), Queue("bin_2"), Queue("bin_3"), Queue("bin_4"), \
        Queue("bin_5"), Queue("bin_6"), Queue("bin_7"), Queue("bin_8"), Queue("bin_9")
    small_bins = [bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9]

    while ordered is not True:
        num = main_bin.dequeue()
        # print(f"num = {num}")
        num_s = str(num)
        # print(f"num_s = {num_s}")
        ones_place = int(num_s[len(num_s) - 1])
        # print(ones_place)
        tens_place = int(num_s[len(num_s) - 2])
        # print(tens_place)
        hunds_place = int(num_s[len(num_s) - 3])
        # print(hunds_place)

        """
        if ones_done is False:
            place = ones_place
        elif tens_done is False:
            place = tens_place
        elif hunds_done is False:
            place = hunds_place
        else:
            ordered is True
        """

        if count == 1:  # move on to the next place for all nums
            place = tens_place
            ones_done = True
        elif count == 10:
            place = hunds_place
            tens_done = True
        elif count == 100:
            hunds_done = True
            ordered = True

        if place == 0:
            bin_0.enqueue(num)
        elif place == 1:
            bin_1.enqueue(num)
        elif place == 2:
            bin_2.enqueue(num)
        elif place == 3:
            bin_3.enqueue(num)
        elif place == 4:
            bin_4.enqueue(num)
        elif place == 5:
            bin_5.enqueue(num)
        elif place == 6:
            bin_6.enqueue(num)
        elif place == 7:
            bin_7.enqueue(num)
        elif place == 8:
            bin_8.enqueue(num)
        else:
            bin_9.enqueue(num)
            # ^^ I did all this before realizing I should make a small_bins list ^^
        print(main_bin.contents())
        print(bin_0.contents(), bin_1.contents(), bin_2.contents(), bin_3.contents(), bin_4.contents(),
              bin_5.contents(), bin_6.contents(), bin_7.contents(), bin_8.contents(), bin_9.contents())
        # realizing I should have made a bin class with a value characteristic, but oh well next time

        if main_bin.size() <= 0:  # dump small bins into main_bin
            for i in small_bins:
                for j in i.contents():
                    main_bin.enqueue(j)

        for i in small_bins:  # empty each small bin
            while i.size() > 0:
                i.dequeue()
            print(f"{i.name()} contains: {i.contents()}")

        count = count * 10
        if count == 0:
            count = 1
        print(f"{count}'s done; main_bin contents: {main_bin.contents()}")
        print("")

    return f"main_bin contents: {main_bin.contents()}"


print(randix(slst))
