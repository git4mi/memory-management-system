# Memory Allocation Techniques
# First Fit, Best Fit, Worst Fit

memory_blocks = []
processes = {}

def input_memory():
    global memory_blocks
    n = int(input("Enter number of memory blocks: "))
    memory_blocks = []
    for i in range(n):
        size = int(input(f"Enter size of block {i+1}: "))
        memory_blocks.append(size)

def first_fit(pid, size):
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= size:
            memory_blocks[i] -= size
            processes[pid] = size
            print(f"Process {pid} allocated using First Fit")
            return
    print("Memory not sufficient")

def best_fit(pid, size):
    best_index = -1
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= size:
            if best_index == -1 or memory_blocks[i] < memory_blocks[best_index]:
                best_index = i

    if best_index != -1:
        memory_blocks[best_index] -= size
        processes[pid] = size
        print(f"Process {pid} allocated using Best Fit")
    else:
        print("Memory not sufficient")

def worst_fit(pid, size):
    worst_index = -1
    for i in range(len(memory_blocks)):
        if memory_blocks[i] >= size:
            if worst_index == -1 or memory_blocks[i] > memory_blocks[worst_index]:
                worst_index = i

    if worst_index != -1:
        memory_blocks[worst_index] -= size
        processes[pid] = size
        print(f"Process {pid} allocated using Worst Fit")
    else:
        print("Memory not sufficient")

def deallocate():
    pid = input("Enter process ID to deallocate: ")
    if pid in processes:
        size = processes.pop(pid)
        memory_blocks.append(size)
        print(f"Process {pid} deallocated")
    else:
        print("Process not found")

def display():
    print("\nMemory Blocks:")
    for i, block in enumerate(memory_blocks):
        print(f"Block {i+1}: {block}")

    print("\nAllocated Processes:")
    if not processes:
        print("None")
    else:
        for pid, size in processes.items():
            print(f"{pid} -> {size}")

def menu():
    while True:
        print("\n--- Memory Allocation Menu ---")
        print("1. Input Memory Blocks")
        print("2. First Fit Allocation")
        print("3. Best Fit Allocation")
        print("4. Worst Fit Allocation")
        print("5. Deallocate Process")
        print("6. Display Memory Status")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            input_memory()

        elif choice in [2, 3, 4]:
            pid = input("Enter process ID: ")
            size = int(input("Enter memory required: "))

            if choice == 2:
                first_fit(pid, size)
            elif choice == 3:
                best_fit(pid, size)
            elif choice == 4:
                worst_fit(pid, size)

        elif choice == 5:
            deallocate()

        elif choice == 6:
            display()

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

menu()