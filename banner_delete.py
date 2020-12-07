from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_banner():
    driver = webdriver.Chrome('D:/chromedriver')
    # максимальная ширина страницы
    driver.maximize_window()
    # Переход на главную страницу
    driver.get('https://aliexpress.ru/home.htm')
    # ожидаем баннер
    wait = WebDriverWait(driver, 10)
    # переключение на iframe, для поиска и взаимодействия с баннером
    driver.switch_to.frame('pc_1455_24317_20201202')
    # проверка что баннер загрузился
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    assert len(driver.find_elements_by_css_selector('img.rax-image ')) == 2
    # закрываем баннер
    driver.find_elements_by_css_selector('img.rax-image ')[1].click()
    # переключение на главную страницу
    driver.switch_to.default_content()
    # проверка отсутствия баннера
    assert not driver.find_elements_by_css_selector('img.rax-image ')
    # нажимаем на кнопку с телефонами
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-phones .cate-name').click()
    # убираем баннер, нажимаем на крестик
    driver.find_element_by_css_selector('a.next-dialog-close').click()
    # проверка наличия товаров в категории
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()
    # проверка товаров по каждой категории
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-computer .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-electronics .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-homeImprovemen .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-women .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-men .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-toys .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-jewelry .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-shoes .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-garden .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-autoParts .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-beauty .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-sports .cate-name').click()
    assert len(driver.find_elements_by_css_selector('li.list-item')) >= 1
