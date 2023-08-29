from selenium.webdriver.common.by import By


class kartHomePages:
    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "h4[class='product-name']")
    addToCart = (By.CSS_SELECTOR, "div[class='product-action'] button")
    cartBtn = (By.CLASS_NAME, "cart-icon")
    proceedToCheckOut = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def getProducts(self):
        return self.driver.find_elements(*kartHomePages.products)

    def getAddToCart(self):
        return self.driver.find_elements(*kartHomePages.addToCart)

    def getCartBtn(self):
        return self.driver.find_element(*kartHomePages.cartBtn)

    def getProceedToCheckOut(self):
        return self.driver.find_element(*kartHomePages.proceedToCheckOut)
