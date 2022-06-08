while True:
    try:
        some_list = list(map(int, input("Укажите произвольный набор чисел через пробел\n").split(" ")))
    except Exception:
         print("Ошибка, неверный ввод чисел")
    else:
        break
while True:
    try:
        some_namber = list(map(int, input(F"Введите число от {min(list(some_list))} до {max(list(some_list))}: ").split(" ")))
        if min(list(some_namber)) < min(list(some_list)) or min(list(some_namber)) > max(list(some_list)):
            raise ValueError
    except ValueError:
        print(f"Нужно ввести число от {min(list(some_list))} до {max(list(some_list))}!")
    else:
        break
array, num = list(map(int, some_list)), list(map(int, some_namber))
array.extend(num)
print(array)
def sortArray(array):
    for i in range(1, len(array)):
        x = array[i]
        p = i
        while p > 0 and array[p - 1] > x:
            array[p] = array[p - 1]
            p -= 1
        array[p] = x
    return array
sortA = sortArray(array)
print(sortA)
def double_search(sortA, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if element == sortA[middle]:
        return middle
    elif element < sortA[middle]:
        return double_search(sortA, element, left, middle - 1)
    else:
        return double_search(sortA, element, middle + 1, right)
element = min(some_namber)
idx = double_search(sortA, element, 0, len(sortA))
if element == max(sortA):
    Pidx = idx
elif element == min(sortA):
    Pidx = "введённое число минимальное"
else:
    Pidx = idx - 1
if element == max(sortA):
    Pidz = "введённое число максимальное"
elif element == min(sortA):
    Pidz = idx
else:
    Pidz = idx + 1
print(F"Последний индекс в списке: {len(sortA)-1}")
print(F"индекс предыдущего числа перед{element} :", Pidx)
print(F"индекс следующего числа после{element} :", Pidz)
