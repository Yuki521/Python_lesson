def search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


data = [4, 1, 7, 3, 5, 4, 5, 6, 8]
target = 7
print("要素番号{}にデータ{}を見つけました。".format(search(data, target), target))
