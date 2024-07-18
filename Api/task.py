from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

def majority(input):
    n = len(input)
    m = n // 2 + 1
    new_dict = {}
    for i in range(n):
        if input[i] in new_dict:
            new_dict[input[i]] += 1
        else:
            new_dict[input[i]] = 1

    for i, j in new_dict.items():
        if j >= m:
            return i
    return None

class InputModel(BaseModel):
    numbers: List[int]

@app.get("/majority/{num}")
def get_majority(num: str):
    result = majority(num)
    if result is None:
        raise HTTPException(status_code=404, detail="No majority element found")
    return {"majority_element": result}

@app.post("/majority")
def post_majority(input_model: InputModel):
    result = majority(input_model.numbers)
    if result is None:
        raise HTTPException(status_code=404, detail="No majority element found")
    return {"majority_element": result}



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def linkedlist(self, input):
        for value in input:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                cur = self.head
            else:
                cur.next = new_node
                cur = cur.next

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result

@app.get("/linkedlist")
async def get_list(input: str):
    input_data = [int(i) for i in input.split(",")]
    
    descending_input = sorted(input_data, reverse=True)
    linked_list_desc = LinkedList()
    linked_list_desc.linkedlist(descending_input)
    
    ascending_input = sorted(input_data)
    linked_list_asc = LinkedList()
    linked_list_asc.linkedlist(ascending_input)
    
    return {"descending_linkedlist": linked_list_desc.to_list(), "ascending_linkedlist": linked_list_asc.to_list()}

class InputModel(BaseModel):
    input: List[int]

@app.post("/linkedlist")
async def post_list(input_model: InputModel):
    input_data = input_model.input

    descending_input = sorted(input_data, reverse=True)
    linked_list_desc = LinkedList()
    linked_list_desc.linkedlist(descending_input)

    ascending_input = sorted(input_data)
    linked_list_asc = LinkedList()
    linked_list_asc.linkedlist(ascending_input)
    
    return {
        "descending_linkedlist": linked_list_desc.to_list(),
        "ascending_linkedlist": linked_list_asc.to_list()
    }