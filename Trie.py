class Node:
    """
    Every node element contains one character, a dictionary of children and a isTerminal
    flag value signifying if the Node character is a terminal character for a word
    """
    def __init__(self,character = None, isTerminal : bool = False) -> None:
      self.character = character
      self.children = {}
      self.isTerminal = isTerminal

class Trie:
    def __init__(self) -> None:
        self.root = Node('')
    
    def insert(self,word:str) -> None:
        """
        to insert a word into a trie we will use this method
        """
        curr = self.root
        for char in word:
            
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
      
        curr.isTerminal=True
    
    def __contains__(self,word:str) -> bool:
       
        curr = self.root
        for char in word:
           
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isTerminal
    
    def getPrefixes(self,word) -> list:
      
        prefix = ''
        prefixes = []
        curr = self.root
        for char in word:
            if char not in curr.children:
                return prefixes
            curr = curr.children[char]
            prefix += char
            if curr.isTerminal:
                prefixes.append(prefix)
        return prefixes