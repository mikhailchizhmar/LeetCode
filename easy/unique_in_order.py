# Реализуйте функцию unique_in_order, которая принимает в качестве аргумента
# последовательность и возвращает список элементов без каких-либо элементов
# с одинаковым значением рядом друг с другом и с сохранением исходного порядка элементов.

def unique_in_order(arr):
    temp_char = None
    ans = []
    for c in arr:
        if c != temp_char:
            temp_char = c
            ans.append(temp_char)
    return ans


assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
assert unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]
