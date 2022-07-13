def binary_search(list=[], target=None):
    first = 0
    last = len(list) - 1
    loops = 0
    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return print("target found in index ", midpoint)
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
        loops += 1
    return print(target, " not in list!\n", "loop amount ", loops)
data = []
for i in range(1, 10000001):
    data.append(i)
binary_search(data, 100000002)
