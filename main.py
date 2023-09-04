from selenium import webdriver
from selenium.webdriver.common.by import By
import time


name_bot = 'CoolBot_V1_№'
password = 'password2098715'
nick_in_the_game = 'nik_v_igre'
quantity_bot = 10


def put_reaction():

    url_to_the_page = input('Введите ссылку на страницу: ')
    post_number = int(input('Введите номер поста: '))

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
        driver.execute_script("arguments[0].click();", target_element)

        driver.quit()


if __name__ == '__main__':
    put_reaction()