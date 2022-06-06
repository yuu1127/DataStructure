# Written by Yuta

from linked_list import *
from trie import *

# sample for Linked_list

LinkedList(range(4)).print()
len(LinkedList((0, 1)))
LinkedList([0, 1, 2, 3]).is_sorted()
LinkedList([0, 2, 1, 3]).is_sorted()

L = LinkedList(range(4))
L.reverse()
L.print()

# sample for Trie

trie = Trie()
for word in ['he', 'hers', 'has', 'heir', 'one']: trie.add_word(word)
print(trie.has_been_recorded('he'))
print(trie.has_been_recorded('height'))
