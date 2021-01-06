import heapq
from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик
from collections import namedtuple

parent = namedtuple("Node", ["left", "right"])
leaf = namedtuple("Leaf", ["char"])

class Node(parent):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(leaf):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


class Huffman:
    def __init__(self):
        self.code = {}

    def encode(self, s):
        h = []
        for ch, freq in Counter(s).items():
            h.append((freq, len(h), Leaf(ch)))
        heapq.heapify(h) 
        count = len(h)
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
            count += 1

        if h: 
            [(_freq, _count, root)] = h
            root.walk(self.code, "")
        return self.code


if __name__ == "__main__":
    coder = Huffman()
    seq = open('/Users/pnovoselov/Desktop/Algorithms/potter_text.txt', encoding='utf-8').readline()
    code = coder.encode(seq.lower())
    encoded = "".join(code[ch] for ch in seq.lower())
    print('Сжатие:', len(seq) * 8 / len(encoded))
