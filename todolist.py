# daily to-do list manager

# initialize an empty to-do list
to_do_list = []

# initialize a list of options on the console
def terminal_menu():
    print('Hello and welcome to your to-do list manager.')
    print('1. Create Task\n2. Read To-do List\n3. Delete Task\n4. Exit to Terminal')

# create a task and add it to the to-do list
def create_task():
    task_name = input('1/2: Type the name of the task.\n')
    task_duration_mins = input('2/2: Type the task duration in minutes.\n')
    task_status = 'pending'

    to_do_item = (task_name, task_duration_mins, task_status)
    to_do_list.extend(to_do_item)

    print('Task item created:', task_name)

# read the to-do list contents
def read_list():
    print(to_do_list)

# update a task status in the to-do list
def update_task_status():
    task_name = input('1/2: Type the name of the task to be updated.\n')
    task_status = input('2/2: Type the new status of the task.\n')

    try:
        for i in range(len(to_do_list)):
            if to_do_list[i][0] == task_name:
                to_do_list[i] = (task_name, to_do_list[i][1], task_status)  # update the status of the task
                print('Task status updated successfuly:', task_name)
                break
        else:
            print('Task not found!')
    except:
        print('Task not found!')

# delete a task from the to-do list
def delete_task():

    task_name = input('Type the name of the task to be permanently deleted from the to-do list.\n')

    try:
        # filter out the task to be deleted
        to_do_list[:] = [item for item in to_do_list if item != task_name]
        print('Task deleted successfuly:', task_name)
    except:
        print('Task not found!')

# exit to terminal
def exit_to_terminal():
    confirm = input('Exit to terminal? Y/n\n')

    if confirm == 'Y' or confirm == 'y':
        print('Goodbye')
        quit()
    elif confirm == 'N' or confirm == 'n':
        pass
    else:
        print('Sorry, I did not understand that.')

terminal_menu()

while True:
    try:
        menu_option = int(input('Select an option from the numbered list.\n'))
    except:
        print('Invalid option! Please try again!')

    match menu_option:
        case 1:
            create_task()
        case 2:
            read_list()
        case 3:
            delete_task()
        case 4:
            exit_to_terminal()
        case _: 
            print('Invalid option! Please try again!')

