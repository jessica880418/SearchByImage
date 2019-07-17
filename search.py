import unittest
from selenium import webdriver
from page import MainPage, SearchResultsPage
import os


class Search(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://images.wjbaike.site/imghp')

    def test_search_by_image(self):

        main_page = MainPage(self.driver)

        # Check google main page is indeed loaded.
        assert main_page.is_title_matches()

        # Set the image to search
        main_page.click_image_button()

        image_url = 'http://i0.hdslb.com/bfs/article/3e914a016057a47ae4af8ee9ba33cd48f5294638.jpg'
        image_content = ["dog", "puppy", "puppies"]
        main_page.search_image_by_url(image_url)

        search_results_page = SearchResultsPage(self.driver)

        # Verifies that the results return and results're related to image content
        assert search_results_page.is_results_found()
        assert search_results_page.is_related_to(image_content)

        # Visit the configurable result
        configuration_file = open("configuration_file", 'r')
        line = configuration_file.readline().split("visit_result = ")
        visit_result = int(line[1])
        search_results_page.visit(visit_result)
        configuration_file.close()

        # Wait page to load and take screenshot
        search_results_page.wait_page()
        screenshot_file = os.path.join(os.path.curdir, 'third_result.png')
        self.driver.find_element_by_xpath("//body").screenshot(screenshot_file)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
