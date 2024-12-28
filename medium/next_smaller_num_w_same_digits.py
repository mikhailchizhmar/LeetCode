def next_smaller(n):
    digits = list(str(n))  # Преобразуем число в список цифр
    length = len(digits)

    # Найти первую "возрастающую пару" с конца
    for i in range(length - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            # Найти наибольшую цифру справа от digits[i], которая меньше её
            for j in range(length - 1, i, -1):
                if digits[j] < digits[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    # Отсортировать оставшиеся цифры справа от i в порядке убывания
                    result = digits[:i + 1] + sorted(digits[i + 1:], reverse=True)
                    if result[0] == '0':
                        return -1
                    return int("".join(result))
            break

    return -1


assert next_smaller(21) == 12
assert next_smaller(907) == 790
assert next_smaller(531) == 513
assert next_smaller(2071) == 2017
assert next_smaller(414) == 144
assert next_smaller(1234567908) == 1234567890
assert next_smaller(9) == -1
assert next_smaller(111) == -1
assert next_smaller(135) == -1
assert next_smaller(1027) == -1
