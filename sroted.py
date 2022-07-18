month_name = [(1, 'January'), (2, 'February'), (3, 'March')]
print(sorted(month_name, key=lambda x: x[1]))
# [(2, 'February'), (1, 'January'), (3, 'March')]

fruits_list = [(1, 'Papaya', 100), (2, 'Kiwi', 50), (3, 'Orange', 15)]
print(sorted(fruits_list, key=lambda x: str(x[2])))
# [(1, 'Papaya', 100), (3, 'Orange', 15), (2, 'Kiwi', 50)]
