from functools import reduce


def debugger(line):
    max_num = reduce(lambda x, y: x if x > y else y, line)
    index = line.index(max_num)
    length = len(line)
    count = index
    line[count] = 0
    count += 1
    while max_num > 0:
        if count == length:
            count = 0
        line[count] += 1
        max_num -= 1
        count += 1

    print(line)
    return line


def part1(lines):
    instructions = set()

    lines = debugger(lines)
    count = 1
    while tuple(lines) not in instructions:
        instructions.add(tuple(lines))
        lines = debugger(lines)
        count += 1

    print(count)


def part2(lines):
    instructions = dict()

    lines = debugger(lines)
    count = 1
    while tuple(lines) not in instructions.keys():
        instructions[tuple(lines)] = count
        lines = debugger(lines)
        count += 1

    print(count)
    print(lines)
    print(count - instructions[tuple(lines)])


def main():
    input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
    lines = [int(i) for i in input.split()]
    #lines = [0,2,7,0]
    part2(lines)


main()
