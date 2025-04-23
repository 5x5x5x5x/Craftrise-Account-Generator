from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import string
import random
import os
from fake_useragent import UserAgent

def type_like_human(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        sleep(delay)

def generate_random_password():
    special_chars = ".@!?"
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    required = [
        random.choice(uppercase),
        random.choice(special_chars),
        random.choice(digits),
        random.choice(lowercase)
    ]

    remaining_lenght = random.randint(4,8)
    remaining_chars = ''.join(random.choices(lowercase + uppercase + digits + special_chars, k=remaining_lenght))

    full_string = required + list(remaining_chars)
    random.shuffle(full_string)
    randompassword = ''.join(full_string)
    return "xHesap" + randompassword

password = generate_random_password()

def generate_random_gmail():
    lenght = random.randint(4, 15)
    letters_only = string.ascii_letters
    random_part = ''.join(random.choices(letters_only, k=lenght))
    return random_part.lower() + "@gmail.com"

mail = generate_random_gmail

def generate_random_username():
    lenght = random.randint(5, 12)
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))
    return "xHesap" + random_part

username = generate_random_username

ua = UserAgent()
user_agent = ua.random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.craftrise.com.tr/kayit")
driver.implicitly_wait(10)
sleep(5)

type_like_human(driver.find_element(By.CSS_SELECTOR, '[id="userName"]'), generate_random_username())
sleep(2)
type_like_human(driver.find_element(By.CSS_SELECTOR, '[id="userMail1"]'), generate_random_gmail())
sleep(2)
type_like_human(driver.find_element(By.CSS_SELECTOR, '[id="registerPass"]'), password)
sleep(2)
type_like_human(driver.find_element(By.CSS_SELECTOR, '[id="registerPass2"]'), password)
sleep(2)
driver.find_element(By.CSS_SELECTOR, '[id="registerTick"]').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, '[id="loginButton"]').click()
sleep(2)

print(f"Hesap Oluşturuldu! ==> Kullanıcı Adı: {username} | Şifre: {password} | Mail: {mail}")

with open("accounts.txt", "a") as file:
    file.write(f"Username: {username} | Password: {password} | Mail: {mail}\n")