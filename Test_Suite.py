import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    
    def test_01_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        #self.assertIn("Python", driver.title)
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("python")
        sleep(5)
        elem.send_keys(Keys.RETURN)
        sleep(5)
        assert "No results found." not in driver.page_source
        # self.driver.quit()

    
    def test_02_search_by_name(self):
        driver = self.driver
        driver.get("http://www.python.org")
        sleep(5)
        elem = driver.find_element_by_name("q")
        elem.send_keys("qython")
        sleep(5)
        elem.send_keys(Keys.RETURN)
        sleep(5)
        assert "No results found." not in driver.page_source
        # self.driver.quit()

        # get the search textbox
        # self.search_field = self.driver.find_element_by_name("q")
        # # enter search keyword and submit
        # self.search_field.send_keys("Python class")
        # self.search_field.submit()
        # #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        # list_new = self.driver.find_elements_by_class_name("r")
        # self.assertEqual(10, len(list_new))
     
    def tear_down(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()