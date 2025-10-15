from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os,base64

driver = webdriver.Chrome()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/?p=cause_list/index/")

time.sleep(2)
print("Page loaded successfully!")

Select(driver.find_element(By.ID, "sess_state_code")).select_by_visible_text("Rajasthan")
time.sleep(1)
Select(driver.find_element(By.ID, "sess_dist_code")).select_by_visible_text("Jaipur District")
time.sleep(1)
Select(driver.find_element(By.ID, "court_complex_code")).select_by_visible_text("Jaipur District Court Complex")
time.sleep(1)


print("Enter Court Name and Cause List Date")
print("Enter the CAPTCHA manually")
time.sleep(30)

pdf_path = os.path.join(os.getcwd(),"cause_list.pdf")
pdf_data = driver.print_page()
pdf_bytes = base64.b64decode(pdf_data)

with open(pdf_path,"wb") as f:
    f.write(pdf_bytes)

print(f"PDF saved successfully at {pdf_path}")