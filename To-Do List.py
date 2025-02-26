# importing os library
import os

# creating a clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# main menu
menu = """1. Add task
2. Mark task as done
3. Edit task
4. Remove task
5. Show tasks
6. Exit
"""

# tasks list
tasks = []

# creating an add task function
def add_task():
    while True:
        show_tasks()
        task = duplicate_task()
        if task == '0':
            clear_screen()
            break
        tasks.append(task)
        clear_screen()

# creating an empty task function
def empty_task():
    while True:
        task = input('Enter the task or 0 to quit: ')
        if task.strip() == '':
            print('You cannot add an empty task')
        elif task.upper() == '0':
            clear_screen()
            return '0'
        else:
            return task

# creating a duplicate task function
def duplicate_task():
    while True:
        task = empty_task()
        if task.upper() in [element.upper() for element in tasks]: #if element is not None]:
            print('You cannot add a duplicate task')
        else:
            return task

# creating a mark done function
def mark_done():
    tick_mark = "\u2713"
    while True:
        show_tasks()
        i = check_marked()
        if i == -1:
            clear_screen()
            break
        elif i == -2:
            clear_screen()
            continue
        elif i < -1:
            print('Please choose a valid number')
        tasks[i] = f'{tasks[i]} {tick_mark}'
        clear_screen()

# creating a check marked function
def check_marked():
    i = check_in_list()
    if i < 0:
        clear_screen()
        return i
    while True:
        if tasks[i][-1] == "\u2713":
            i = -2
            return i
        else:
            return i

# creating a check number function
def check_number():
    while True:
        try:
            i = empty_task_2()
            i = int(i) - 1
            return i
        except:
            print('Please choose a valid number')

# creating a second empty task function
def empty_task_2():
    while True:
        task = input('Enter the task number or 0 to quit: ')
        if task.strip() == '':
            input('You cannot add an empty task\nPress any key to continue...')
        elif task.upper() == '0':
            clear_screen()
            return '0'
        else:
            return task

# creating a check in list function
def check_in_list():
    i = check_number()
    while i >= len(tasks):
        print('Please choose a valid number')
        i = check_number()
    return i

# creating an edit task function
def edit_task():
    while True:
        show_tasks()
        i = check_in_list()
        if i == -1:
            clear_screen()
            break
        elif i < -1:
            print('Please choose a valid number')
        new_task = input(f'The chosen task is: {tasks[i]}\nEnter the new task: ')
        tasks[i] = new_task
        clear_screen()

# creating a remove task function
def remove_task():
    while True:
        show_tasks()
        i = check_in_list()
        if i == -1:
            clear_screen()
            break
        elif i < -1:
            print('Please choose a valid number')
        print(f'The deleted task is: {tasks[i]}')
        del tasks[i]
        clear_screen()

# creating a show tasks function
def show_tasks():
    for i, task in enumerate(tasks):
        print(f'{i + 1}- {tasks[i]}')

# take user name
while True:
    name = input('Enter your name: ')
    if name.strip() == '':
        input('You cannot add an empty name\nPress any key to continue...')
    else:
        clear_screen()
        break
print(f'Welcome {name.title()}!\nThis is your personalised to-do list!')

# run the program
while True:
    choice = input(menu)
    if choice == '6':
        break
    elif choice == '1':
        clear_screen()
        add_task()
    elif choice == '2':
        clear_screen()
        mark_done()
    elif choice == '3':
        clear_screen()
        edit_task()
    elif choice == '4':
        clear_screen()
        remove_task()
    elif choice == '5':
        clear_screen()
        show_tasks()
        input('Press any key to return to main menu...')
        clear_screen()
    else:
        input('Invalid choice\nPress any key to continue...')
        clear_screen()
