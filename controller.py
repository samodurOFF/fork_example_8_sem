import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        
        if answer == '1':
            date = model.get_data()
            view.show_contacts(date)

        elif answer == '2':
            contact = input('Введите данные контакта через пробел: ')
            res = model.add_contact(contact)
            if res:
                view.success(res)
            else:
                view.not_success(res)

        elif answer == '3': 
            contact = input('Введите данные контакта для внесения изменений: ') 
            res = model.contact_change(contact)
            if res:
                view.data_changed(res)
            else:
                view.data_exists(res)

        elif answer == '4': 
            contact = input('Введите данные контакта для удаления контакта: ') 
            res = model.contact_delite(contact)
            view.delite(res)

        elif answer == '5':
            contact = input('Введите данные контакта для поиска: ')
            result = model.find(contact)
            view.show_contacts(result)

        elif answer == '6':
            break
        else:
            view.error()
