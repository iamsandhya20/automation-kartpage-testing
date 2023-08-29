from selenium.webdriver.common.by import By


class kartPages:
    def __init__(self, driver):
        self.driver = driver

    rate = (By.XPATH, "//tbody/tr/td[5]/p")
    total = (By.CLASS_NAME, "totAmt")
    promoCode = (By.CSS_SELECTOR, "input[class='promoCode']")
    promoBtn = (By.XPATH, "//button[text()='Apply']")
    promoInfo = (By.CSS_SELECTOR, "span[class='promoInfo']")
    discount = (By.CSS_SELECTOR, "span[class='discountAmt']")
    placeOrder = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def getRates(self):
        return self.driver.find_elements(*kartPages.rate)

    def getTotal(self):
        return self.driver.find_element(*kartPages.total)
    
    def getPromoCode(self):
        return self.driver.find_element(*kartPages.promoCode)

    def getPromoBtn(self):
        return self.driver.find_element(*kartPages.promoBtn)

    def getPromoInfo(self):
        return self.driver.find_element(*kartPages.promoInfo)

    def getDiscount(self):
        return self.driver.find_element(*kartPages.discount)

    def getPlaceOrder(self):
        return self.driver.find_element(*kartPages.placeOrder)