from selenium.webdriver.common.by import By
from pageObjects.BaseClass import BaseClass

class HomePage(BaseClass):
    """ HomePage : contains the locators and operations associated to Home Page"""
    page_title = "Foreign Exchange Solutions | moneycorp USA"
    Foreign_exchange_Findoutmore = (By.XPATH, "//h3[contains(text(),'Foreign exchange solutions')]/following-sibling::a/span")

    def __init__(self, driver):
        super().__init__(driver)

    def click_foreign_exchange_solution(self):
        self.click(self.Foreign_exchange_Findoutmore)

    def verify_title(self):
        super().verify_title(self.page_title)
