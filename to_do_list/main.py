from functions import test_user_input


def main():
    tasks_list = []
    trash_list = []

    while True:
        print(f'{tasks_list=}\n{trash_list=}')
        print("Commands: list, undo, redo, clear, delete, exit")
        try:
            user_input = input("Type a task or command >> ").lower().strip()
        except ValueError:
            print('invalid input...')
            continue
        if user_input == 'exit':
            break
        test_user_input(user_input, tasks_list, trash_list)


if __name__ == '__main__':
    main()
