#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index


        """
        hash() is a built-in method in python that returns the hash value
        of an object. Hash values are integers.
        """
        # hash the key given
        # modules by the len of stored buckets
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n) iterates through all buckets """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys




    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n) iterates through all buckets
        """
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket


        all_values = [] # list with all values stored
        for bucket in self.buckets: # iterates all buckets
            for key, value in bucket.items(): # iterates all keys and values of each bucket
                all_values.append(value) # store all methods in all_values list
        return all_values # return the list with all values stored


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket


        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket


        count_buckets = 0 #

        for bucket in self.buckets:
            count_buckets += bucket.length()
        return count_buckets



    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        key_index = self._bucket_index(key)
        bucket = self.buckets[key_index]
        found_item = bucket.find(lambda key_value: key_value[0] == key)
        key_in_bucket = False

        if found_item is not None:
            key_in_bucket = True
            return key_in_bucket
        else:
            return key_in_bucket


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?
        O(l)
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        key_index = self._bucket_index(key)
        bucket = self.buckets[key_index]
        found_item = bucket.find(lambda key_value: key_value[0] == key)

        if found_item is not None:
            return found_item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))




    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions? best case -> O(1)
        otherwise O(l)"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        key_index = self._bucket_index(key)
        bucket = self.buckets[key_index]
        found_item = bucket.find(lambda key_value: key_value[0] == key)

        if found_item is not None:
            bucket.delete(found_item)

        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(l)"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        key_index = self._bucket_index(key) # locates what index where key belongs
        bucket = self.buckets[key_index] # gets the key value pair
        found_item = bucket.find(lambda item: item[0] == key)

        if found_item is not None:
            bucket.delete(found_item)
        else:
            raise KeyError('Key not found: {}'.format(key))



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
