from config import bot_name, password, nick_in_the_game, quantity_bot
import create_anonim_emai
import re, os, random, string, time
from selenium import webdriver
from selenium.webdriver.common.by import By



url = 'https://forum.advance-rp.ru/register/'

def generate_random_email():
    domain_list = ["1secmail.com", "1secmail.org", "1secmail.net"]
    domain = random.choice(domain_list)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
    return f'{username}@{domain}'

def create_bot():
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

                print(str(matches)[2:-3])
                authenticity = webdriver.Chrome()
                authenticity.get(str(matches)[2:-3])

                attempts = 0
                max_attempts = 10

            while attempts < max_attempts:
                try:
                    os.remove(file_path)
                    print(f"Файл '{file_name}' успешно удален.")
                    print('\n', '-'*20, '\n')
                    break
                except PermissionError:
                    time.sleep(1)
                    attempts += 1

        driver.quit()
        authenticity.quit()


