from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


name_bot = 'CoolBot_V1_№'
password = 'password2098715'
nick_in_the_game = 'nik_v_igre'
quantity_bot = 10


def put_reaction():

    url_to_the_page = input('Введите ссылку на страницу: ')
    post_number = int(input('Введите номер поста: '))
    reaction = input('Выберете реакцию[Клёво/Люблю/Ха-ха/Ничоси/Печалька/Отстой]: ')


    for i in range(1, quantity_bot+1):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url_to_the_page)

        driver.find_element(By.CLASS_NAME, 'p-navgroup-linkText').click()
        time.sleep(2)
        driver.find_elements(By.CLASS_NAME, 'input')[-2].send_keys(f'{name_bot}{i}')
        driver.find_elements(By.CLASS_NAME, 'input')[-1].send_keys(password)
        driver.find_elements(By.CLASS_NAME, 'iconic-label')[-1].click()
        driver.find_elements(By.CLASS_NAME, 'button-text')[-2].click()

        reaction_elements = driver.find_elements(By.CLASS_NAME, 'reaction-text.js-reactionText')
        target_element = reaction_elements[post_number-1]
        driver.execute_script("arguments[0].scrollIntoView();", target_element)



        x = driver.find_elements(By.CLASS_NAME, 'message-inner')[post_number-1]\
            .find_element(By.CSS_SELECTOR, '.message-cell.message-cell--main')\
            .find_element(By.CSS_SELECTOR, '.message-main.js-quickEditTarget')\
            .find_element(By.CSS_SELECTOR, '.message-attribution.message-attribution--split')\
            .find_element(By.CSS_SELECTOR, '.message-attribution-opposite.message-attribution-opposite--list ')\
            .find_element(By.TAG_NAME, 'li').find_element(By.TAG_NAME, 'a').get_attribute('href').split('-')[-1]

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

        driver.quit()
        confirm_reaction.quit()


if __name__ == '__main__':
    put_reaction()