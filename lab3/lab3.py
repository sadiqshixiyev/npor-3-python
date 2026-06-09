
from typing import Any, Callable, Optional, Union
from collections import namedtuple, deque

# Определение типа для базового представления дерева в виде словаря
BinaryTreeDict = dict[str, Union[int, float, Optional[dict]]]

def gen_bin_tree(
    height: int = 5,
    root: Union[int, float] = 1,
    left_leaf: Callable[[Union[int, float]], Union[int, float]] = lambda x: x * 2,
    right_leaf: Callable[[Union[int, float]], Union[int, float]] = lambda x: x + 3
) -> Optional[BinaryTreeDict]:
    """Рекурсивно строит бинарное дерево в виде вложенных словарей.

    Аргументы:
        height: Оставшаяся высота поддерева для построения (базовый случай: height <= 0).
        root: Значение текущего узла.
        left_leaf: Функция (lambda) для вычисления значения левого потомка.
        right_leaf: Функция (lambda) для вычисления значения правого потомка.

    Возвращает:
        Словарь с ключами 'value', 'left', 'right' или None, если достигнута
        максимальная высота дерева.
    """
    if height <= 0:
        return None

    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    }


# --- ИССЛЕДОВАНИЕ АЛЬТЕРНАТИВНЫХ СТРУКТУР ИЗ МОДУЛЯ COLLECTIONS ---

# Вариант 1: Использование namedtuple для неизменяемой (immutable) структуры узла
Node = namedtuple('Node', ['value', 'left', 'right'])

def gen_bin_tree_namedtuple(
    height: int,
    root: Union[int, float],
    left_leaf: Callable[[Any], Any],
    right_leaf: Callable[[Any], Any]
) -> Optional[Node]:
    """Строит бинарное дерево, используя namedtuple из модуля collections."""
    if height <= 0:
        return None
    
    return Node(
        value=root,
        left=gen_bin_tree_namedtuple(height - 1, left_leaf(root), left_leaf, right_leaf),
        right=gen_bin_tree_namedtuple(height - 1, right_leaf(root), left_leaf, right_leaf)
    )

def serialize_tree_to_deque(tree_dict: Optional[BinaryTreeDict]) -> deque:
    """Преобразует дерево из словаря в очередь deque (обход в ширину / BFS).
    
    Это демонстрирует применение deque для линейного хранения уровней дерева.
    """
    result_deque = deque()
    if not tree_dict:
        return result_deque
        
    queue = deque([tree_dict])
    while queue:
        current = queue.popleft()
        if current:
            result_deque.append(current['value'])
            queue.append(current['left'])
            queue.append(current['right'])
        else:
            result_deque.append(None) # Маркер пустого узла
            
    # Удаляем лишние None с конца для красоты
    while result_deque and result_deque[-1] is None:
        result_deque.pop()
        
    return result_deque