"""
Определите максимальную длину цепочки вида XYZXYZXYZ, ласт фрагмент может быть неполным.
"""

def main():
    file = open('24_demo_7.txt', 'r')
    sequence = file.readline() # Весь текст в файле записан в первой же огромной строке. Прочитаем только одну строку

    max_length = 0

    capacity = 333334 # (10^6+1) / 3 = 333.333, прибавляем один на всякий случай
    # Именно 333.333 - максимально количество 'XYZ' в файле, если файл будет весь состоять из последовательности.
    # Шанс этого весьма мал, поэтому искомая последовательность будет значительно меньше этого числа

    for i in range(1, capacity+1): # 'XYZ' умножаем на i, считаем кол-во XYZ / XYZX / XYZXY
        XYZ = sequence.count('XYZ'*i)
        XYZX = sequence.count('XYZ'*i+'X')
        XYZXY = sequence.count('XYZ'*i+'XY')

        if XYZ == 0: # Если XYZ*i == 0, то дальше не существует XYZ+X / XYZ+XY / XYZ * (i+1) и  так далее,
            print(max_length)                           # макс последовательность найдена
            break

        if XYZ != 0 and i * 3 > max_length: # Считаем макс длину последовательности из 'XYZ'*i
            max_length = i * 3

        if XYZX != 0 and i * 3 + 1 > max_length: # Считаем макс длину последовательности из 'XYZ'*i + 'X'
            max_length = i * 3 + 1

        if XYZXY != 0 and i * 3 + 2 < max_length: # Считаем макс длину последовательности из 'XYZ'*i + 'XY'
            max_length = i * 3 + 2


if __name__ == "__main__":
    main()
