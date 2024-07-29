class Hash_table:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        for pair in self.hash_table[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash_table[hash_key].append([key, value])

    def delete(self, key):
        hash_key = self._hash_function(key)
        for i, pair in enumerate(self.hash_table[hash_key]):
            if pair[0] == key:
                del self.hash_table[hash_key][i]
                return

    def search(self, key):
        hash_key = self._hash_function(key)
        for pair in self.hash_table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None


hash_table = Hash_table(10)

hash_table.insert(3, "Valary")
hash_table.insert(10, "Aileen")
hash_table.insert(11, "Arya")
hash_table.insert(12, "Jay")
hash_table.insert(13, "Iscah")
hash_table.insert(14, "Njambi")
hash_table.insert(15, "Gatweri")

print(hash_table.search(10))  

print(hash_table.search(20))

# Removing a key and its value
#Use the delete method followed by the key you'd like to delete.
hash_table.delete(10)

print(hash_table.search(10)) 



#Binary search tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


if __name__ == "__main__":

    digits = None
    
    
    digits = insert(digits, 50)
    digits = insert(digits, 30)
    digits = insert(digits, 20)
    digits =insert(digits, 40)
    digits= insert(digits, 70)
    digits = insert(digits, 60)
    digits = insert(digits, 80)
    
    
    print("Found:", search(digits, 70).val)
    print("Found:", search(digits, 60).val)

