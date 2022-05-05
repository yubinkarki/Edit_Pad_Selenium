import time, json, unittest, objectpath
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Get_URL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Copy geckodriver in the path folder.
        self.driver.maximize_window()
        url = "https://www.editpad.org/"
        self.driver.get(url)
        self.driver.implicitly_wait(20)


    def test_url(self):
        driver = self.driver
        ok = driver.find_element(By.NAME, "text")
        ok.clear()

        with open('testdata.json', "r", encoding="utf8") as f:
            data = json.load(f)
            start = objectpath.Tree(data)
            result = tuple(start.execute('$..value'))  # Gets data from the "value" key.
        for i in result:
            ok.send_keys(i)
            ok.send_keys(Keys.RETURN)


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
