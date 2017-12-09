from functools import reduce


class Tree(object):
    def __init__(self):
        self.data = None
        self.children = []
        self.weight = 0
        self.cumulative_weight = 0


def getCumulative(root):
    head = root
    if len(head.children) > 0:
        for child in head.children:
            getCumulative(child)
            head.cumulative_weight += child.cumulative_weight
        head.cumulative_weight += head.weight
    else:
        head.cumulative_weight = head.weight

    print(root.data)


def getFaultWeight(root):
    head = root
    weightMap = dict()
    if len(head.children) > 0:
        max_child = reduce(lambda x,y : x if x.cumulative_weight > y.cumulative_weight else y, head.children)
        for child in head.children:
            if child.cumulative_weight != max_child.cumulative_weight:
                diff = max_child.cumulative_weight - child.cumulative_weight
                getFaultWeight(max_child)
                print("diff - " + str(max_child.weight - diff))
                exit(0)


def main():
    fname = "E:\\DevWorld\\Python\\AdventOfCode\\2017\\resource\\day7.txt"
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        print(content)

        data = [x.split() for x in content]
        treeMap = dict()
        for val in data:
            weight = val[1][val[1].index("(") + 1:val[1].rindex(")")]
            tree = treeMap.get(val[0], Tree())
            tree.weight = int(weight)
            tree.data = val[0]
            if val[0] not in treeMap.keys():
                treeMap[val[0]] = tree
            else:
                treeMap.pop(val[0])
            if '->' in val:
                children = val[3::]
                for child in children:
                    child = child.strip(',')
                    node = treeMap.get(child, None)
                    if node is None:
                        childNode = Tree()
                        childNode.data = child
                        treeMap[child] = childNode
                        tree.children.append(childNode)
                    else:
                        tree.children.append(node)
                        treeMap.pop(child)

                print(children)

            print(weight)

        print(treeMap.keys())
        root = list(treeMap.values())[0]
        getCumulative(root)
        getFaultWeight(root)
        print(root)


main()
