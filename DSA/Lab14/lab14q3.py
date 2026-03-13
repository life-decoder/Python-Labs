"""Implement the Huffman coding algorithm.

Given a set of characters and their frequencies, this module generates a binary prefix-free
code for each character. It includes a simple encoder/decoder and a few test cases.

Algorithm:
- Build a min-heap (priority queue) of leaf nodes (character + frequency).
- Repeatedly merge the two nodes with smallest frequencies into a new internal node.
- Traverse the built tree to assign binary codes (0/1) to each character.

References:
- https://en.wikipedia.org/wiki/Huffman_coding
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass
from itertools import count
from typing import Dict, Optional, Tuple


@dataclass(frozen=True)
class _Node:
    """Node used internally for building the Huffman coding tree."""

    freq: int
    char: Optional[str] = None
    left: Optional[_Node] = None
    right: Optional[_Node] = None


def huffman_codes(freq_map: Dict[str, int]) -> Dict[str, str]:
    """Return a dict mapping each symbol to its Huffman binary code.

    Args:
        freq_map: Mapping of symbol -> frequency (must be positive integers).

    Returns:
        Mapping of symbol -> prefix-free binary string.
    """

    if not freq_map:
        return {}

    # Validate input
    for sym, f in freq_map.items():
        if not isinstance(f, int) or f < 0:
            raise ValueError(f"Frequency must be a non-negative int: {sym} -> {f}")

    # Use a counter to ensure heap elements are comparable when frequencies tie
    counter = count()
    heap: list[Tuple[int, int, _Node]] = []

    for ch, f in freq_map.items():
        node = _Node(freq=f, char=ch)
        heapq.heappush(heap, (f, next(counter), node))

    # Edge case: only one symbol
    if len(heap) == 1:
        _, _, single = heap[0]
        return {single.char: "0"}

    # Build Huffman tree
    while len(heap) > 1:
        f1, _, n1 = heapq.heappop(heap)
        f2, _, n2 = heapq.heappop(heap)
        merged = _Node(freq=f1 + f2, left=n1, right=n2)
        heapq.heappush(heap, (merged.freq, next(counter), merged))

    root = heap[0][2]

    codes: Dict[str, str] = {}

    def _build_codes(node: _Node, prefix: str) -> None:
        if node.char is not None:
            # Leaf node
            codes[node.char] = prefix or "0"
            return
        assert node.left and node.right, "Internal node must have two children"
        _build_codes(node.left, prefix + "0")
        _build_codes(node.right, prefix + "1")

    _build_codes(root, "")
    return codes


def encode(text: str, codes: Dict[str, str]) -> str:
    """Encode a string using the provided Huffman codes."""

    return "".join(codes[ch] for ch in text)


def decode(bits: str, codes: Dict[str, str]) -> str:
    """Decode a bitstring using the provided Huffman codes."""

    # Build reverse lookup
    rev = {v: k for k, v in codes.items()}

    decoded_chars: list[str] = []
    buffer = ""

    for b in bits:
        buffer += b
        if buffer in rev:
            decoded_chars.append(rev[buffer])
            buffer = ""

    if buffer:
        raise ValueError("Bitstring does not align to a valid Huffman code")

    return "".join(decoded_chars)


def huffman_statistics(freq_map: Dict[str, int], codes: Dict[str, str]) -> Tuple[Dict[str, int], Dict[str, int], float]:
    """Compute per-symbol path lengths, weighted lengths, and average bits.

    Returns:
        Tuple of (path_lengths, weighted_lengths, avg_bits).

    - path_lengths: symbol -> code length (path length)
    - weighted_lengths: symbol -> frequency * path length
    - avg_bits: weighted average bits per symbol
    """

    total_weight = sum(freq_map.values())
    if total_weight <= 0:
        return {}, {}, 0.0

    path_lengths: Dict[str, int] = {}
    weighted_lengths: Dict[str, int] = {}

    for sym, freq in freq_map.items():
        code = codes.get(sym, "")
        length = len(code)
        path_lengths[sym] = length
        weighted_lengths[sym] = freq * length

    avg_bits = sum(weighted_lengths.values()) / total_weight
    return path_lengths, weighted_lengths, avg_bits


def print_huffman_statistics(freq_map: Dict[str, int], codes: Dict[str, str]) -> None:
    """Prints the path length, weighted path length, and average bits for each symbol."""

    path_lengths, weighted_lengths, avg_bits = huffman_statistics(freq_map, codes)

    print("Symbol | Freq | Path Len | Weighted Len")
    print("------ | ---- | -------- | ------------")
    for sym in sorted(freq_map):
        print(
            f"{sym!r:>6} | {freq_map[sym]:>4} | {path_lengths.get(sym, 0):>8} | {weighted_lengths.get(sym, 0):>12}"
        )
    print(f"\nAverage bits per symbol: {avg_bits:.4f}\n")


def _run_tests() -> None:
    """Basic sanity tests for the Huffman module."""

    # Example from standard Huffman coding discussion
    freqs = {"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}
    codes = huffman_codes(freqs)

    # Display path lengths and averages for the sample distribution
    print("Huffman statistics for example frequency map:")
    print_huffman_statistics(freqs, codes)

    # All characters must have a code and codes must be prefix-free
    assert set(codes.keys()) == set(freqs.keys())
    for c1, code1 in codes.items():
        for c2, code2 in codes.items():
            if c1 != c2:
                assert not code1.startswith(code2), f"{code1} is prefix of {code2}"

    # Encode / decode roundtrip
    text = "abcdef"
    bitstring = encode(text, codes)
    assert decode(bitstring, codes) == text

    # Single character edge case
    single = {"x": 100}
    single_codes = huffman_codes(single)
    assert single_codes == {"x": "0"}
    assert encode("xxxx", single_codes) == "0000"
    assert decode("0000", single_codes) == "xxxx"

    print("All tests passed.")


if __name__ == "__main__":
    _run_tests()
