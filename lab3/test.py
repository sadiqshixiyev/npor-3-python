"""Модуль тестирования функции построения бинарного дерева."""

import unittest
from lab3 import gen_bin_tree, gen_bin_tree_namedtuple, serialize_tree_to_deque

class TestBinaryTreeGeneration(unittest.TestCase):
    """Набор тестов для проверки генерации дерева и альтернативных структур."""

    def test_base_case_zero_height(self):
        """Проверка, что при высоте <= 0 возвращается None."""
        self.assertIsNone(gen_bin_tree(height=0, root=1))
        self.assertIsNone(gen_bin_tree(height=-1, root=5))

    def test_tree_height_one(self):
        """Проверка дерева из одного корневого узла."""
        expected = {"value": 10, "left": None, "right": None}
        self.assertEqual(gen_bin_tree(height=1, root=10), expected)

    def test_variant_1_logic(self):
        """Проверка математической логики Варианта 1 на высоте 2.
        
        Правила: left = x * 2, right = x + 3. При кодировании root=1:
        left должен быть 2, right должен быть 4.
        """
        tree = gen_bin_tree(height=2, root=1, left_leaf=lambda x: x * 2, right_leaf=lambda x: x + 3)
        
        self.assertEqual(tree["value"], 1)
        self.assertEqual(tree["left"]["value"], 2)
        self.assertEqual(tree["right"]["value"], 4)
        self.assertIsNone(tree["left"]["left"])

    def test_namedtuple_structure(self):
        """Проверка работы альтернативной структуры на namedtuple."""
        tree = gen_bin_tree_namedtuple(height=2, root=1, left_leaf=lambda x: x*2, right_leaf=lambda x: x+3)
        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.left.value, 2)
        self.assertIsNone(tree.left.left)

    def test_deque_serialization(self):
        """Проверка плоской сериализации структуры через collections.deque."""
        tree = gen_bin_tree(height=2, root=1, left_leaf=lambda x: x*2, right_leaf=lambda x: x+3)
        flat_queue = serialize_tree_to_deque(tree)
        # Ожидаем в очереди: корень(1), левый(2), правый(4)
        self.assertEqual(list(flat_queue), [1, 2, 4])

# ИСПРАВЛЕНО: Строго __main__, чтобы тесты запускались при вызове файла
if __name__ == "__main__":
    unittest.main()