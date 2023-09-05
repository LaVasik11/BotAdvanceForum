import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import create_bot
from config import bot_name, password, quantity_bot
import tkinter as tk
from tkinter import ttk




options = webdriver.ChromeOptions()
options.add_argument('--headless')

def put_reaction():

    url_to_the_page = input('Введите ссылку на пост: ')
    reaction = input('Выберете реакцию[Клёво/Люблю/Ха-ха/Ничоси/Печалька/Отстой]: ')


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


def remove_reactions():
    url_to_the_page = input('Введите ссылку на страницу: ')
    post_number = int(input('Введите номер поста: '))

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

    print('\n', '-'*16, '\n| Реакции убраны |\n', '-'*16)


def write_messages():
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
    func_dict = {'Создать ботов': create_bot.create_bot,
                 'Поставить реакции на пост': put_reaction,
                 'Убрать реакции': remove_reactions,
                 'Написать сообщения в теме': write_messages}


    def finish():
        root.destroy()

    root = tk.Tk()
    root.title("Консоль упровления ботами")
    icon = tk.PhotoImage(file="images/AdvanceLogo.png")
    root.iconphoto(False, icon)
    root.geometry("600x250+700+300")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", finish)

    bot_name_widget = tk.StringVar(value='CoolBot_V1_№')
    password_widget = tk.StringVar(value='password2098715')
    nick_in_the_game_widget = tk.StringVar(value='nik_v_igre')
    quantity_bot_widget = tk.IntVar(value=10)


    create_bot_btn = ttk.Button(text="Создать ботов", command=create_bot)
    put_reaction_btn = ttk.Button(text='Поставить реакции на пост', command=put_reaction)
    remove_reactions_btn = ttk.Button(text='Убрать реакции', command=remove_reactions)
    write_messages_btn = ttk.Button(text='Написать сообщения в теме', command=write_messages)
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

