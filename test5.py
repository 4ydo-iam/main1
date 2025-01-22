note = {
    'Алексей': [{'заголовок': 'Список покупок', 'описание': 'Купить продукты на неделю'}],
     'Мария': [{'заголовок': 'Учёба', 'описание': 'Подготовиться к экзамену'}]
      }
print('Приветствую в менеджере заметок!')



my_list = []
def del_name():
    del_name1 = input('Введите "Имя" или "Заголовок" для удаления: ')
    for note in my_list:
        if user_name == del_name1:
            del note[del_name1]

        if del_name1 in note:
            del note[del_name1]

        if del_name1 in my_list:
            del note[del_name1]
            #display()
def del_notes():
    while True:
        del_ = input('Желаете Удалить заметку?(да/нет): ')
        if del_ == 'нет':
            print('Отлично! Всего доброго!')
            display()
            break
        if del_ == 'да':
            del_name()
        else:
            invalid_input()
def user_name():
    user_name1 =  input('Введите имя пользователя: ')
    return user_name1
def description():
    description1 = input('Введите описание заголовка: ')
    return description1
def title():
    title1 = input('Введите название заголовка: ')
    return title1
def invalid_input():
    return print('Ошибка! Не верный ввод! Используйте (да/нет)')
def display():
    print('\nВаши Заметки')
    for name,titl in note.items():
        for discription in titl:
            print(f'Имя пользователя: {name}')
            print(f'Название заголовка: {discription['заголовок']}')
            print(f'Описание заголовка: {discription['описание']}')
while True:
    new_titles = input('Желаете создать новую заметку?(да/нет): ')
    if new_titles == 'да':
        new_name = user_name()
        if new_name in note:
            print(f'Имя {new_name} уже существует!')
            note_name = input('Желаете создать для него заметку?(да/нет)')
            if note_name == 'да':
                note[new_name].append({'заголовок':title(),'описание':description()})
                print(f'Заметка для {new_name} успешно создана!')
                continue

        note[new_name] = []
    elif new_titles == 'нет':
        print(display())
        break
    else:
        invalid_input()
        continue
    while True:
        new_title = (title())
        new_description = (description())
        if new_title == '' or new_description == '':
            print('Не верный ввод! Поля "название" или "описание" не могут быть пустыми!')
        my_list ={'заголовок' : new_title,'описание': new_description}
        note[new_name].append(my_list)

        break
del_notes()



