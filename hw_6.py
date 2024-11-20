def bubble_sort(unsorted_list):
    num = len(unsorted_list)
    for i in range(num - 1):
         for j in range(num - i - 1):
             if unsorted_list[j] > unsorted_list[j + 1]:
                 unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


def binary_search(Val, sorted_list):
    N = len(sorted_list)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1
    while First <= Last:
        Middle = (First + Last) // 2
        if Val == sorted_list[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            Pos = Middle
            break
        elif Val > sorted_list[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk == True:
        print('Элемент найден', Pos)
    else:
        print('Элемент не найден')
    return Pos

unsorted_list = [14, 26, 13, 37, 28, 45, 52, 11, 92]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
Val = 11
position = binary_search(Val, sorted_list)