import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    # Инициализация браузера 
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после завершения теста
    driver.quit()

def test_image_alt_attribute(browser):
    # Открываем страницу
    browser.get('https://shopiland.ru/')

    # Находим все элементы img на странице
    images = browser.find_elements_by_tag_name('img')

    # Проверяем, что каждое изображение содержит атрибут 'alt'
    for image in images:
        alt_attribute = image.get_attribute('alt')
        assert alt_attribute is not None and alt_attribute != ''

    # Опционально: выводим информацию о количестве изображений
    print(f"Total images found: {len(images)}")
