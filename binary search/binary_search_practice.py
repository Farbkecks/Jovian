"""
Problem:
Es gibt einen Input list aus int. Diese waren in einer aufsteigenden sortierten Liste. 
Die aufgabe ist es raus zufinden wie oft ich die Liste Rotieren musste um die aktuelle Liste zu bekommen.
Rotieren heißt hier das letzte Elemtnt nach vorne verschieben.

Input:
[int, int,...]
[5, 6, 9, 0, 2, 3, 4]
Output:
3

Solution:
Brute Force 1 :
1. liste Sortieren gucken ob sie sich ändert wenn nein diese zurückgeben
2. letztes Elemtnt nach vorne, counter +1

Brute Force 2 :
1. durch die liste durchgehn index finden wenn die gegebene zahl größer als die Zahl rechts von ihr ist.

Optimize:
1. Variable lo auf 0, Varibale hi auf lenge der Liste, last_numbber auf letze zahl setzen
2. mid durch lo und hi addieren und durch 2 rechen
3. mid_nummber durch nums mit index mid bekommen
4. wenn mid_number kleiner als linker nachber ist mid_nummber zurückgeben
5. Wenn mid_nummber kleiner als letzte zahl:
    hi auf mid -1 setzen
6. Wenn mid_number größer als letzte zahl:
    lo auf mid + 1 setzen
"""


# def count_rotations(nums: list) -> int:
#     index = 0
#     if len(nums) == 0:
#         return -1
#     while index < len(nums) - 1 and len(nums) > 1:
#         if nums[index] > nums[index + 1]:
#             return index + 1
#         index += 1
#     return 0


# # Kopiert von Jovian
# def binary_search(lo, hi, condition):
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = condition(mid)
#         if result == "found":
#             return mid
#         elif result == "left":
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return -1


# def count_rotations(nums: list) -> int:
#     if len(nums) == 1:
#         return 0

#     def condition(mid):
#         last_numbber = nums[-1]
#         if nums[mid - 1] > nums[mid]:
#             return "found"
#         if nums[mid] < last_numbber:
#             return "left"
#         if nums[mid] > last_numbber:
#             return "right"

#     return binary_search(0, len(nums) - 1, condition)


def count_rotations(nums: list) -> int:
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    lo, hi = 0, len(nums)
    last_numbber = nums[-1]
    while True:
        mid = (lo + hi) // 2
        mid_nummber = nums[mid]
        if mid_nummber < nums[mid - 1]:
            return mid
        if mid_nummber < last_numbber:
            hi = mid - 1
        if mid_nummber > last_numbber:
            lo = mid + 1


tests = []
tests.append({"input": {"nums": [6, 1, 2, 3, 4, 5]}, "output": 1})
tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3, 4]}, "output": 3})
tests.append({"input": {"nums": [0, 2, 3, 4]}, "output": 0})
tests.append({"input": {"nums": [20, 24, 25, 30, 1]}, "output": 4})
tests.append({"input": {"nums": []}, "output": -1})
tests.append({"input": {"nums": [5, 6, 7, 2, 3, 4]}, "output": 3})
tests.append({"input": {"nums": [5, 6, 7, -1, 2, 3, 4]}, "output": 3})
tests.append({"input": {"nums": [1]}, "output": 0})
tests.append(
    {"input": {"nums": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]}, "output": 6}
)


test_count = 1
for test in tests:
    print(f"Test {test_count}: ", end="")
    test_count += 1
    output = count_rotations(**test["input"])
    print(f" output: {output} ", end="")
    print(output == test["output"])
