from sys import platform
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
if platform == 'win32':
    from ttk import *
else:
    from tkinter import ttk
from crypt_file import generate_new_key, encrypting_file, decrypting_file
from cryptography.fernet import InvalidToken



key_file_name = ''
source_file_name = ''
destination_file_name = ''
new_key_file_name = ''
if platform == 'win32':
    x_entry = 165
    entry_width = 70
    x_label = 515
else:
    x_entry = 230
    entry_width = 62
    x_label = 635


def get_key():
    global key_file_name
    key_file_name = fd.askopenfilename()
    key_path = Entry(window, width=70)
    key_path.place(x=x_entry, y=20)
    key_path.delete(0, END)
    key_path.insert(0, key_file_name)


def get_sourse_file():
    global source_file_name
    source_file_name = fd.askopenfilename()
    source_path = Entry(window, width=70)
    source_path.place(x=x_entry, y=100)
    source_path.delete(0, END)
    source_path.insert(0, source_file_name)


def get_destination_file():
    global destination_file_name
    destination_file_name = fd.asksaveasfilename()
    destination_path = Entry(window, width=70)
    destination_path.place(x=x_entry, y=140)
    destination_path.delete(0, END)
    destination_path.insert(0, destination_file_name)


def execute_now():
    try:
        if not (source_file_name and destination_file_name and key_file_name):
            mb.showwarning('Подсказка', "Укажите:\n-\tключ\n-\tчто обработать и\n-\tкуда сохранить результат.")
        else:
            # Расшифровать
            if choose_direction.get() == 1:
                decrypting_file(source_file_name, destination_file_name, key_file_name)
                mb.showinfo('Результат', "Готово.")
            # Зашифровать
            elif choose_direction.get() == 2:
                encrypting_file(source_file_name, destination_file_name, key_file_name)
                mb.showinfo('Результат', "Готово.")
            else:
                mb.showwarning('Ошибка', "Направление шифрование указано неверно.")
    except InvalidToken:
        mb.showwarning('Ошибка', "Ключ не подходит. ¯\_(ツ)_/¯")


def get_new_key_file():
    global new_key_file_name
    new_key_file_name = fd.asksaveasfilename()
    new_key_path = Entry(window, width=70)
    new_key_path.place(x=x_entry, y=280)
    new_key_path.delete(0, END)
    new_key_path.insert(0, new_key_file_name)


def create_new_key_now():
    if not new_key_file_name:
        mb.showwarning('Подсказка', "Укажите куда сохранить ключ.")
    else:
        generate_new_key(new_key_file_name)
        mb.showinfo('Результат', "Ключ создан.")


window = Tk()
if platform == 'win32':
    window.style = Style()
    window.style.theme_use('xpnative')
    window.geometry('600x370')
else:
    window.style = ttk.Style()
    #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    window.style.theme_use('default')
    window.geometry('740x370')
window.wm_title('File encripter')


# Запрос параметров
key_file_name_button = Button(master=window, text='Укажите файл ключа      ', command=get_key).place(x=10, y=20)
key_path = Entry(window, width=entry_width).place(x=x_entry, y=20)
choose_direction = IntVar()
rbutton1=Radiobutton(window, text='Расшифровать', variable=choose_direction, value=1).place(x=10, y=60)
rbutton2=Radiobutton(window, text='Зашифровать', variable=choose_direction, value=2).place(x=150, y=60)

source_file = Button(master=window, text='Укажите исходный файл ', command=get_sourse_file).place(x=10, y=100)
source_path = Entry(window, width=entry_width).place(x=x_entry, y=100)
destination_file = Button(master=window, text='Куда сохранить результат', command=get_destination_file).place(x=10, y=140)
destination_path = Entry(window, width=entry_width).place(x=x_entry, y=140)

# Запуск
execute_now = Button(master=window, text='Выполнить', command=execute_now).place(x=270, y=180)

# Блок создания ключа
key_instruction = Label(master=window, text='Если вы хотите зашифровать файл, а ключа у вас нет, то его можно создать.').place(x=10, y=230)
key_instruction2 = Label(master=window, text='Для этого укажите куда его сохранить и как назвать файл с ключем:').place(x=10, y=250)
created_key_file = Button(master=window, text='Куда сохранить результат', command=get_new_key_file).place(x=10, y=280)
created_key_path = Entry(window, width=entry_width).place(x=x_entry, y=280)
# Генерация ключа
create_new_key_now = Button(master=window, text='Генерация ключа', command=create_new_key_now).place(x=255, y=320)

info = Label(master=window, text='SenseFlare Lab').place(x=x_label, y=350)

window.mainloop()
