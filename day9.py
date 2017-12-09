def part1(line):
    stack = list()
    garbage = list()
    count = 0
    skip = False
    score = 0
    for ch in line:
        if skip:
            skip = False
        elif ch == '!':
            skip = True
        elif ch == '>':
            stack.pop()
        elif ch == '<' and '<' not in stack:
            stack.append(ch)
        elif ch == '{' and '<' not in stack:
            stack.append(ch)
        elif ch == '}' and '{' in stack and '<' not in stack:
            score += len(stack)
            stack.pop()
        elif '<' in stack:
            garbage.append(ch)

            count += 1

    print(score)
    print(len(garbage))


def main():
    line = "<!!!>>"
    fname = "E:\\DevWorld\\Python\\AdventOfCode\\2017\\resource\\day9.txt"
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
       # print(content)
    part1(content[0])
    #part1(line)

main()