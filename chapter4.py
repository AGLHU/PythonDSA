# Exercise 4.1
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([1, 3, 5, 10, -3]))

# Exercise 4.2
def countItems(list):
    if list == []:
        return 0
    return 1 + countItems(list[1:])

print(countItems([1, 2, 3, 4, 5]))

# Exercise 4.3
def findMax(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(findMax([1, 100, 50, 69, -100]))
