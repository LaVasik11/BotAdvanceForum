import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import create_bot
import re


name_bot = 'CoolBot_V1_№'
password = 'password2098715'
nick_in_the_game = 'nik_v_igre'
quantity_bot = 10

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

        confirm_reaction.find_elements(By.CLASS_NAME, 'input')[0].send_keys(f'{name_bot}{i}')
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
        driver.find_elements(By.CLASS_NAME, 'input')[-2].send_keys(f'{name_bot}{i}')
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
        driver.find_elements(By.CLASS_NAME, 'input')[-2].send_keys(f'{name_bot}{i}')
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

    print('Доступные варианты: [Создать ботов | Поставить реакции на пост | Убрать реакции | Написать сообщения в теме]')
    choice = input('Выберите действие: ')
    print(f'Вы выбрали: {choice}\n', '-'*(12+len(choice)))

    func_dict[choice]()


if __name__ == '__main__':
    main()

