from functools import reduce


def get_operator(operator, var, val):
    value = int(val)
    if operator == "inc":
        return var + (value)
    else:
        return var - (value)


def get_logic(operator, lhsStr, rhsStr):
    lhs = int(lhsStr)
    rhs = int(rhsStr)

    if operator == ">":
        return lhs > rhs
    elif operator == "<":
        return lhs < rhs
    elif operator == "==":
        return lhs == rhs
    elif operator == ">=":
        return lhs >= rhs
    elif operator == "<=":
        return lhs <= rhs
    elif operator == "!=":
        return lhs != rhs


def main():
    fname = "E:\\DevWorld\\Python\\AdventOfCode\\2017\\resource\\day8.txt"
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

        data = [x.split() for x in content]
        varMap = {}
        maxMap = {}
        for line in data:
            if get_logic(line[5], varMap.get(line[4], 0), line[6]):
                varMap[line[0]] = get_operator(line[1], varMap.get(line[0], 0), line[2])
                if maxMap.get(line[0],0) < varMap.get(line[0],0):
                    maxMap[line[0]] = varMap[line[0]]
        max = reduce(lambda x, y : x if x > y else y, varMap.values())
        max_ever = reduce(lambda x, y : x if x > y else y , maxMap.values())
        print(max)
        print("Max Ever :" + str(max_ever))


main()
