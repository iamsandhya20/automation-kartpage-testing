from selenium.webdriver.common.by import By


class kartConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "//label[text()='Choose Country']/parent::div/div/select")
    agree = (By.CLASS_NAME, "chkAgree")
    proceed = (By.XPATH, "//button[text()='Proceed']")

    def getCountry(self):
        return self.driver.find_element(*kartConfirmPage.country)

    def getAgree(self):
        return self.driver.find_element(*kartConfirmPage.agree)

    def getProceed(self):
        return self.driver.find_element(*kartConfirmPage.proceed)