
# 501  二叉搜索树中的众数

"""

给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 任意顺序 返回。

假定 BST 满足如下定义：

结点左子树中所含节点的值 小于等于 当前节点的值
结点右子树中所含节点的值 大于等于 当前节点的值

左子树和右子树都是二叉搜索树

"""


def findMode1(root):
    """
    方法一: 使用哈希表存储来统计众数
    """

    answer = {}
    def dfs(node):

        if node is None:
            return
        dfs(node.left)
        x = root.val
        if x in answer:
            answer[x] += 1
        else:
            answer[x] = 1
        dfs(node.right)

    dfs(root)
    return find_most_frequent_key(answer)


def find_most_frequent_key(hash_table):
    # Initialize variables to track the most frequent key and its count
    most_frequent_keys = []
    max_count = 0

    # Iterate over the hash table
    for key, count in hash_table.items():
        if count > max_count:
            # Found a new maximum count, renew the list and update max_count
            most_frequent_keys = [key]
            max_count = count
        elif count == max_count:
            # If the current count equals max_count, add the key to the list
            most_frequent_keys.append(key)

    return most_frequent_keys















