import copy

def main():
    old_list = [i for i in range(10)]

    new_list1 = old_list

    new_list2 = list(old_list)

    new_list3 = old_list[:]

    print(id(old_list))
    print(id(new_list1))
    print(id(new_list2))
    print(id(new_list3))

    old_list.append([11, 12])

    print(new_list1)
    print(new_list2)
    print(new_list3)

    new_list4 = copy.copy(old_list)
    new_list5 = copy.deepcopy(old_list)

    print(new_list4)
    print(new_list5)

    # assert id(new_list4) == id(new_list5)
    # assert new_list4 == new_list5
    # assert new_list4 is new_list5

    print(id(new_list4))
    print(id(new_list5))

    old_list[10][0] = 13
    print(old_list)
    print(new_list4) # 浅拷贝，只复制了外层列表，内部的 [11, 12] 仍然是原对象的引用
    print(new_list5) # 深拷贝，深拷贝递归复制了所有嵌套对象，生成全新内存结构



if __name__ == '__main__':
    main()