from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_banner():
    driver = webdriver.Chrome('D:/chromedriver')
    # открываю страницу
    driver.maximize_window()
    # Переход на главную страницу
    driver.get('https://aliexpress.ru/home.htm')
    # ожидаем появление  баннера
    wait = WebDriverWait(driver, 10)
    # переключение на iframe, для поиска и взаимодействия с баннером
    driver.switch_to.frame('pc_1455_24317_20201201')
    # проверка загрузки баннера
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.rax-image ')))
    assert len(driver.find_elements_by_css_selector('img.rax-image ')) == 2
    # нажимаем на закрытие баннера
    driver.find_elements_by_css_selector('img.rax-image ')[1].click()
    # переключаемся на главную страницу
    driver.switch_to.default_content()
    # проверка отсутствия баннера
    assert not driver.find_elements_by_css_selector('img.rax-image ')
    # нажимаем на кнопку с телефонами
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-phones .cate-name').click()
    # убираем баннер

    driver.switch_to.frame(driver.find_elements_by_css_selector('ym-native-frame'))
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.next-dialog-close')))
    # assert len(driver.find_elements_by_css_selector('a.next-dialog-close')) == 1
    driver.find_element_by_css_selector('a.next-dialog-close').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()
    # проверка товаров во всех категориях
    driver.find_element_by_css_selector('#home-firstscreen .cl-item-computer .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-electronics .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-homeImprovemen .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-women .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-men .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-toys .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-jewelry .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-shoes .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-garden .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-autoParts .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-beauty .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
    driver.back()

    driver.find_element_by_css_selector('#home-firstscreen .cl-item '
                                        'cl-item-sports .cate-name').click()
    assert len(driver.find_elements_by_class_name('list product-card')) >= 1
