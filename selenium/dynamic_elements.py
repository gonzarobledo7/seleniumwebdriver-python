import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= "C:\\Users\\Usuario\\Desktop\\selenium-python\\chromedriver.exe")
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Disappearing Elements")

    def test_name_elements(self):
        driver = self.driver

        #creamos una lista vacia
        options = []
        menu = 5    #menu con valores por defecto
        tries = 1       #cantidad de intentos que le tomo a selenium

        while len(options) < 5:     #medimos la long de opciones
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number{i + 1} is NOT FOUND')
                    tries + 1
                    driver.refresh()
        print(f'Finished in {tries} tries')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()