import unittest
import pathlib, os
from selenium import webdriver



def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()




class WebpageTests(unittest.TestCase):

    def test_title(self):
        # open web page
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")


    def test_inc_value(self):
        driver.get(file_uri("counter.html"))
        inc = driver.find_element_by_id("inc")
        inc.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "1")


    def test_dec_value(self):
        driver.get(file_uri("counter.html"))
        dec = driver.find_element_by_id("dec")
        dec.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "-1")
    
    def test_inc_multi(self):
        driver.get(file_uri("counter.html"))
        inc = driver.find_element_by_id("inc")
        for i in range(3):
            inc.click()
        self.assertEqual(driver.find_element_by_tag_name('h1').text, "3")





if __name__ == "__main__":
    unittest.main()