number_one = input('Введите числа через пробел: ')
polzovatel_numbers = int(input('Введите число: '))


def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


if ' ' not in number_one:
    print("\n При вводе отсутствуют пробелы")
    number_one = input('Введите числа через пробел: ')
if not is_int(number_one):
    print('\n В строке не содержится чисел')
    print(error)
else:
    number_one = number_one.split()

list_number_one = [int(item) for item in number_one]

def merge_sort(A):
    if len(A) < 2:
        return A[:]
    else:
        middle = len(A) // 2
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_number_one = merge_sort(list_number_one)

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

print(f'Упорядоченный по возрастанию список: {list_number_one}')

if not binary_search(list_number_one, polzovatel_numbers, 0, len(list_number_one)):
    rI = min(list_number_one, key=lambda x: (abs(x - polzovatel_numbers), x))
    ind = list_number_one.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < polzovatel_numbers:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_number_one[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_number_one.index(rI)}
В списке нет меньшего элемента''')
    elif rI > polzovatel_numbers:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_number_one.index(rI)}
Ближайший меньший элемент: {list_number_one[min_ind]} его индекс: {min_ind}''')
    elif list_number_one.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_number_one.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_number_one, polzovatel_numbers, 0, len(list_number_one))}')



