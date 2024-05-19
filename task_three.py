from task_one import BinarySearchTree as BST, AVLTree as AVL


class BST_SUM(BST):
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.key + self._sum_values(node.left) + self._sum_values(node.right)


class AVL_SUM(AVL):
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.key + self._sum_values(node.left) + self._sum_values(node.right)


def main():
    # Приклад використання
    bst = BST_SUM()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print("Сума всіх значень у дереві:", bst.sum_values())

    avl = AVL_SUM()
    avl.insert(50)
    avl.insert(30)
    avl.insert(20)
    avl.insert(40)
    avl.insert(70)
    avl.insert(60)
    avl.insert(80)
    print("Сума всіх значень у AVL-дереві:", avl.sum_values())


if __name__ == "__main__":
    main()
