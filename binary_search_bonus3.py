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
"""


def find_element(nums: list, target: int) -> int:
    index = 0
    while index < len(nums):
        if nums[index] == target:
            return index
        index += 1
    return -1


if __name__ == "__main__":
    tests = []
    tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3, 4], "target": 2}, "output": 4})
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
