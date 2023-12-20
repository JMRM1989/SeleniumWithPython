from tests.pages.main_page import MainPage

chrome_path = '/usr/local/bin/chromedriver'


def test_price_calculation_R1(browser, root_url):
    # R1 The customer gets 10% price reduction if the price of the goods reaches 200 euros.
    price_value = '200'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.price_calculation(price_value)
    result = main_page.get_result_value()

    # input is 200 after getting 10% discount the total price should be 180
    assert result == '180'


def test_prince_calculation_R1_NoDiscount(browser, root_url):
    # R1 The customer gets 10% price reduction if the price of the goods reaches 200 euros.
    price_value = '100'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.price_calculation(price_value)
    result = main_page.get_result_value()

    # input is 100 not discount will be offer so the total price will be 100
    assert result == '100'


def test_price_calculation_R2(browser, root_url):
    # R2 The delivery is free if the total weight of the goods is under five kilograms.
    # Reaching 5 kg, the delivery price is the weight in euros.
    # E.g. when the products together are 6 kilograms then the delivery price is 6 euros.
    price_value = '100'
    weight_value = '4'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # the weigh is less than 5 so the total price won't have the weigh price increase
    assert result == '100'


def test_price_calculation_R2_WeightPriceIncrease(browser, root_url):
    # R2 The delivery is free if the total weight of the goods is under five kilograms.
    # Reaching 5 kg, the delivery price is the weight in euros.
    # E.g. when the products together are 6 kilograms then the delivery price is 6 euros.
    price_value = '100'
    weight_value = '5'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # the weigh is more than 5 so the total price will have the weigh price increase
    assert result == '105'


def test_price_calculation_R3(browser, root_url):
    # The delivery remains free if the price of the goods exceeds 100 euros.
    price_value = '150'
    weight_value = '10'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # even though we exceeded the 5kg we won't be charge the delivery since also exceeded the 100 price
    assert result == '150'


def test_price_calculation_R3_Delivery(browser, root_url):
    # The delivery remains free if the price of the goods exceeds 100 euros.
    price_value = '99'
    weight_value = '10'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # we exceeded the 5kg weigh limit, will be charge for the delivery
    assert result == '109'


def test_price_calculation_R4(browser, root_url):
    # R4 If the customer prepays with a credit card,
    # then s/he gets 3% price reduction from the reduced price of the goods.
    price_value = '100'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.check_box()
    main_page.price_calculation(price_value)
    result = main_page.get_result_value()

    # We get a 3% discount paying with credit card so the total price will be 97
    assert result == '97'


def test_price_calculation_R5(browser, root_url):
    # R5 If the price reaches 200 euros and the customer pays with credit card,
    # and the weight is under 5 kg, then the customer gets a 15% price reduction for
    # the original price of the goods.
    price_value = '200'
    weight_value = '4'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.check_box()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # if the price, weight and credit card conditions are met you should get 170
    assert result == '170'


def test_price_calculation_R5_NoWeightCondition(browser, root_url):
    # R5 If the price reaches 200 euros and the customer pays with credit card,
    # and the weight is under 5 kg, then the customer gets a 15% price reduction for
    # the original price of the goods.
    price_value = '200'
    weight_value = '5'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.check_box()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # if weight conditions is met you should get 174.6
    assert result == '174.6'


def test_price_calculation_R5_NoPriceWeightCondition(browser, root_url):
    # R5 If the price reaches 200 euros and the customer pays with credit card,
    # and the weight is under 5 kg, then the customer gets a 15% price reduction for
    # the original price of the goods.
    price_value = '190'
    weight_value = '4'
    main_page = MainPage.navigate(browser)
    main_page.go_price_calculation()
    main_page.check_box()
    main_page.weigh_calculation(price_value, weight_value)
    result = main_page.get_result_value()
    # if the price, weight conditions are not met we will get 184.3
    assert result == '184.3'
