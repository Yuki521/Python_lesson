from pprint import pprint


def sort(data):
    pprint(len(data))
    for i in range(len(data)):
        for j in range(i - 1, -1, -1):
            pprint(j)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            else:
                break


data = [4, 1, 7, 3, 5, 4, 5, 6, 2, 8]
sort(data)
print(data)
