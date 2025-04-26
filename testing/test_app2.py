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


benign_values = [
    9.0, 15.0, 60.0, 300.0, 0.08, 0.12, 0.15, 0.07, 0.14, 0.06,
    0.3, 0.5, 1.2, 10.0, 0.01, 0.02, 0.03, 0.01, 0.02, 0.001,
    11.0, 18.0, 75.0, 450.0, 0.1, 0.15, 0.2, 0.08, 0.1, 0.07
]


input_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))

for i, field in enumerate(input_fields):
    field.clear()
    field.send_keys(str(benign_values[i]))


predict_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))


driver.execute_script("arguments[0].scrollIntoView();", predict_button)
time.sleep(1)  
predict_button.click()


result = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text  
print("Prediction Result:", result)

assert "Cancer Not Detected" in result, "Test Failed: Expected 'Cancer Not Detected' but got different output."

print("✅ Test Passed: Cancer Not Detected")


driver.quit()
