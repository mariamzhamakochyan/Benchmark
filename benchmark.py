import time
import random

def delete(col, element):
    start_time = time.time()
    if element in vector:
        vector.remove(element)
    end_time = time.time()
    return end_time - start_time

def insert(col, index, element):
    start_time = time.time()
    col.insert(index, element)
    end_time = time.time()
    return end_time - start_time
    
n = int(input("How many elements do you want to generate? "))
random_elements = [random.randint(1,100) for _ in range(n)]

vector = random_elements.copy()
lst = random_elements.copy()

delete_time_vector = delete(vector, 3)
insert_time_vector = insert(vector, 2, 10)

delete_time_list = delete(lst, 3)
insert_time_list = insert(lst, 2, 10)

print("Delation from vector: {:.6f} seconds".format(delete_time_vector))
print("Insert in vector: {:.6f} seconds".format(insert_time_vector))
print("Delation from list: {:.6f} seconds".format(delete_time_list))
print("Insert in list: {:.6f} seconds".format(insert_time_list))

