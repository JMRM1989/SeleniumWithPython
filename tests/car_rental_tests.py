from tests.pages.main_page import MainPage

chrome_path = '/usr/local/bin/chromedriver'


def test_car_rental_R1_addCar(browser, root_url):
    # R1 The customer can add cars or bikes one by one to the rental order.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_car()
    total_price = main_page.get_rental_price()

    assert total_price == '300'


def test_car_rental_R1_addBike(browser, root_url):
    # R1 The customer can add cars or bikes one by one to the rental order.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_bike()
    total_price = main_page.get_rental_price()

    assert total_price == '100'


def test_car_rental_R1_addCarBike(browser, root_url):
    # R1 The customer can add cars or bikes one by one to the rental order.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_car()
    main_page.add_bike()
    total_price = main_page.get_rental_price()

    assert total_price == '400'


def test_car_rental_R3a(browser, root_url):
    # R3 If the customer rents cars for more than EUR 600, then they can rent one bike for free. In case of discount:
    # R3a If the customer has selected some bikes previously, then one of them becomes free.
    # R3b If the customer hasn't selected a bike previously, then one free bike is added.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_car()
    main_page.add_car()
    main_page.add_car()
    total_price = main_page.get_rental_price()

    assert total_price == '900'


def test_car_rental_R3b(browser, root_url):
    # R3 If the customer rents cars for more than EUR 600, then they can rent one bike for free. In case of discount:
    # R3a If the customer has selected some bikes previously, then one of them becomes free.
    # R3b If the customer hasn't selected a bike previously, then one free bike is added.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_bike()
    main_page.add_car()
    main_page.add_car()
    main_page.add_car()
    total_price = main_page.get_rental_price()

    assert total_price == '900'


def test_car_rental_R4a(browser, root_url):
    # R4 If the customer deletes some cars or motorcycles from the order that the offering threshold doesn't hold,
    # then any offering will be withdrawn. R4a When the discount is withdrawn but given again, and no bike was added
    # meanwhile, the customer gets the previous discount back. R4b When the discount is withdrawn and some bikes are
    # added when the discount is given again, then one of them becomes free.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_car()
    main_page.add_car()
    main_page.add_car()
    main_page.remove_bike()
    main_page.add_bike()
    total_price = main_page.get_rental_price()

    assert total_price == '900'


def test_car_rental_R4b(browser, root_url):
    # R4 If the customer deletes some cars or motorcycles from the order that the offering threshold doesn't hold,
    # then any offering will be withdrawn. R4a When the discount is withdrawn but given again, and no bike was added
    # meanwhile, the customer gets the previous discount back. R4b When the discount is withdrawn and some bikes are
    # added when the discount is given again, then one of them becomes free.
    main_page = MainPage.navigate(browser)
    main_page.go_car_rental()
    main_page.add_car()
    main_page.add_car()
    main_page.add_car()
    main_page.remove_bike()
    main_page.add_bike()
    main_page.add_bike()
    total_price = main_page.get_rental_price()

    assert total_price == '1000'
