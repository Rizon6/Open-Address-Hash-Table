# This hash table uses open addressing and horners method as the hash function
def main():
    my_table = HashTable(3)
    my_table.insert("Rizon", 26)
    my_table.insert("Brooke", 1)
    my_table.insert("Sam", 15)
    print(my_table.search("Brooke"))
    print(my_table.search("Rizon"))


class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def horner_hash(self, key, base=31, mod=None):
        if mod is None:
            mod = self.size # so you can set the mod in the parameter, defaults to size of table
        hash_value = 0

        for char in key: # loop thru each character in string
            hash_value = (hash_value * base + ord(char)) % mod # each character adds some amount to hash value
        return hash_value
    
    def insert(self, key, value):
        index = self.horner_hash(key)
        initial_index = index

        while self.table[index] is not None:
            index = (index + 1) % self.size  # Linear probing to find next available slot
            if index == initial_index: # index looped around to original (table is full)
                raise ValueError("Hash table is full")

        self.table[index] = (key, value)
        return("insert succesful")
    
    def search(self, key):
        index = self.horner_hash(key)
        initial_index = index

        while True:
            if self.table[index][0] == key:
                return self.table[index][1]  # Return value if key is same

            index = (index + 1) % self.size  # Move to next slot, stay in bounds of table

            if index == initial_index:
                break  # Exit loop if we've come full circle
        return None
main()
