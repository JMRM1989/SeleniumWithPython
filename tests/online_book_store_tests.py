from tests.pages.main_page import MainPage

chrome_path = '/usr/local/bin/chromedriver'


def test_online_book_store_R1(browser, root_url):
    # R1 For online new book purchasing regular customers with cards obtain 10% price reduction.
    new_book_input = '100'
    main_page = MainPage.navigate(browser)
    main_page.go_online_book_store()
    main_page.new_book(new_book_input)
    result = main_page.get_result_value()
    # 10% discount will always be granted for any customer that buys a book of at least 50
    assert result == '90'


def test_online_book_store_R2_NoDiscount(browser, root_url):
    # R2 Similarly, any customer buying new books for at least EUR 50 gets 10% price reduction.
    new_book_input = '40'
    main_page = MainPage.navigate(browser)
    main_page.go_online_book_store()
    main_page.new_book(new_book_input)
    result = main_page.get_result_value()

    # 10% discount will always be granted for any customer that buys a book of at least 50
    # if we try a value less than 50 we should get the discount
    assert result == '40'


def test_online_book_store_R3(browser, root_url):
    # R3 If somebody has a card and buys new books not less than EUR 50, then the price reduction is 15%.
    new_book_input = '50'
    main_page = MainPage.navigate(browser)
    main_page.go_online_book_store()
    main_page.check_box()
    main_page.new_book(new_book_input)
    result = main_page.get_result_value()

    assert result == '42.5'


def test_online_book_store_R4(browser, root_url):
    # R4 If a customer buys second hand books s/he gets price reduction 5%,
    # but only if the price of them exceeds EUR 60 and s/he also buys new books for more than EUR 30.
    new_book_input = '40'
    old_book_input = '70'
    main_page = MainPage.navigate(browser)
    main_page.go_online_book_store()
    main_page.newold_book(new_book_input, old_book_input)
    result = main_page.get_result_value()

    assert result == '106.5'


def test_online_book_store_R4_VIP(browser, root_url):
    # R4 If a customer buys second hand books s/he gets price reduction 5%,
    # but only if the price of them exceeds EUR 60 and s/he also buys new books for more than EUR 30.
    new_book_input = '40'
    old_book_input = '70'
    main_page = MainPage.navigate(browser)
    main_page.go_online_book_store()
    main_page.check_box()
    main_page.newold_book(new_book_input, old_book_input)
    result = main_page.get_result_value()

    assert result == '102.5'
