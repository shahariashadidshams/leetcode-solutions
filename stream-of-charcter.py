class TrieNode:
  def __init__(self):
    self.children: dict[str, "TrieNode"] = {}
    self.isWord = False

class StreamChecker:
  def __init__(self, words: list[str]):
    self.root = TrieNode()
    self.letters = []
    for word in words:
      self._insert(word)

  def query(self, letter: str) -> bool:
    self.letters.append(letter)
    node = self.root
    for c in reversed(self.letters):
      if c not in node.children:
        return False
      node = node.children[c]
      if node.isWord:
        return True
    return False

  def _insert(self, word: str) -> None:
    node = self.root
    for c in reversed(word):
      node = node.children.setdefault(c, TrieNode())
    node.isWord = True

def stream_test():
    words = ["abc", "xyz"]
    sc = StreamChecker(words)
    stream = "axxyz"
    expected = [False, False, False, False, True]  # last 'z' matches "xyz"
    out = [sc.query(c) for c in stream]
    assert out == expected
    print("StreamChecker simple test passed")

stream_test()


"""
Stream of Characters:
Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string from a given array of strings words.

For example:
If words = ["abc", "xyz"] and the stream added the four characters a, x, y, z, the algorithm should detect that the suffix "xyz" matches a word in words.

Implement the StreamChecker class:
StreamChecker(String[] words) → Initializes the object with the array words.
boolean query(char letter) → Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.
"""