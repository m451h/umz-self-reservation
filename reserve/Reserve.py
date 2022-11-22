import time

import jdatetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

today = jdatetime.datetime.now().strftime("%Y/%m/%d")
tomorrow = (jdatetime.date.today() + jdatetime.timedelta(days=1)).strftime("%Y/%m/%d")

username = ""
password = ""
service = Service("/Users/m451h/Downloads/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://self.umz.ac.ir/")
driver.find_element("id", "username").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element(
    "xpath", "/html/body/div/div/div[2]/div/div/div[2]/div/form/div/button"
).click()


def todayFood(driver, today):
    driver.get("https://self.umz.ac.ir/#!/UserIndex")
    time.sleep(1)
    table = driver.find_element(
        "xpath", "/html/body/div[2]/div/section[2]/div/div/div[4]/div/div/div[3]/table"
    )
    time.sleep(1)
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        if today in row.text:
            print(row.text)


def nextDayFood(username, password, driver, tomorrow):
    driver.get("https://self.umz.ac.ir/#!/UserIndex")
    time.sleep(1)
    table = driver.find_element(
        "xpath", "/html/body/div[2]/div/section[2]/div/div/div[4]/div/div/div[3]/table"
    )
    time.sleep(1)
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        if tomorrow in row.text:
            print(row.text)


def thisWeekFood(username, password, driver, today):
    driver.get("https://self.umz.ac.ir/#!/UserIndex")
    time.sleep(1)
    table = driver.find_element(
        "xpath", "/html/body/div[2]/div/section[2]/div/div/div[4]/div/div/div[3]/table"
    )
    time.sleep(1)
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols[:5]:
            print(col.text)


def resNextWeek(driver):
    # driver.minimize_window()
    # time.sleep(1)    
    driver.get("https://self.umz.ac.ir/#!/Reservation")
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div/section[2]/div/div/div/div/div/div/div[3]/div[1]/div[2]/div/button[3]",
    ).click()#next week
    time.sleep(1)
    # FOR DAY = 0-7 DAYS FIND ELEMENT BY ID F"TAB_DAY{DAY}" for iterate through the days
    for day in range(2,5):
        meal = driver.find_element(By.ID, f"tab_day{day}")
        elements = meal.find_elements(By.ID, "selectFood")
        #print(len(element)) => 3
        for element in elements: 

            # SELECT FOOD
            drp = Select(element)
            food_options = drp.options
            for index, food in enumerate(food_options[1:], start=1):
                print(f"{index}_{food.text}") #doesn't show the breakfast options
            op = int(input(">>> "))
            drp.select_by_index(op) #cant be 1 when breakfast

            # IF YOU DONT WANT THIIS MEAL: OPTION == 0
            # if op != 0 : 

            # SELECT SELF
            element1 = meal.find_element(By.ID, "selectSelf")
            drp1 = Select(element1)
            self_options = drp1.options
            for index, sel in enumerate(self_options, start=1):
                print(f"{index}_{sel.text}")
            op1 = int(input(">>> "))
            drp1.select_by_index(op1 - 1)
    # driver.find_element("xpath", '//*[@id="tab_11"]/button').click()
    # time.sleep(1)
    # driver.find_element("xpath", '//*[@id="tab_21"]/div/button').click()
    # time.sleep(1)
            # elif op == 0:
            #     break

def resThisWeek(username, password):
    pass

def fCode():
    pass

def charge():
    pass

def notReservedAlert():
    pass

#todayFood(driver, today)
resNextWeek(driver)
driver.close()
