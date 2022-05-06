def inputData():# считывание входных данных из файла
    branch = []
    with open('input.txt', 'r', encoding = 'utf8') as file:
        count = int(file.readline())
        for i in range(count):
            data = list(map(int, file.readline().split()))
            branch.append(data)
    return branch, count

def search(branch, count):  # проверка на сбалансированность дерева
    result = []
    lengthAnd = {}
    length = list(reversed(range(len(branch))))
    for i in length:    # перебор по элементам из массива (их номера)
        if branch[i][1] == 0 and branch[i][2] == 0: #если элемент лист
            lenBranch = 1 # высота
            agreement = 0 #балансировка
            lengthAnd[i+1] = (lenBranch, agreement) # запись в словарь для использования
            result.append(0)    # запись балансировки как конечный результат дял этого элемента
        else:   # проверка следующих элементов
            if branch[i][1] == 0:
                hight1 = 0
            else:
                element1 = lengthAnd[branch[i][1]]
                hight1 = element1[0]    #высота
            if branch[i][2] == 0:
                hight2 = 0
            else:
                element2 = lengthAnd[branch[i][2]]
                hight2 = element2[0]

            agreement = hight2 - hight1 #вычисление балансировки
            lenBranch = max(hight1, hight2) + 1 # высота текущего узла
            result.append(agreement) # запись результата текущего элемента
            lengthAnd[i+1] = (lenBranch, agreement) # запись в словарь для использования
    return reversed(result)

def printResult(result): #вывод в файл конечного результата
    with open('output.txt', 'w', encoding = 'utf8') as file:
        file.write('\n'.join(list(map(str, result))))

def main():
    branch, count = inputData()
    result = search(branch, count)
    printResult(result)


if __name__ == '__main__':
    main()