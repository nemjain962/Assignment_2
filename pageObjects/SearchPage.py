from selenium.webdriver.common.by import By

from pageObjects.BaseClass import BaseClass

class SearchPage(BaseClass):
    """ SearchPage : contains the locators and operations associated to Search Result page"""
    matched_articles = (By.XPATH, "//div[@class='results-wrapper']//a")
    page_title = "Search"

    def __init__(self, driver):
        super().__init__(driver)

    def verify_title(self):
        """ verify_title : to verify the page title."""
        super().verify_title(self.page_title)

    def verify_links(self, article_url_prefix):
        """ verify_links : to verify the page title."""
        list_of_articles = self.get_list_of_links()

        if(len(list_of_articles)>=1):
            print(len(list_of_articles))
            i = 1
            flag = True
            for linkk in list_of_articles:
              strLink = linkk.get_attribute('href')

              verifyResult = strLink.startswith(article_url_prefix)
              print(i, strLink, verifyResult)
              i = i + 1
              if verifyResult == False:
                  flag = False
            return flag
