from time import time
MAX_RAM_NUMBERS = 24
MAX_WORK_FILES = 8
MAX_NUMBER_OF_ELEMENTS = 36000

def read_part(file):
    numbers = []
    for _ in range(MAX_RAM_NUMBERS):
        number = file.readline()
        if number == '':
            break
        numbers.append(int(number))
    return numbers

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def sort_part(part, temp_filename):
    mergeSort(part)
    with open(temp_filename, 'w') as temp_file:
        # temp_file.write('\n'.join(list(map(str, part))))
        for i in range(len(part)):
            temp_file.write('%d\n' % part[i])


def merge_files(temp_filenames, buf_filename):
    with open(buf_filename, 'w') as buf_file:
        open_temp_files=[]
        min_elements_of_files=[]
        for i in range(len(temp_filenames)):
            open_temp_files.append(open(temp_filenames[i]))
            min_elements_of_files.append(open_temp_files[i].readline().strip())
        check = True
        index = None
        while check:
            min = 100000
            check = False
            for k in range(len(temp_filenames)):
                if min_elements_of_files[k] == '':
                    continue
                elif int(min_elements_of_files[k]) <= min:
                    index = k
                    min = int(min_elements_of_files[k])
                    check = True
            if check:
                buf_file.write('%s\n' % min_elements_of_files[index])
                min_elements_of_files[index] = open_temp_files[index].readline().strip()


def main():
    t = time()
    buf_files = ['temp1.txt', 'temp2.txt']
    open(buf_files[0], 'w').close()
    temp_files = ['temp{}.txt'.format(i) for i in range(3, MAX_WORK_FILES + 1)]
    with open('mainfile.txt', 'w') as mainfile:
        from random import randint
        for i in range(MAX_NUMBER_OF_ELEMENTS):
            mainfile.write('%d\n' % randint(1, 5000))
    with open('mainfile.txt') as mainfile:
        parts_count = 0
        buf_file_index = 0
        while True:
            part = read_part(mainfile)
            if len(part) == 0:
                break
            sort_part(part, temp_files[parts_count])
            parts_count += 1
            if parts_count == MAX_WORK_FILES - 2:
                merge_files(temp_files + [buf_files[buf_file_index]], buf_files[1 - buf_file_index])
                buf_file_index = 1 - buf_file_index
                parts_count = 0
        if parts_count:
            merge_files(temp_files[:parts_count] + [buf_files[buf_file_index]], buf_files[1 - buf_file_index])
    import os
    for i in range(3, MAX_WORK_FILES + 1):
        os.remove(('temp{}.txt'.format(i)))        #удаление лишних файлов после окончания работы программы
    print(time() - t)


if __name__ == '__main__':
    main()























"""

    read_part(file):
        numbers = []
        for _ in range(MAX_NUMBERS):
            number = file.read()
            if number == '':
                break
            numbers.append(number)
        return numbers

    Main:
        buf_files = ['temp1.txt', 'temp2.txt']
        temp_files = ['temp{}.txt'.format(i) for i in range(3, TEMP_FILES_COUNT+1)]
        with open('mainfile') as mainfile:
            temp_file_index = 2
            parts_count = 0
            buf_file_index = 0
            while True:
                part = read_part(mainfile)
                if len(part) == 0:
                    break
                sort_part(part, temp_file_index)
                temp_file_index += 1
                parts_count += 1
                if parts_count == TEMP_FILES_COUNT - 2:
                    merge_files(temp_files + buf_files[buf_file_index], buf_files[1 - buf_file_index])
                    buf_file_index = 1-buf_file_index
                    parts_count = 0
            if parts_count:
                merge_files(temp_files + buf_files[buf_file_index], buf_files[1 - buf_file_index])



"""