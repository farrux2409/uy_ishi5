import service
from dto import UserRegisterDTO
from utils import ResponseData
from colorama import Fore


def print_response(response: ResponseData):
    color = Fore.GREEN if response.status else Fore.RED
    print(color + str(response.data) + Fore.RESET)


def print_error(error: Exception):
    print(Fore.RED + str(error) + Fore.RESET)


def menu():
    print('Login       => 1')
    print('Register    => 2')
    print('Logout      => 3')
    print('Todo ADD    => 4')
    print('Todo Delete => 5')
    print('Todo Edit   => 6')
    print('Todo View   => 7')
    print('OneTodo View => 8')
    print('Quit        => q')
    return input('?: ')


def authentication():
    username = input('Username: ')
    password = input('Password: ')
    response: ResponseData = service.login(username, password)
    print_response(response)


def register():
    username = input('Username: ')
    password = input('Password: ')
    dto: UserRegisterDTO = UserRegisterDTO(username=username, password=password)
    response: ResponseData = service.register(dto)
    print_response(response)


def logout():
    response: ResponseData = service.logout()
    print_response(response)


def add_todo():
    try:
        title = str(input('Todo title: '))
        response: ResponseData = service.add_todo(title)
        print_response(response)
    except Exception as e:
        print_error(e)


def delete_todo():
    response: ResponseData = service.delete_todo()
    print(response)


def edit_todo():
    try:
        title = str(input('Todo title: '))
        response: ResponseData = service.edit_todo(title)
        print_response(response)
    except Exception as e:
        print_error(e)


def view_todo():
    response = service.view_todo()
    print(response)


def view_one_todo():
    response = service.view_one_todo()
    print(response)


if __name__ == '__main__':
    while True:
        choice = menu()
        if choice == '1':
            authentication()
        elif choice == '2':
            register()
        elif choice == '3':
            logout()

        elif choice == '4':
            add_todo()
        elif choice == '5':
            delete_todo()
        elif choice == '6':
            edit_todo()
        elif choice == '7':
            view_todo()

        elif choice == 'q':
            break
