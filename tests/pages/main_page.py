from tests.pages.base_page import BasePage
from tests.utils.locators import PageLocators as Locator


class MainPage(BasePage):
    @staticmethod
    def navigate(driver):
        page = MainPage(driver)
        page.navigate_to()
        return page

    def go_price_calculation(self):
        self.click_on(Locator.price_calculation)
        return self

    def go_online_book_store(self):
        self.click_on(Locator.online_book_store)
        return self

    def go_car_rental(self):
        self.click_on(Locator.car_rental)
        return self

    def price_calculation(self, txt):
        self.enter_txt(Locator.price_input, txt)
        self.click_on(Locator.next_test_button)
        return self

    def weigh_calculation(self, txt, txt2):
        self.enter_txt(Locator.price_input, txt)
        self.enter_txt(Locator.weight_input, txt2)
        self.click_on(Locator.next_test_button)
        return self

    def get_result_value(self):
        result = self.find_element(Locator.result).text
        return result

    def check_box(self):
        self.click_on(Locator.checkbox)
        return self

    def new_book(self, txt):
        self.enter_txt(Locator.new_book, txt)
        self.click_on(Locator.next_test_button)
        return self

    def newold_book(self, txt, txt2):
        self.enter_txt(Locator.new_book, txt)
        self.enter_txt(Locator.old_book, txt2)
        self.click_on(Locator.next_test_button)
        return self

    def add_car(self):
        self.click_on(Locator.add_car_button)
        return self

    def remove_car(self):
        self.click_on(Locator.remove_car_button)
        return self

    def add_bike(self):
        self.click_on(Locator.add_bike_button)
        return self

    def remove_bike(self):
        self.click_on(Locator.remove_bike_button)
        return self

    def click_next_test(self):
        self.click_on(Locator.next_test_button)
        return self

    def get_rental_price(self):
        result = self.find_element(Locator.total_rent_price).text
        return result
