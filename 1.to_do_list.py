def add_task(tasks):
    task = input("task ko add karo")
    tasks.append(task)
    print(f"task '{task}' add hogya")

def view_task(tasks):
    if not tasks:
        print("koye task nai hai")
    else:
        print("\nAppkai task")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_complete(tasks):
    view_task(tasks)  # Pehle tasks dikhao taaki user choose kar sake
    if tasks:
        try:
            index = int(input("Kaunsa task complete hua? (Number dalo): ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] = tasks[index] + " [Done]"
                print("Task complete mark ho gaya!")
            else:
                print("Galat number dala!")
        except ValueError:
            print("Sirf number dalo!")

def delete_task(tasks):
    view_task(tasks)
    if tasks:
        try:
            index = int(input("Kaunsa task delete karna hai? (Number dalo): ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' delete ho gaya!")
            else:
                print("Galat number dala!")
        except ValueError:
            print("Sirf number dalo!")

def main():
    tasks = [] # Ye ek khali list hai jahan tasks store honge

    while True:
        print("\n==== TO DO List ====")
        print("1. Add task")
        print("2.View task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        chooise = input("please enter youe option (1-5)")
        if chooise == "1":
            add_task(tasks)
            
        elif chooise == "2":
            view_task(tasks)
            
            
        elif chooise == "3":
            mark_complete(tasks)
           
        elif chooise == "4":
            delete_task(tasks)
            
            print("exit thank you")
            break
        else:
            print("sai number enter karo")

if __name__ == "__main__":
    main()



    
