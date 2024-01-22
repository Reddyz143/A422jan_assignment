from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Task1:
    def __init__(self, url):
        self.url = url
        self.destanations = ["Bengaluru", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagpur", "Dubai"]
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    
    def get_details(self):
        driver = self.driver
        
        continue_button = driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
        continue_button.click()
        
        cities_elms = driver.find_elements(By.XPATH, "//*[@class='row cnt-schedule-table']/table/tbody/tr/td/div/span")
        status_elms = driver.find_elements(By.XPATH, "//*[@class='row cnt-schedule-table']/table/tbody/tr/td[@class='ng-binding']/span/parent::td")
        
        cities = [elm.text for elm in cities_elms]
        status = [elm.text for elm in status_elms]
        
        mapped_data = list(zip(cities, status))
        
        for city in self.destanations:
            for mapped_city, status in mapped_data:
                if city == mapped_city:
                    print(f'{city}: {status}')
                else:
                    print(f'{city}: data not available')
                    break
        
        driver.close()
        driver.quit()
        
        
if __name__ == '__main__':
    obj = Task1('https://www.flightradar24.com/data/airports/pnq')
    obj.get_details()