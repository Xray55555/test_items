from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket(browser, language):
    browser.get(link)
    time.sleep(30) # задержка выполнения теста по требованию условий задачи (проверка смены языка)

    y = len(browser.find_elements(By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket'))

    assert y > 0, 'Кнопка не найдена!'