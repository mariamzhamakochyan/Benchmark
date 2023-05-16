import time
import random
import numpy as np

def delete_vector(vector, element):
    start_time = time.time()
    vector = np.delete(vector, np.where(vector == element))
    end_time = time.time()
    return end_time - start_time

def insert_vector(vector, index, element):
    start_time = time.time()
    vector = np.insert(vector, index, element)
    end_time = time.time()
    return end_time - start_time
    
def delete_list(col, element):
    start_time = time.time()
    if element in vector:
        col.remove(element)
    end_time = time.time()
    return end_time - start_time

def insert_list(col, index, element):
    start_time = time.time()
    col.insert(index, element)
    end_time = time.time()
    return end_time - start_time
    
n = int(input("How many elements do you want to generate? "))
random_elements1 = np.random.randint(1, 100, size=n)
random_elements2 = [random.randint(1,100) for _ in range(n)]

vector = random_elements1.copy()
lst = random_elements2.copy()

delete_time_vector = delete_vector(vector, 3)
insert_time_vector = insert_vector(vector, 2, 10)

delete_time_list = delete_list(lst, 3)
insert_time_list = insert_list(lst, 2, 10)

print("Delation from vector: {:.6f} seconds".format(delete_time_vector))
print("Insert in vector: {:.6f} seconds".format(insert_time_vector))
print("Delation from list: {:.6f} seconds".format(delete_time_list))
print("Insert in list: {:.6f} seconds".format(insert_time_list))
