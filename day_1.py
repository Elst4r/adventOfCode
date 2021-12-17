
def task_1():
    with open("data/day_1_input.txt") as file:
        increased_amount = 0
        last_entry = int(file.readline().strip())
        for line in file:
            number = int(line.strip())
            if number > last_entry:
                increased_amount += 1
            last_entry = number

        print("Increased: ", increased_amount)


def task_2():
    numbers_list = file2list("day_1_input.txt")
    increased_amount = 0
    last_entrys = numbers_list[:3]
    last_sum = sum(last_entrys)
    for number in numbers_list[3:]:
        last_entrys.pop(0)
        last_entrys.append(number)
        new_sum = sum(last_entrys)
        if new_sum > last_sum:
            increased_amount += 1
        last_sum = new_sum

    print("Increased: ", increased_amount)


def file2list(filename):
    with open("data/" + filename) as file:
        return [int(line.strip()) for line in file]

if __name__ == '__main__':
    task_2()