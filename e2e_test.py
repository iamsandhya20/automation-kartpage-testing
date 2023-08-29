import time

import pytest
from selenium.webdriver.support.select import Select

from kartObjects.confirmPage import kartConfirmPage
from kartObjects.kartHomePages import kartHomePages
from kartObjects.kartPages import kartPages


@pytest.mark.usefixtures("setup")
class TestOne:
    def test_sample(self):
        karthomepages = kartHomePages(self.driver)
        products = karthomepages.getProducts()
        i = -1
        for product in products:
            i = i + 1
            name = product.text
            if "Tomato" in name:
                karthomepages.getAddToCart()[i].click()
            if "Mushroom" in name:
                karthomepages.getAddToCart()[i].click()
            if "Orange" in name:
                karthomepages.getAddToCart()[i].click()
            if "Raspberry" in name:
                karthomepages.getAddToCart()[i].click()
            if "Almonds" in name:
                karthomepages.getAddToCart()[i].click()
            if "Walnuts" in name:
                karthomepages.getAddToCart()[i].click()

        karthomepages.getCartBtn().click()
        karthomepages.getProceedToCheckOut().click()
        time.sleep(3)

        kartpage = kartPages(self.driver)
        sum = 0
        rates = kartpage.getRates()
        for rate in rates:
            sum = sum + int(rate.text)
        print(sum)
        total = int(kartpage.getTotal().text)
        assert sum == total

        kartpage.getPromoCode().send_keys("rahulshettyacademy")
        kartpage.getPromoBtn().click()
        time.sleep(12)
        text = kartpage.getPromoInfo().text
        assert text in "Code applied ..!"

        discount = float(kartpage.getDiscount().text)
        assert discount < total
        kartpage.getPlaceOrder().click()
        time.sleep(3)

        kartconfirmpage = kartConfirmPage(self.driver)
        country = Select(kartconfirmpage.getCountry())
        country.select_by_visible_text('India')
        time.sleep(2)
        kartconfirmpage.getAgree().click()
        kartconfirmpage.getProceed().click()
