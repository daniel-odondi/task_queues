#Queues are data structure used to effect the first come first served procedure
# A simple task queue in Python using Python's built-in queue module.

from queue import Queue

# create a task queue
task_queue = Queue()
# Add tasks
task_queue.put("Send confirmation email")
task_queue.put("Generate invoice")
task_queue.put("Update inventory")

# process tasks
while not task_queue.empty():
    task = task_queue.get()
    print(f"Processing {task}")
    task_queue.task_done()
