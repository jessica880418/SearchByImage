import unittest
from selenium import webdriver
import page

class Search(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_extension("/Users/jessica/Downloads/google-access-helper.crx")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://images.wjbaike.site/imghp')

    # Load the main page. In this case the home page of Google.
    def test_search_by_image(self):
        main_page = page.MainPage(self.driver)

    # Check google main page is indeed loaded.
        assert main_page.is_title_matches()
    # Set the image to search
        main_page.click_image_button()

        image_url = 'http://i0.hdslb.com/bfs/article/3e914a016057a47ae4af8ee9ba33cd48f5294638.jpg'
        image_content = ["dog", "puppy"]
        main_page.input_imageurl_andgo(image_url)

        search_results_page = page.SearchResultsPage(self.driver)

    # Verifies that the results return
        assert search_results_page.is_results_found()

    # Visit the configurable result
        VISIT_RESULT = 3
        search_results_page.visit(VISIT_RESULT)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


