import unittest
from proj3 import *

class TestStudent(unittest.TestCase):

    def test_frequency_1(self):
        self.assertEqual(
            count_frequency("therefore"),
            {'e': 3, 'f': 1, 'h': 1, 'o': 1, 'r': 2, 't': 1}
        )

    def test_count_frequency_2(self):
        self.assertEqual(
            count_frequency(""),
            {}
            )

    def test_count_frequency_3(self):
        self.assertEqual(
            count_frequency("BANNANA"),
            {'A': 3, 'B': 1, 'N': 3}
            )

    def test_insert_1(self):
        heap = MinHeap([])
        heap = insert(heap, Node(2, 'c'))

        self.assertEqual(heap.data[0].freq, 2)

    def test_insert_2(self):
        heap = MinHeap([])
        heap = insert(heap, Node(1, 'v'))
        heap = insert(heap, Node(2, 'o'))

        self.assertEqual(heap.data[0].freq, 1)

    def test_insert_3(self):
        heap = MinHeap([])
        heap = insert(heap, Node(10, 'd'))
        heap = insert(heap, Node(4, 'g'))
        heap = insert(heap, Node(8, 'p'))

        self.assertEqual(heap.data[0].freq, 4)

    def test_heapify_up_1(self):
        heap = MinHeap([
            Node(6, 'e'),
            Node(3, 'h'),
            Node(1, 'u')
        ])

        heap = heapify_up(heap, 2)

        self.assertEqual(heap.data[0].freq, 1)

    def test_heapify_up_2(self):
        heap = MinHeap([
            Node(2, 'x'),
            Node(4, 'y'),
            Node(5, 'z')
        ])

        heap = heapify_up(heap, 2)

        self.assertEqual(heap.data[0].freq, 2)

    def test_heapify_up_3(self):
        heap = MinHeap([
            Node(6, 't'),
            Node(7, 'w'),
            Node(8, 'y'),
            Node(9, 'z')
        ])

        heap = heapify_up(heap, 3)

        self.assertEqual(heap.data[0].freq, 6)

    def test_heapify_down_1(self):
        heap = MinHeap([
            Node(1, 'd'),
            Node(2, 'e'),
            Node(3, 'f')
        ])

        heap = heapify_down(heap, 0)
        self.assertEqual(heap.data[0].freq, 1)

    def test_heapify_down_2(self):
        heap = MinHeap([
            Node(3, 'n'),
            Node(5, 'p'),
            Node(6, 's')
        ])

        heap = heapify_down(heap, 0)
        self.assertEqual(heap.data[0].freq, 3)

    def test_heapify_down_3(self):
        heap = MinHeap([
            Node(4, 'f'),
            Node(7, 'h'),
            Node(8, 'j'),
            Node(10, 'k')
        ])

        heap = heapify_down(heap, 0)
        self.assertEqual(heap.data[0].freq, 4)

    def test_extract_min_1(self):
        heap = MinHeap([])
        heap = insert(heap, Node(9, 'd'))
        heap = insert(heap, Node(3, 'l'))

        heap, node = extract_min(heap)

        self.assertEqual(node.freq, 3)

    def test_extract_min_2(self):
        heap = MinHeap([])
        heap = insert(heap, Node(4, 'h'))
        heap = insert(heap, Node(8, 'p'))
        heap = insert(heap, Node(1, 'q'))

        heap, node = extract_min(heap)

        self.assertEqual(node.freq, 1)

    def test_extract_min_3(self):
        heap = MinHeap([])
        heap = insert(heap, Node(4, 'k'))

        heap, node = extract_min(heap)

        self.assertEqual(node.freq, 4)
        self.assertEqual(heap.data, [])

    def test_create_priority_queue_1(self):
        freq = {'c': 5, 'n': 3}
        heap = create_priority_queue(freq)
        self.assertEqual(heap.data[0].freq, 3)

    def test_create_priority_queue_2(self):
        freq = {}
        heap = create_priority_queue(freq)
        self.assertEqual(heap.data, [])

    def test_create_priority_queue_3(self):
        freq = {'x': 8}
        heap = create_priority_queue(freq)
        self.assertEqual(heap.data[0].char, 'x')

    def test_build_tree_1(self):
        freq = {'a': 7, 's': 8}

        heap = create_priority_queue(freq)
        root = build_tree(heap)

        self.assertEqual(root.freq, 15)

    def test_build_tree_2(self):
        freq = {'c': 4, 'r': 5, 'v': 9}

        heap = create_priority_queue(freq)
        root = build_tree(heap)

        self.assertEqual(root.freq, 18)

    def test_build_tree_3(self):
        freq = {'x': 7}

        heap = create_priority_queue(freq)
        root = build_tree(heap)

        self.assertEqual(root.char, 'x')

    def test_generate_codes_1(self):
        encoded, decoded, codes = huffman_encoding("HELLO")
        self.assertEqual(set(codes.keys()), {'E', 'H', 'L', 'O'})
        self.assertEqual(set(codes.values()), {'0', '110', '10', '111'})

    def test_generate_codes_2(self):
        encoded, decoded, codes = huffman_encoding("FGH")
        self.assertEqual(len(codes), 3)

    def test_generate_codes_3(self):
        encoded, decoded, codes = huffman_encoding("nnnn")
        self.assertEqual(list(codes.keys()), ['n'])
        self.assertIn(codes['n'], ['0', ''])

    def test_encode_1(self):
        codes = {'P': '0', 'O': '1'}

        self.assertEqual(
         encode("PPOO", codes),
          "0011"
        )

    def test_encode_2(self):
        codes = {'h': '0', 'i': '1', 'o': '2'}

        self.assertEqual(
         encode("hio", codes),
          "012"
        )
    def test_encode_3(self):
        codes = {'w': '1'}

        self.assertEqual(
            encode("www", codes),
            "111"
        )

    def test_decode_1(self):
        encoded, decoded, codes = huffman_encoding("heyyyooo")

        self.assertEqual(decoded, "heyyyooo")

    def test_decode_2(self):
        encoded, decoded, codes = huffman_encoding("bcd")

        self.assertEqual(decoded, "bcd")

    def test_decode_3(self):
        encoded, decoded, codes = huffman_encoding("KLM")

        self.assertEqual(decoded, "KLM")

    def test_huffman_encoding_1(self):
        encoded, decoded, codes = huffman_encoding("grabbing")

        self.assertEqual(decoded, "grabbing")

    def test_huffman_encoding_2(self):
        encoded, decoded, codes = huffman_encoding("SSTT")

        self.assertEqual(encoded, "0011")

    def test_huffman_encoding_3(self):
        encoded, decoded, codes = huffman_encoding("XYZ")

        self.assertEqual(decoded, "XYZ")


