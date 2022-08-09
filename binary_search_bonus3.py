"""
Input:
[5,6,9,0,2,3,4], 2
Output:
5

Problem description:
eine Sortierte Liste wo N oft die letzte Zahl nach vorne verschoben wurde
man bekommt eine target number
Mann soll den Index zurückgeben an der die Target number ist
es sind nur einzigartige Zahlen in der Liste

Brute force:
varibale inedex erstellen
solange index kleiner als die länge der liste ist:
    gucken ob die aktuelle zahl das target ist wenn ja zurückgeben
    wenn nicht index plus 1
-1 zurückgeben

Optimize:
Varibale mid, lo, hi, last_numbber erstellen (int)
Varibale revers_rechts, reverse_links erstellen (boolen)

--

mid durschnitt aus lo und hi

akutell = zahl von nums mit index mid 

wenn aktuell gleich target return mid

Wenn Target kleiner als last_numbber und Aktuell größer als last_number: reverse_links auf True
Wenn Target größer als last_number und Aktuell kleiner als last_number: reverse_rechts auf True

wenn target > aktuell dann rechts
gucken ob revers rechts

wenn target < aktuell dann links
gucken ob revers links

wenn links: hi = mid -1
wenn rechts: lo = mid +1

beide revers auf false

ab Strich wiederholen

"""

from enum import Enum, auto


class Direction(Enum):
    none = auto()
    right = auto()
    left = auto()


# def find_element(nums: list, target: int) -> int:
#     index = 0
#     while index < len(nums):
#         if nums[index] == target:
#             return index
#         index += 1
#     return -1


def find_element(nums: list, target: int) -> int:
    if len(nums) == 0:
        return -1
    lo = 0
    hi = len(nums) - 1
    last_nummber = nums[-1]

    while True:
        direction = Direction.none
        revers_left = False
        revers_right = False
        mid = (lo + hi) // 2
        nummber = nums[mid]
        if nummber == target:
            return mid
        if target <= last_nummber and nummber > last_nummber:
            revers_left = True
        if target > last_nummber and nummber < last_nummber:
            revers_right = True
        if target > nummber:
            direction = Direction.right
        if target < nummber:
            direction = Direction.left

        if revers_right and direction == Direction.right:
            direction = Direction.left
        if revers_left and direction == Direction.left:
            direction = Direction.right

        if direction == Direction.left:
            hi = mid - 1
        if direction == Direction.right:
            lo = mid + 1


if __name__ == "__main__":
    tests = []
    tests.append({"input": {"nums": [5, 0, 2, 3, 4], "target": 5}, "output": 0})
    tests.append(
        {
            "input": {"nums": [5, 6, 9, 12, 123, 534, 0, 1, 2, 3, 4], "target": 2},
            "output": 8,
        }
    )
    tests.append(
        {
            "input": {
                "nums": [5, 6, 7, 8, 9, 13, 20, 25, 27, 38, 100, 0, 2, 3, 4],
                "target": 2,
            },
            "output": 12,
        }
    )
    tests.append({"input": {"nums": [], "target": 2}, "output": -1})
    tests.append({"input": {"nums": [2], "target": 2}, "output": 0})
    tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3], "target": 5}, "output": 0})
    tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3], "target": 3}, "output": 5})

    test_count = 1
    for test in tests:
        output = find_element(**test["input"])
        resulte = output == test["output"]
        print(f"{test_count} output: {output} {resulte}")
        test_count += 1
