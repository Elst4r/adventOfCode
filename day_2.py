# first task fancy class based
class Submarine:
    horizontal_pos = 0
    depth = 0

    def go_forward(self, amount):
        self.horizontal_pos += amount

    def dive(self, amount):
        self.depth += amount

    def where_am_i_and_why(self):
        print(self.horizontal_pos, self.depth, self.horizontal_pos * self.depth)

    def follow_course(self, course_file):
        directions_list = _read_file(course_file)
        for axe, amount in directions_list:
            if axe == "horizontal":
                self.go_forward(amount)
            elif axe == "depth":
                self.dive(amount)

def _read_file(file_name):
    with open("data/" + file_name) as file:
        directions_list = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file]

    def _replace(direction, amount):
        if direction == "down":
            return "depth", amount
        elif direction == "up":
            return "depth", -amount
        else:
            return "horizontal", amount
    # replace up and down with positive or negative value for depth
    directions_list = [_replace(direction, amount) for direction, amount in directions_list]
    return directions_list

# second task minimal work
def task2():
    with open("data/day_2.txt") as file:
        directions_list = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file]
    aim = 0
    depth = 0
    horizontal = 0
    for axe, amount in directions_list:
        if axe == "up":
            aim -= amount
        elif axe == "down":
            aim += amount
        else:
            horizontal += amount
            depth += aim * amount
    print(horizontal * depth)


if __name__ == '__main__':
    task2()
    # yellowSubmarine = Submarine()
    # yellowSubmarine.follow_course("day_2.txt")
    # yellowSubmarine.where_am_i_and_why()