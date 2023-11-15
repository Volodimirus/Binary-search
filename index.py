"""Для правильной работы алгоритма, его элементы должны находиться в порядке возрастания"""
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digits_len = len(digits)

first_index = 0
last_index = len(digits) - 1
guess_number = 5

guess_number_index = 0
tries = 1


if guess_number <= digits_len:
    while first_index <= last_index:
        mid_index = round((first_index + last_index) / 2)
        mid_element = digits[mid_index]

        if guess_number < mid_element:
            last_index = digits.index(mid_element) - 1
        elif guess_number > mid_element:
            first_index = digits.index(mid_element) + 1
        else:
            guess_number_index = mid_index
            break

        tries += 1
else:
    print("Заданное число не находится в списке")

print(f"Заданное число {guess_number} находится на позиции {guess_number_index}")
print(f'Количество итераций {tries}')