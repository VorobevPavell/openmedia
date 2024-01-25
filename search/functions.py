import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By


def search_vehicle_info(search_type: str, search_value: str):
    try:
        result_list = []
        options = wd.ChromeOptions()
        options.add_argument('--headless')
        browser = wd.Chrome(options=options)
        url = "https://vin01.ru/"
        browser.get(url)

        if search_type == "num_plate":
            search_field = browser.find_element(By.ID, "num")
            search_field.send_keys(search_value)
            browser.find_element(By.ID, 'searchByGosNumberButton').click()
        elif search_type == "vin":
            browser.find_element(By.ID, "vinToggleButton").click()
            search_field = browser.find_element(By.ID, "vinNumber")
            time.sleep(4)
            search_field.send_keys(search_value)
            browser.find_element(By.ID, 'searchByVinNumberButton').click()


        time.sleep(3)

        get_check_btn = browser.find_element(By.ID, "getCheckButton")
        get_check_btn.click()
        time.sleep(3)

        info = browser.find_element(By.ID, "modal-body")
        result_list.append(info.text)

        dropdown = browser.find_element(By.ID, "checkType")
        dropdown.click()

        option_value = "taxi"
        option = browser.find_element(By.XPATH, f"//option[@value='{option_value}']")
        option.click()
        get_check_btn.click()

        time.sleep(3)
        was_in_taxi = browser.find_element(By.CLASS_NAME, 'alert')
        result_list.append(was_in_taxi.text)
        browser.close()
        browser.quit()
        return result_list
    except Exception:
        print(f"Произошла ошибка")
        search_vehicle_info(search_type, search_value)
