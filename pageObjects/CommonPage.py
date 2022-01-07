from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.BaseClass import BaseClass


class CommonPage(BaseClass):
    """
     Common Page : this class contains locators and their operations for
     common elements on the page like headers, cookies settings etc
    """

    language_selector = (By.CSS_SELECTOR, "#language-dropdown-flag img")
    locale_list_element = By.ID, 'nav-languages'
    locale_path = (By.XPATH, "//div[@id='nav-languages']//a[contains(.,'USA')]")
    search_lens = (By.CSS_SELECTOR, ".navigation-search")
    search_text = (By.ID, "nav_search")
    accept_cookies_button = (By.ID, "onetrust-accept-btn-handler")
    cookie_frame = (By.XPATH, '//iframe[@title="_hjRemoteVarsFrame"]')

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies(self):
        """accept_cookies : to click the accept button on the cookies modal appeared at bottom"""
        self.click(self.accept_cookies_button)

    def search(self, txt):
        """ search: to search a given term using search feature """

        # click on search icon on the header
        self.click(self.search_lens)

        # click on the search text box
        self.click(self.search_text)

        # enter the search string in the search box
        self.enter_text(self.search_text, txt)

        # enter the return key in the search box to trigger the search
        self.click_enter(self.search_text)

    def select_locale(self):
        """ select_locale : to select the language using language selector feature"""

        # click on the language selector icon
        self.click(self.language_selector)

        # Use mouse click and drag functionaltiy through selenium action class
        action_class = ActionChains(self.driver)

        source = self.driver.find_element(By.ID, 'nav-languages')
        not_found_flag = True
        while not_found_flag:
            try:
                action_class.click_and_hold(source) \
                    .move_by_offset(0, -100) \
                    .pause(2) \
                    .release() \
                    .perform()
                self.click(self.locale_path)
                not_found_flag = False
            except:
                not_found_flag = True
