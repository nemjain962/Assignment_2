import time
import json

from pageObjects.CommonPage import CommonPage
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage

class Test_Quiz():
    """
        Class contains test cases specified in the quiz to validate foreign exchange portal.
    """

    def setup_method(self, method):
        """
            setup_method : to initialise the test data before every testcase
        """
        f = open(".\\conf\\test_data.json", "r")
        self.test_data = json.loads(f.read())
        f.close()

    def teardown_method(self, method):
        """
            teardown_method : to close the browser after every testcase
        """
        self.driver.quit()

    def test_question2(self, setup):
        """
            test_question2 function validates question 2 of the assignment.
            It is a positive testcase to validate following workflow

            Marks the testcase as Pass if all the above steps are working as mentioned,
             else marks the testcase as Fail
        """
        # 1. Open the following URL: https://www.moneycorp.com/en-gb/
        self.driver.get(self.test_data["common"]["url"])

        # 2. Change the language and region from the top right corner to USA (English).
        common_page = CommonPage(self.driver)

        #    Modal appears at bottom, click on accept Cookies
        common_page.accept_cookies()

        # Select language to USA
        common_page.select_locale()

        # 3. Click Find out more for “Foreign exchange solutions”
        home_page = HomePage(self.driver)
        home_page.click_foreign_exchange_solution()

        #    Validate if you have arrived on the page
        home_page.verify_title()  # TBD just to inform the verification failure

        # 4. Search for the word “international payments” using the search box
        common_page.search(self.test_data["test_question2"]["string_to_be_searched"])

        # 5. Validate if you have arrived on the result page
        search_page = SearchPage(self.driver)
        search_page.verify_title()  # TBD just to inform the verification failure

        # 6. Validate that each article in the list displays a link that starts with https://www.moneycorp.com/en-us/
        assert search_page.verify_links(self.test_data["test_question2"]["article_url_prefix"])

        # Delay added at last just for demo purpose
        time.sleep(5)

        # We can include following components if required and have sufficient time:
        # logging module
        # reporting module
        # configuration reader class
        # marker
        # locator management class
        # test data management class