import time
import random


class liste:
    def __init__(self, list) -> None:
        self.list = list
        self.quicksort()

    def quicksort(self, start=0, end=None):
        def partion(start, end):
            l, r = start, end - 1
            while r > l:
                if self.list[l] <= self.list[end]:
                    l += 1
                elif self.list[r] > self.list[end]:
                    r -= 1
                    pass
                else:
                    self.list[l], self.list[r] = self.list[r], self.list[l]
            assert l == r
            if self.list[r] > self.list[end]:
                self.list[l], self.list[end] = self.list[end], self.list[l]
                return r
            return end

        if len(self.list) in [0, 1]:
            return

        if end == None:
            end = len(self.list) - 1
        if start < end:
            pivot = partion(start, end)
            self.quicksort(start, pivot - 1)
            self.quicksort(pivot + 1, end)

    def show(self):
        print(self.list)


if __name__ == "__main__":
    tests = []
    tests.append({"input": {"nums": [1, 2, 3, 4, 5, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append({"input": {"nums": []}, "output": []})
    tests.append({"input": {"nums": [1]}, "output": [1]})
    tests.append({"input": {"nums": [3, 1, 2, 5, 4, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append(
        {"input": {"nums": [3, -1, -2, 5, 1, 4, 6]}, "output": [-2, -1, 1, 3, 4, 5, 6]}
    )
    tests.append(
        {
            "input": {"nums": [8, 0, 1, 7, 4, 13, 6, 12, 9, 3, 10, 5, 11, 2, 14]},
            "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        }
    )
    tests.append(
        {"input": {"nums": [3, 1, 2, 5, 4, 4, 6]}, "output": [1, 2, 3, 4, 4, 5, 6]}
    )
    tests.append(
        {
            "input": {"nums": [2, 13, 10, 0, 7, 14, 4, 9, 6, 3, 12, 11, 8, 1, 5]},
            "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        }
    )

    x = 100000
    list1 = list(range(x))
    list2 = list(range(x))
    random.shuffle(list2)
    tests.append({"input": {"nums": list2}, "output": list1})
    pass
    for test in tests:
        start_time = time.time()
        x = liste(test["input"]["nums"])
        output = x.list
        print(output == test["output"], end="")
        # print(f" output: {output}", end="")
        print(f" dauer: {time.time()-start_time}")
