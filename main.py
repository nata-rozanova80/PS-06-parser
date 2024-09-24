import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)

time.sleep(10)

# После загрузки страницы
html_source = driver.page_source
print(html_source)  # Выводим HTML-код страницы

# Вы также можете записать HTML в файл для более удобного просмотра
with open("page_source.html", "w", encoding="utf-8") as file:
    file.write(html_source)


products = driver.find_elements(By.CLASS_NAME, 'wYUX2')
print("Найдено продуктов:", len(products))

parsed_data = []

for product in products:
    print(0)
    try:
# class="wYUX2"><a tabindex="0" class="ui-GPFV8 qUioe ProductName ActiveProduct"
# href="/product/divan-numo-velvet-yellow"><span itemprop="name">Диван Нумо Velvet Yellow</span></a>
# <link itemprop="url" href="https://www.divan.ru/product/divan-numo-velvet-yellow">
# <meta itemprop="price" content="36990"><meta itemprop="priceCurrency" content="RUB"><link itemprop="availability"
        print(1)
        # name = product.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').get_attribute('text')
        # Находим элемент по классу и извлекаем название
        name_element = driver.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct span[itemprop="name"]')
        product_name = name_element.text

        print(product_name)  # Выводим название продукта
        #print(name)
        price = product.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
        link = product.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')

        parsed_data.append([product_name, price, link])
        print(parsed_data)
    except NoSuchElementException as e:
        print("Нет такого элемента:", e)
        continue

driver.quit()

with open("mebel.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
