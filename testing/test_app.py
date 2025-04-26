from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:5000") 
driver.maximize_window()

wait = WebDriverWait(driver, 10)

test_values = [
    14.2, 20.5, 90.2, 600.3, 0.1, 0.3, 0.4, 0.2, 0.2, 0.08,
    0.5, 1.2, 3.1, 20.0, 0.02, 0.03, 0.04, 0.03, 0.02, 0.001,
    16.2, 25.5, 110.2, 800.3, 0.15, 0.25, 0.35, 0.18, 0.25, 0.09
]

input_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))

for i, field in enumerate(input_fields):
    field.clear()
    field.send_keys(str(test_values[i]))

predict_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))


driver.execute_script("arguments[0].scrollIntoView();", predict_button)
time.sleep(1)  


predict_button.click()


time.sleep(3)

result = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text  
print("Prediction Result:", result)

driver.quit()
