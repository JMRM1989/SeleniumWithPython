from selenium.webdriver.common.by import By


class PageLocators:
    # Price Calculation Page Locators
    price_calculation = (
    By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[1]/div/main/div/article/div/figure[1]/table/tbody/tr[2]/td[1]/a')
    price_input = (By.XPATH, '/html/body/div/div/header[2]/p[3]/input[1]')
    weight_input = (By.XPATH, '/html/body/div/div/header[2]/p[3]/input[2]')
    next_test_button = (By.XPATH, '/html/body/div/div/header[2]/p[3]/button[1]')
    result = (By.XPATH, '/html/body/div/div/header[2]/p[3]/span[3]')
    checkbox = (By.XPATH, '/html/body/div/div/header[2]/p[3]/input[3]')

    # Online Book Store Page Locators
    online_book_store = (
    By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/main/div/article/div/figure[1]/table/tbody/tr[3]/td[1]/a')
    new_book = (By.XPATH, '/html/body/div/div/header[2]/p[3]/input[1]')
    old_book = (By.XPATH, '/html/body/div/div/header[2]/p[3]/input[2]')

    # Car Rental Page Locators
    car_rental = (
    By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[1]/div/main/div/article/div/figure[2]/table/tbody/tr[2]/td[1]/a')
    add_car_button = (By.XPATH, '/html/body/div/div/header[2]/p[3]/button[1]')
    remove_car_button = (By.XPATH,'/html/body/div/div/header[2]/p[3]/button[2]')
    add_bike_button = (By.XPATH, '/html/body/div/div/header[2]/p[3]/button[3]')
    remove_bike_button = (By.XPATH,'/html/body/div/div/header[2]/p[3]/button[4]')
    number_of_cars = (By.XPATH,'/html/body/div/div/header[2]/p[3]/span[2]')
    number_of_bikes = (By.XPATH,'/html/body/div/div/header[2]/p[3]/span[3]')
    total_rent_price = (By.XPATH,'/html/body/div/div/header[2]/p[3]/span[4]')


