from task_one import BinarySearchTree as BST, AVLTree as AVL


class BST_MIN(BST):
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key


class AVL_MIN(AVL):
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key


def main():
    # Приклад використання
    bst = BST_MIN()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print("Найменше значення у дереві:", bst.find_min())

    avl = AVL_MIN()
    avl.insert(50)
    avl.insert(30)
    avl.insert(20)
    avl.insert(40)
    avl.insert(70)
    avl.insert(60)
    avl.insert(80)
    print("Найменше значення у AVL-дереві:", avl.find_min())


if __name__ == "__main__":
    main()
