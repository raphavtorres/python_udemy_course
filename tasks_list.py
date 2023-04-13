import os

tasks_list = ['teste1', 'teste2']


def list_tasks():
    print("\nTASKS:")
    print(*tasks_list, sep='\n')
    print()


def undo_task():
    if len(tasks_list) == 0:
        print("No tasks to undo")
    print('Undoing')


def redo_task():
    

    print('Redoing')


def test_user_input(user_input):
    if user_input == 'list':
        list_tasks()
    elif user_input == 'undo':
        undo_task(user_input)
    elif user_input == 'redo':
        redo_task()       
    elif user_input == 'clear':
         os.system('cls')
    else:
        tasks_list.append(user_input)
        


def main():
    while True:
        prev_list = [task for task in tasks_list]
        print("Commands: list, undo, redo, clear, exit")
        try:
            user_input = input("Type a task or command >> ").lower().strip()
        except:
            print('invalid input...')
            continue
        if user_input == 'exit': 
            break
        test_user_input(user_input)
        

if __name__ == '__main__':
    main()
