class Queue:
    
    # Uses a list to create the Queue
    def __init__(self, lista) -> None:
        self.queue = lista
    
    # Removes from the Queue the first value that match the type with the user input
    # and returns the name of the removed one
    def dequeue(self, aprt_type):
        assert aprt_type == "one" or aprt_type == "two", "Wrong apartment type"
        for j, k in enumerate(self.queue):
            if k["type"] == aprt_type or k["type"] == "both":
                return self.queue.pop(j)["name"] 


    def __repr__(self) -> str:
        return f"{self.queue}"


dic_list = [
    {"name": "Jessie", "type": "one"},
    {"name": "Herbert", "type": "both"},
    {"name": "Sam", "type": "one"},
    {"name": "John", "type": "two"},
    {"name": "Peter", "type": "two"},
    {"name": "Michael", "type": "both"},
    {"name": "Noah", "type": "both"},
    {"name": "Ron", "type": "one"}
]

new_queue = Queue(dic_list)
user_input = None

while True:
    print("The queue is: ", "\n")
    print(new_queue)
    user_input = input("Please enter the apartment type: ")
    
    if user_input == "exit":
        break
    
    try:
        print(f"{new_queue.dequeue(user_input)} has been removed from the list", "\n")
    except AssertionError:
        print("Wrong input value, apartment type must be <one> or <two>")