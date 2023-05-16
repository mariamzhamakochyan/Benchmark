import time
import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_element(self, element):
        start_time = time.time()
        if self.head is None:
            return
        if self.head.data == element:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current is not None and current.data != element:
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
        end_time = time.time()
        return end_time - start_time

    def insert_element(self, index, element):
        start_time = time.time()
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current is not None and count < index:
                prev = current
                current = current.next
                count += 1
            if current is None:
                return
            prev.next = new_node
            new_node.next = current
        end_time = time.time()
        return end_time - start_time


def delete_vector(col, element):
    start_time = time.time()
    if element in col:
        col.remove(element)
    end_time = time.time()
    return end_time - start_time


def insert_vector(col, index, element):
    start_time = time.time()
    col.insert(index, element)
    end_time = time.time()
    return end_time - start_time


n = int(input("How many elements do you want to generate? "))
random_elements = [random.randint(1, 100) for _ in range(n)]

lst = random_elements.copy()
delete_time_vector = delete_vector(lst, 2)
insert_time_vector = insert_vector(lst, 3, 10)

print("Deletion from vector: {:.6f} seconds".format(delete_time_vector))
print("Insertion in vector: {:.6f} seconds".format(insert_time_vector))

linked_list = LinkedList()
for element in random_elements:
    linked_list.append(element)

delete_time_llist = linked_list.delete_element(2)
insert_time_llist = linked_list.insert_element(3, 10)

print("Deletion from linked list: {:.6f} seconds".format(delete_time_llist))
print("Insertion in linked list: {:.6f} seconds".format(insert_time_llist))
