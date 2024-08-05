class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None  # New variable to track the end of the list
        self.num_nodes = 0  # Initialize the size counter

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        if self.tail is None:  # If the list was empty, set the tail to the new node
            self.tail = temp
        self.num_nodes += 1  # Increment the size counter

    def size(self):
        return self.num_nodes  # Return the size counter

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not found:
            print(f"Item {item} not found in the list.")
            return
        if previous is None:
            self.head = current.get_next()
            if self.head is None:  # If the list becomes empty, update the tail
                self.tail = None
        else:
            previous.set_next(current.get_next())
            if current.get_next() is None:  # If the removed node was the tail, update the tail
                self.tail = previous
        self.num_nodes -= 1  # Decrement the size counter

    def append(self, item):
        temp = Node(item)
        if self.tail is not None:
            self.tail.set_next(temp)
        else:  # If the list was empty, set head to the new node
            self.head = temp
        self.tail = temp  # Update the tail to the new node
        self.num_nodes += 1  # Increment the size counter

    def index(self, item):
        current = self.head
        position = 0
        while current is not None:
            if current.get_data() == item:
                return position
            current = current.get_next()
            position += 1
        return -1  # This line should never be reached if we assume the item is in the list

    def insert(self, pos, item):
        if pos < 0 or pos > self.num_nodes:
            raise IndexError("Index out of bounds")
        temp = Node(item)
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
            if self.tail is None:
                self.tail = temp
        else:
            current = self.head
            previous = None
            current_position = 0
            while current_position < pos:
                previous = current
                current = current.get_next()
                current_position += 1
            temp.set_next(current)
            previous.set_next(temp)
            if temp.get_next() is None:
                self.tail = temp
        self.num_nodes += 1

    def pop(self, pos=None):
        if self.num_nodes == 0:
            raise IndexError("Pop from empty list")
        if pos is None:
            pos = self.num_nodes - 1
        if pos < 0 or pos >= self.num_nodes:
            raise IndexError("Index out of bounds")
        current = self.head
        previous = None
        current_position = 0
        while current_position < pos:
            previous = current
            current = current.get_next()
            current_position += 1
        if previous is None:
            self.head = current.get_next()
            if self.head is None:
                self.tail = None
        else:
            previous.set_next(current.get_next())
            if current.get_next() is None:
                self.tail = previous
        self.num_nodes -= 1
        return current.get_data()


# Main method to test the UnorderedList class
def main():
    my_list = UnorderedList()

    print("Is the list empty?", my_list.is_empty())  # Expected: True

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print("List size:", my_list.size())  # Expected: 6
    print("Is 93 in the list?", my_list.search(93))  # Expected: True
    print("Is 100 in the list?", my_list.search(100))  # Expected: False

    print("Index of 93:", my_list.index(93))  # Expected: 2

    my_list.insert(2, 44)
    print("List size after inserting 44 at position 2:", my_list.size())  # Expected: 7
    print("Index of 44:", my_list.index(44))  # Expected: 2

    print("Pop last item:", my_list.pop())  # Expected: 31
    print("List size after popping last item:", my_list.size())  # Expected: 6

    print("Pop item at position 2:", my_list.pop(2))  # Expected: 44
    print("List size after popping item at position 2:", my_list.size())  # Expected: 5

    my_list.remove(54)
    print("List size after removing 54:", my_list.size())  # Expected: 4

    my_list.remove(93)
    print("List size after removing 93:", my_list.size())  # Expected: 3

    my_list.remove(100)  # Expected: Item 100 not found in the list.
    print("List size after attempting to remove 100:", my_list.size())  # Expected: 3

    print("Is 93 in the list?", my_list.search(93))  # Expected: False
    print("Is the list empty?", my_list.is_empty())  # Expected: False

    my_list.append(99)
    print("List size after appending 99:", my_list.size())  # Expected: 4
    print("Is 99 in the list?", my_list.search(99))  # Expected: True


if __name__ == "__main__":
    main()
