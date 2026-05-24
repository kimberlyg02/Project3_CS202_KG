from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    data = heap.data[:]

    while index > 0:
        parent = (index - 1) // 2
        if data[index] < data[parent]:
            temp = data[index]

            data_1 = (
                    data[:parent]
                    + [temp]
                    + data[parent + 1:index]
                    + [data[parent]]
                    + data[index + 1:]
            )

            data = data_1
            index = parent
        else:
            break

    return MinHeap(data)


def insert(heap: MinHeap, element: Node) -> MinHeap:
    data_2 = heap.data + [element]
    heap_1 = MinHeap(data_2)

    return heapify_up(heap_1, len(data_2) - 1)


def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    data = heap.data[:]
    size = len(data)

    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < size and data[left] < data[smallest]:
            smallest = left

        if right < size and data[right] < data[smallest]:
            smallest = right

        if smallest != index:
            temp = data[index]

            data_3 = data[:]
            data_3[index] = data_3[smallest]
            data_3[smallest] = temp

            data = data_3
            index = smallest
        else:
            break

    return MinHeap(data)

def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if len(heap.data) == 0:
        raise IndexError("There are no numbers since this is an empty heap")

    root = heap.data[0]

    if len(heap.data) == 1:
        return MinHeap([]), root

    data_4 = [heap.data[-1]] + heap.data[1:-1]

    heap_2 = MinHeap(data_4)
    heap_2 = heapify_down(heap_2, 0)

    return heap_2, root

def count_frequency(s: str)-> dict[str,int]:
    frequency = {}

    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    heap = MinHeap([])

    for char in frequency:
        node = Node(frequency[char], char)
        heap = insert(heap, node)

    return heap

def build_tree(priority_queue: MinHeap) -> Node:
    heap = priority_queue

    while len(heap.data) > 1:
        heap, left = extract_min(heap)
        heap, right = extract_min(heap)

        merged = Node(
            left.freq + right.freq,
            min(left.char, right.char),
            left,
            right
        )

        heap = insert(heap, merged)

    return heap.data[0]

build_tree_from_queue = build_tree

def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}
    if node is None:
        return code

    if node.left is None and node.right is None:
        if prefix == "":
            code[node.char] = "0"
        else:
            code[node.char] = prefix

        return code

    generate_codes(node.left, prefix + "0", code)
    generate_codes(node.right, prefix + "1", code)

    return code

def encode(s: str, codes: dict)-> str:
    encoded = ""

    for char in s:
        encoded += codes[char]

    return encoded

def decode(encoded_string: str, root: Node):
    if root.left is None and root.right is None:
        return root.char * len(encoded_string)

    decoded = ""
    current = root

    for bit in encoded_string:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded += current.char
            current = root

    return decoded

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes

