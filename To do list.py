tasks=[]
def add(task):
    tasks.append(task)
    print("task added")
    
def remove(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("task not found")

def display(task):
    if not tasks:
        print("no tasks found")
    else:
        print("current tasks are:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
            
    
while True:
    print("MENU:")
    print("1.ADD TASK")
    print("2.REMOVE TASK")
    print("3.DISPLAY TASK")
    print("4.QUIT")
    
    choice=input("enter your choice:")
    
    if choice=='1':
        task=input("enter your task:")
        add(task)
    elif choice=='2':
        task=input("enter your task:")
        remove(task)
    elif choice=='3':
        display(task)
    elif choice=='4':
        print("exiting")
        break 
    else:
        print("invalid syntax please try again")