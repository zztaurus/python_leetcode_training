
class Solution(object):

    def isValidSerialization(self, preorder):
        """
        在二叉树中，所有节点的入度之和等于出度之和
        """

        # 一条指向根节点的虚拟边
        edge = 1
        for node in preorder.split(","):
            # 任何时候，边数都不能小于 0
            if node == "#":
                # 空指针消耗一条空闲边
                edge -= 1
                if edge < 0:
                    return False
            else:
                # 非空节点消耗一条空闲边，增加两条空闲边
                edge -= 1
                if edge < 0:
                    return False
                edge += 2
        # 最后不应该存在空闲边
        return edge == 0


    def isValidSerialization1(self, preorder):
        """

        二叉树的结构特性
        节点和边的关系:
        在一棵二叉树中，如果有 n 个节点，那么就有  n−1 条边（每个节点除了根节点外都有一个父节点）。
        每个非空节点（非叶子节点）会增加两个子节点的可能性（即两个新的槽位），而每个空节点（叶子节点）则不增加新的槽位。

        2. 槽位的概念:
            槽位可以被视为树中可以放置节点的位置。
            初始时，根节点需要一个槽位。
            每当一个节点被放置时，它会消耗一个槽位。

        前序遍历的性质
            在前序遍历中，节点的访问顺序是：根节点 -> 左子树 -> 右子树。
            对于序列化的字符串：非空节点（如数字）：消耗一个槽位。增加两个新的槽位（因为它有两个子节点）。空节点（#）：只消耗一个槽位，不增加新的槽位。

        1. 初始化槽位:
            1. 开始时，只有一个槽位用于放置根节点。

        2. 遍历序列化字符串:
            1. 每访问一个节点，消耗一个槽位。

            2. 如果节点是非空的，增加两个新的槽位。

            3. 如果槽位在任何时候变为负数，说明序列化无效，因为这意味着有节点没有足够的槽位来放置。

        3. 最终检查:
            遍历结束后，槽位应为零，表示所有节点都正确匹配，没有多余的槽位或未使用的槽位。

        4.槽位思路的优势

            简单性: 通过维护一个简单的计数器来跟踪槽位，避免了显式构建树的复杂性。
            效率: 只需一次遍历即可完成验证，时间复杂度为

        """

        slots = 1
        nodes = preorder.split(',')

        for node in nodes:
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2

        return slots == 0

    def isValidSerialization2(self, preorder):

        """
        反序列化
        """
        pass

    def deserialize(self, nodes):

        if not nodes:
            return True





