class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0
        self.deleted = object()  # A unique marker for deleted slots

    def put(self, key, data):
        # Resize the table if the load factor exceeds 0.66 (Lowered from 0.75)
        if self.count / self.size > 0.66:
            self.resize()

        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None or self.slots[hash_value] is self.deleted:
            self.slots[hash_value] = key
            self.data[hash_value] = data
            self.count += 1
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while (self.slots[next_slot] is not None and
                       self.slots[next_slot] != key and
                       self.slots[next_slot] is not self.deleted):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None or self.slots[next_slot] is self.deleted:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                    self.count += 1
                else:
                    self.data[next_slot] = data

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                data = self.data[position]
                break
            position = self.rehash(position, len(self.slots))
            if position == start_slot:
                break

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        return self.count

    def __contains__(self, key):
        return self.get(key) is not None

    def __delitem__(self, key):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == key:
            self.slots[hash_value] = self.deleted
            self.data[hash_value] = None
            self.count -= 1
        else:
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] is not None:
                if self.slots[next_slot] == key:
                    self.slots[next_slot] = self.deleted
                    self.data[next_slot] = None
                    self.count -= 1
                    break
                next_slot = self.rehash(next_slot, len(self.slots))
                if next_slot == hash_value:
                    break

    def resize(self):
        new_size = self.get_next_prime(2 * self.size)
        new_slots = [None] * new_size
        new_data = [None] * new_size

        # Reinsert all existing items into the new table
        for key, data in zip(self.slots, self.data):
            if key is not None and key is not self.deleted:
                new_hash_value = key % new_size
                if new_slots[new_hash_value] is None:
                    new_slots[new_hash_value] = key
                    new_data[new_hash_value] = data
                else:
                    next_slot = (new_hash_value + 1) % new_size
                    while new_slots[next_slot] is not None:
                        next_slot = (next_slot + 1) % new_size
                    new_slots[next_slot] = key
                    new_data[next_slot] = data

        self.size = new_size
        self.slots = new_slots
        self.data = new_data

    def get_next_prime(self, n):
        """Returns the first prime number greater than n."""

        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime = n
        while True:
            prime += 1
            if is_prime(prime):
                return prime


def test_hash_table():
    # Create a new hash table
    h = HashTable()

    # Test inserting new keys
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"

    # Test retrieving existing keys
    assert h[54] == "cat", f"Expected 'cat', got {h[54]}"
    assert h[26] == "dog", f"Expected 'dog', got {h[26]}"
    assert h[93] == "lion", f"Expected 'lion', got {h[93]}"
    assert h[17] == "tiger", f"Expected 'tiger', got {h[17]}"
    assert h[77] == "bird", f"Expected 'bird', got {h[77]}"
    assert h[31] == "cow", f"Expected 'cow', got {h[31]}"
    assert h[44] == "goat", f"Expected 'goat', got {h[44]}"
    assert h[55] == "pig", f"Expected 'pig', got {h[55]}"
    assert h[20] == "chicken", f"Expected 'chicken', got {h[20]}"

    # Test updating existing keys
    h[20] = "duck"
    assert h[20] == "duck", f"Expected 'duck', got {h[20]}"

    # Test collision handling
    h[32] = "giraffe"  # 32 % 11 == 32
    h[43] = "elephant"  # 43 % 11 == 43

    assert h[32] == "giraffe", f"Expected 'giraffe', got {h[32]}"
    assert h[43] == "elephant", f"Expected 'elephant', got {h[43]}"

    print("All tests passed.")


def test_hash_table_len_contains():
    h = HashTable()

    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"

    # Test __len__
    assert len(h) == 3, f"Expected length 3, got {len(h)}"

    # Test __contains__
    assert 54 in h, "Expected key 54 to be in the hash table"
    assert 99 not in h, "Expected key 99 to not be in the hash table"

    print("len and contains tests passed.")


def test_hash_table_del():
    h = HashTable()

    h[22] = "cat"
    h[33] = "dog"
    h[44] = "lion"

    assert h[22] == "cat", f"Expected 'cat', got {h[22]}"
    assert h[33] == "dog", f"Expected 'dog', got {h[33]}"
    assert h[44] == "lion", f"Expected 'lion', got {h[44]}"

    del h[33]
    assert 33 not in h, "Expected key 33 to be deleted"
    assert h[44] == "lion", f"Expected 'lion', got {h[44]}"

    print("del method test passed.")


def test_hash_table_resize():
    h = HashTable()

    # Adding enough items to exceed the load factor and trigger a resize
    for i in range(9):
        h[i] = f"value{i}"

    assert len(h) == 9, f"Expected 9, got {len(h)}"
    assert h.size > 11, f"Expected resized table, got size {h.size}"

    for i in range(9):
        assert h[i] == f"value{i}", f"Expected 'value{i}', got {h[i]}"

    print("Resize test passed.")


# Run the test
def main():
    test_hash_table()
    test_hash_table_len_contains()
    test_hash_table_del()
    test_hash_table_resize()


if __name__ == "__main__":
    main()