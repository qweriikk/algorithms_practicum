from collections import Counter
import heapq

def huffman_encode(text):
    freq = Counter(text)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    huffman_tree = heap[0][1:]
    codes = {char: code for char, code in huffman_tree}
    encoded_text = ''.join(codes[char] for char in text)

    print(len(codes), len(encoded_text))
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)

if __name__ == "__main__":
    huffman_encode("Errare humanum est.")

