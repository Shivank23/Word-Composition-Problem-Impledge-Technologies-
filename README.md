# Word-Composition-Problem-Impledge-Technologies-
There are many ways to store and search strings inside text, like binary search trees or hash tables. I decided on using a trie data structure, which is an ordered tree data structure where strings that share a common stem or prefix hang off a common node. Tries insert and find strings in O(m) time, where m is the length of the string.

HERE ARE THE STEPS I TOOK....
1)Add each word to a trie data structure 

2) For each word, find the first prefix that exists in the trie if there is one. Then look at the suffix and see if it has a prefix. Continue to call that recursively. When the prefix and the suffix both exist in the trie, then that is a concatenated word.

3)Keep a counter and increment it each time a concatenated word is found.

4)Since the words are sorted by length, return the first two concatenated words found and those are the two longest concatenated words.
