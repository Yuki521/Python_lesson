from pprint import pprint


def sort(data):
    for i in range(len(data) - 1, 0, -1):  # 後ろから比較
        for j in range(i):  # 未整列の部分を比較
            if data[j] > data[j + 1]:  # 隣り合う要素で前の方が大きい場合
                data[j], data[j + 1] = data[j + 1], data[j]  # 要素を入れ替える


data = [4, 1, 7, 3, 5, 4, 5, 6, 2, 8]
sort(data)
print(data)
