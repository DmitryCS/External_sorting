# External_sorting

   Задание: 
   
   Отсортировать массив размера N методом слияния отрезков. Используйте P файлов для хранения отрезков. M - максимальное количество элементов в оперативной памяти. Для внутренней сортировки использовать метод сортировки слиянием.
    
   
   Принцип работы программы: 
   
   
   
   создается файл mainfile.txt, в который записываются N рандомных элементов типа int в диапазоне 1-5000(изменяем). Кроме того, создается P дополнительных файлов, первые два из которых будут буферными. Считываются по M элементов из главного файла и сортируются, результат записывается в последние P-2 файла. Затем среди P-1 файлов находится минимальный элемент, и он записывается в один из буферных файлов.Это повторяется, пока в этот буферный файл не запишутся все элементы из P-1 файлов. То есть происходит слиение файлов в один. В дальнейшем происходит тоже самое, за исключением того, что слияние файлов произойдет в другой буферный файл. Таким образом, итоговый отсортированный файл будет одним из двух буферных файлов. После сортировки файлы P-2 удаляются. Остаются главный файл и два буферных, в одном из которых находится итоговый вариант отсортированных элементов. Кроме того, выведется время работы программы. 
   
   
   
   Особенности реализации: возможность простого изменения параметров M, P, N вначале кода программы
    
    MAX_RAM_NUMBERS = 24              #Максимальное количество элементов M в оперативной памяти(кол-во элементов при внутренней сортировке)
    MAX_WORK_FILES = 8                #Количество файлов P для хранения отрезков 
    MAX_NUMBER_OF_ELEMENTS = 36000    #Количество элементов N в главном файле.
