import os

# empty list to store task
tasks = []


# display menu
def display_menu():
    print('\nTO-DO LIST: ')
    print('1. Add')
    print('2. View')
    print('3. Update')
    print('4. Delete')
    print('5. Exit')


# add new task
def add_task():
    task = input('Add New Task: ')
    tasks.append(task)
    print('Task Added')


# view the task list
def view_tasks():
    if not tasks:
        print('No tasks to show')
    else:
        print('TO-DO LIST: ')
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


# update task
def update_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input('Enter the task number to update: '))
            if 1 <= task_number <= len(tasks):
                new_task = input('Enter the new task: ')
                tasks[task_number-1] = new_task
                print('Task Updated')
            else:
                print('Invalid')
        except ValueError:
            print('Enter a valid number')


# delete task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input('Enter the task number to delete: '))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number-1)
                print(f"Task '{deleted_task}' Deleted")
            else:
                print('Invalid')
        except ValueError:
            print('Enter a valid number')


# main menu
def main():
    while True:
        display_menu()
        select = input('\nSelect an option: ')

        if select == '1':
            add_task()
        elif select == '2':
            view_tasks()
        elif select == '3':
            update_task()
        elif select == '4':
            delete_task()
        elif select == '5':
            print("Exit")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


main()


