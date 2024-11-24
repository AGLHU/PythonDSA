# HashTable code from BeAPython tutorial video
# Video Link: https://youtu.be/iBaTns9S4zc
 
import hashlib
 
class HashTable(object):
    def __init__(self, size=10):        
        self.num_elements = 0
        self.data = [0] * size
        self.size = len(self.data)
        print(self.data)
 
    def __resize(self):
        pass
 
    def __get_hash_index(self, key):
        key_str = str(key)
        our_hash = int(hashlib.md5(key_str.encode()).hexdigest(), 16)        
        return our_hash % self.size
 
    def insert(self, key, value):
        """
        This method inserts data into our hash table
 
        Returns none
 
        Args:
          key(str): The key to insert
          value(tuple): Tuple of customer data 
        """
        hash_data = (key, value)
        hash_index = self.__get_hash_index(key)
        self.data[hash_index] = hash_data
        self.num_elements += 1
        # TODO: If num_elements == self.size * 2 then resize
 
    def get(self, key):
        """Get data by a key"""
        hash_index = self.__get_hash_index(key)
        data = self.data[hash_index]
        data_key = data[0]
        if key != data_key or data == 0:
            raise KeyError("Hash key does not exist")
 
        return data[1]
 
    def remove(self, key):
        hash_index = self.__get_hash_index(key)
        data = self.data[hash_index]
        data_key = data[0]
        if key != data_key or data == 0:
            raise KeyError("Hash key does not exist")
 
        self.data[hash_index] = 0
        self.num_elements -= 1
 
    def key_contains(self, substring):
        """
        Look through all the keys and return data as a list
        that partial matches the substring
        """
        pass
 
our_data = ("johnsmith123@gmail.com", "John", "Smith", 1000)
our_hash_table = HashTable()
our_hash_table.insert(our_data[0], our_data)
print("== Insert data ==")
print(our_hash_table.data)
print(our_hash_table.num_elements)
print("==Get data==")
print(our_hash_table.get(our_data[0]))
print("== Remove data==")
our_hash_table.remove(our_data[0])
print(our_hash_table.data)