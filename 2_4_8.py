from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    # Wait and click button
    element1 = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button =  browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    # Скрол
    button1 = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    #считываем   переменную x_element
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    print(x_element)
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    # Ввод значения Y в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # Нажимаем кнопку
    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    button2.click()
finally:    
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

    
# не забываем оставить пустую строку в конце файла

    