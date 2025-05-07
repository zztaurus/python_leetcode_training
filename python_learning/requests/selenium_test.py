from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    try:
        driver = webdriver.Chrome()
        driver.get("https://mail.163.com")
        driver.find_element(By.XPATH, '//*[@id="auto-id-1746536452365"]').send_keys("zztaurus@163.com")
        driver.find_element(By.XPATH, '//*[@id="auto-id-1746536452368"]').send_keys("159@Zhou")
        driver.find_element(By.XPATH, '//*[@id="dologin"]')
        cookies = driver.get_cookies()
        time.sleep(20)
        print(cookies)
    except Exception as error:
        print(error)
    finally:
        driver.close()


if __name__ == '__main__':
    main()