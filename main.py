from config import bot_name, password, quantity_bot, nick_in_the_game
import tkinter as tk
from tkinter import ttk
import create_anonim_emai
import re, os, random, string, time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--headless')
url = 'https://forum.advance-rp.ru/register/'


def generate_random_email():
    domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
    domain = random.choice(domain_list)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
    return f'{username}@{domain}'

def create_bot(bot_name, password, nick_in_the_game, quantity_bot):

    for i in range(1, quantity_bot+1):
        mail = generate_random_email()
        driver = webdriver.Chrome()
        driver.get(url)
        input_fields = driver.find_elements(By.CLASS_NAME, 'input')[0:]
        labels = driver.find_elements(By.CLASS_NAME, 'formRow-label')[0:]

        for label, input_field in zip(labels, input_fields):
            if label.text == 'Имя пользователя':
                input_field.send_keys(f'{bot_name}{i}')
            elif label.text == 'Электронная почта':
                input_field.send_keys(mail)
            elif label.text == 'Пароль':
                input_field.send_keys(f'{password}')
            elif label.text == 'Ник в игре':
                input_field.send_keys(f'{nick_in_the_game}{i}')
            elif label.text == 'Сервер':
                input_field.click()
                driver.find_elements(By.TAG_NAME, 'option')[-2].click()
        driver.find_elements(By.CLASS_NAME, 'iconic')[-1].find_element(By.TAG_NAME, 'i').click()
        time.sleep(30)
        driver.find_element(By.ID, 'js-signUpButton').click()


        create_anonim_emai.main(mail=mail)

        files_in_folder = os.listdir('all_mails')
        if len(files_in_folder) == 1:
            file_name = files_in_folder[0]
            file_path = os.path.join('all_mails', file_name)
            with open(file_path, 'r') as file:
                file_contents = file.read()
                pattern = r"https://forum\.advance-rp\.ru/account-confirmation/.+"
                matches = re.findall(pattern, file_contents)

                # print(str(matches)[2:-3])
                authenticity = webdriver.Chrome()
                authenticity.get(str(matches)[2:-3])

                attempts = 0
                max_attempts = 10

            while attempts < max_attempts:
                try:
                    os.remove(file_path)
                    # print(f"Файл '{file_name}' успешно удален.")
                    # print('\n', '-'*20, '\n')
                    break
                except PermissionError:
                    time.sleep(1)
                    attempts += 1

        driver.quit()
        authenticity.quit()



def put_reaction(bot_name, password, quantity_bot, root):
    def main_ction(url_to_the_page, reaction):

        for i in range(1, quantity_bot+1):
            x = url_to_the_page.split('-')[-1]

            d = {'Клёво': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=1',
                 'Люблю': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=2',
                 'Ха-ха': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=3',
                 'Ничоси': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=4',
                 'Печалька': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=5',
                 'Отстой': f'https://forum.advance-rp.ru/posts/{x}/react?reaction_id=6'}


            confirm_reaction = webdriver.Chrome(options=options)
            confirm_reaction.get(url=d[reaction])

            confirm_reaction.find_elements(By.CLASS_NAME, 'input')[0].send_keys(f'{bot_name}{i}')
            confirm_reaction.find_elements(By.CLASS_NAME, 'input')[-1].send_keys(password)
            confirm_reaction.find_elements(By.CLASS_NAME, 'button-text')[2].click()
            confirm_reaction.find_element(By.CSS_SELECTOR, '.button--primary.button.button--icon.button--icon--confirm').click()

            confirm_reaction.quit()

        frame2.destroy()


    frame2 = tk.Toplevel(root)
    frame2.title("Консоль упровления ботами")
    frame2.geometry("600x230+700+300")
    icon = tk.PhotoImage(file="images/AdvanceLogo.png")
    frame2.iconphoto(False, icon)
    frame2.resizable(False, False)

    global entry_var
    entry_var = tk.StringVar()

    lable_seting = ttk.Label(frame2, text="| НАСТРОЙКИ |")
    label_link = ttk.Label(frame2, text="Введите ссылку на пост: ")
    lable_dash = ttk.Label(frame2, text="-" * 120)
    combobox_react = ttk.Combobox(frame2, values=["Клёво", "Люблю", "Ха-ха", "Ничоси", "Печалька", "Отстой"])
    lable_combobox_react = ttk.Label(frame2, text="Выберете реакцию: ")
    start_btn = ttk.Button(frame2, text='Старт', command=lambda: main_ction(entry_var.get(), combobox_react.get()))

    lable_seting.grid(column=0, row=0, columnspan=2)
    lable_dash.grid(column=0, row=1, columnspan=2)
    label_link.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
    ttk.Entry(frame2, textvariable=entry_var, width=55).grid(column=1, row=2, pady=10, sticky=tk.W)
    lable_combobox_react.grid(column=0, row=3, padx=10, pady=10, sticky=tk.E)
    combobox_react.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)
    start_btn.grid(column=0, row=4, padx=10, pady=10, sticky=tk.EW, columnspan=2, rowspan=2)


    root.mainloop()


def remove_reactions(bot_name, password, quantity_bot, root):
    def main_ction(url_to_the_page, post_number):
        for i in range(1, quantity_bot + 1):
            driver = webdriver.Chrome(options=options)
            driver.get(url_to_the_page)

            driver.find_element(By.CLASS_NAME, 'p-navgroup-linkText').click()
            time.sleep(2)
            driver.find_elements(By.CLASS_NAME, 'input')[-2].send_keys(f'{bot_name}{i}')
            driver.find_elements(By.CLASS_NAME, 'input')[-1].send_keys(password)
            driver.find_elements(By.CLASS_NAME, 'iconic-label')[-1].click()
            driver.find_elements(By.CLASS_NAME, 'button-text')[-2].click()

            reaction_elements = driver.find_elements(By.CLASS_NAME, 'reaction-text.js-reactionText')
            target_element = reaction_elements[post_number - 1]
            driver.execute_script("arguments[0].scrollIntoView();", target_element)
            driver.execute_script("arguments[0].click();", target_element)

            driver.quit()

        frame2.destroy()


    frame2 = tk.Toplevel(root)
    frame2.title("Консоль упровления ботами")
    frame2.geometry("600x230+700+300")
    icon = tk.PhotoImage(file="images/AdvanceLogo.png")
    frame2.iconphoto(False, icon)
    frame2.resizable(False, False)

    global entry_var_link, entry_var_number
    entry_var_link = tk.StringVar()
    entry_var_number = tk.IntVar()

    lable_seting = ttk.Label(frame2, text="| НАСТРОЙКИ |")
    label_link = ttk.Label(frame2, text="Введите ссылку на страницу: ")
    lable_dash = ttk.Label(frame2, text="-" * 120)
    lable_number_post = ttk.Label(frame2, text="Введите номер поста: ")
    start_btn = ttk.Button(frame2, text='Старт', command=lambda: main_ction(entry_var_link.get(), entry_var_number.get()))

    lable_seting.grid(column=0, row=0, columnspan=2)
    lable_dash.grid(column=0, row=1, columnspan=2)
    label_link.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
    ttk.Entry(frame2, textvariable=entry_var_link, width=55).grid(column=1, row=2, pady=10, sticky=tk.W)
    lable_number_post.grid(column=0, row=3, padx=10, pady=10, sticky=tk.E)
    ttk.Entry(frame2, textvariable=entry_var_number).grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)
    start_btn.grid(column=0, row=4, padx=10, pady=10, sticky=tk.EW, columnspan=2, rowspan=2)


def write_messages(bot_name, password, quantity_bot):
    url_to_the_page = input('Введите ссылку на страницу: ')
    message = input('Введите текст сообщения: ')

    for i in range(1, quantity_bot+1):
        driver = webdriver.Chrome(options=options)
        driver.get(url_to_the_page)

        driver.find_element(By.CLASS_NAME, 'p-navgroup-linkText').click()
        time.sleep(2)
        driver.find_elements(By.CLASS_NAME, 'input')[-2].send_keys(f'{bot_name}{i}')
        driver.find_elements(By.CLASS_NAME, 'input')[-1].send_keys(password)
        driver.find_elements(By.CLASS_NAME, 'iconic-label')[-1].click()
        driver.find_elements(By.CLASS_NAME, 'button-text')[-2].click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.CSS_SELECTOR, '.fr-element.fr-view.fr-element-scroll-visible').send_keys(message)
        driver.find_elements(By.CLASS_NAME, 'button-text')[-3].click()

        driver.quit()

def main():
    func_dict = {'Создать ботов': create_bot,
                 'Поставить реакции на пост': put_reaction,
                 'Убрать реакции': remove_reactions,
                 'Написать сообщения в теме': write_messages}


    def finish():
        root.destroy()

    root = tk.Tk()
    root.title("Консоль упровления ботами")
    icon = tk.PhotoImage(file="images/AdvanceLogo.png")
    root.iconphoto(False, icon)
    root.geometry("600x230+700+300")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", finish)

    bot_name_widget = tk.StringVar(value=bot_name)
    password_widget = tk.StringVar(value=password)
    nick_in_the_game_widget = tk.StringVar(value=nick_in_the_game)
    quantity_bot_widget = tk.IntVar(value=quantity_bot)


    create_bot_btn = ttk.Button(text="Создать ботов",
                                command=lambda: create_bot(bot_name_widget.get(),
                                                           password_widget.get(),
                                                           nick_in_the_game_widget.get(),
                                                           quantity_bot_widget.get()))
    put_reaction_btn = ttk.Button(text='Поставить реакции',
                                  command=lambda: put_reaction(bot_name_widget.get(),
                                                               password_widget.get(),
                                                               quantity_bot_widget.get(),
                                                               root))
    remove_reactions_btn = ttk.Button(text='Убрать реакции',
                                      command=lambda: remove_reactions(bot_name_widget.get(),
                                                                       password_widget.get(),
                                                                       quantity_bot_widget.get(),
                                                                       root))
    write_messages_btn = ttk.Button(text='Написать сообщения в теме',
                                    command=lambda: write_messages(bot_name_widget.get(),
                                                                   password_widget.get(),
                                                                   quantity_bot_widget.get()))

    label_settings = ttk.Label(text='| НАСТРОЙКИ |')
    label_action = ttk.Label(text="| ВЫБЕРИТЕ ДЕЙСТВИЕ |")
    label_bot_name = ttk.Label(text="Имя бота:")
    lable_password_widget = ttk.Label(text="Пароль:")
    lable_nick_in_the_game_widget = ttk.Label(text="Ник в игре:")
    lable_quantity_bot_widget = ttk.Label(text="Количество ботов:")
    lable_dash = ttk.Label(text="-"*120)



    label_action.grid(column=0, row=0, padx=5, pady=10, columnspan=4)
    create_bot_btn.grid(column=0, row=1, padx=5, pady=10)
    put_reaction_btn.grid(column=1, row=1, padx=5, pady=10)
    remove_reactions_btn.grid(column=2, row=1, padx=5, pady=10)
    write_messages_btn.grid(column=3, row=1, padx=5, pady=10)
    label_settings.grid(column=0, row=2, padx=5, pady=10, columnspan=4)
    label_bot_name.grid(column=0, row=3, pady=10, sticky=tk.E)
    ttk.Entry(textvariable=bot_name_widget).grid(column=1, row=3, pady=10, sticky=tk.W)
    lable_password_widget.grid(column=2, row=3, pady=10, sticky=tk.E)
    ttk.Entry(textvariable=password_widget).grid(column=3, row=3, pady=10, sticky=tk.W)
    lable_nick_in_the_game_widget.grid(column=0, row=4, pady=10, sticky=tk.E)
    ttk.Entry(textvariable=nick_in_the_game_widget).grid(column=1, row=4, pady=10, sticky=tk.W)
    lable_quantity_bot_widget.grid(column=2, row=4, pady=10, sticky=tk.E)
    ttk.Entry(textvariable=quantity_bot_widget).grid(column=3, row=4, pady=10, sticky=tk.W)
    lable_dash.grid(column=0, row=5, columnspan=4, sticky=tk.SW)

    root.mainloop()



    # print('Доступные варианты: [Создать ботов | Поставить реакции на пост | Убрать реакции | Написать сообщения в теме]')
    # choice = input('Выберите действие: ')
    # print(f'Вы выбрали: {choice}\n', '-'*(12+len(choice)))

    # func_dict[choice]()


if __name__ == '__main__':
    main()

