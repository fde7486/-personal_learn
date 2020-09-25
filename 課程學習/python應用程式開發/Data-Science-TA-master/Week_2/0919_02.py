from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# available since 2.4.0
from selenium.webdriver.support.ui import WebDriverWait
# available since 2.26.0
from selenium.webdriver.support import expected_conditions as EC
 
driver = webdriver.Firefox(executable_path="geckodriver.exe")
 
# 去 google
driver.get("http://www.google.com")

# 找到搜尋框
inputElement = driver.find_element_by_name("q")
 
# 搜尋框輸入字
inputElement.send_keys("逢甲大學")
 
# 提交
inputElement.submit()
 
try:
    # 直到標題有逢甲大學
    WebDriverWait(driver, 10).until(EC.title_contains("逢甲大學"))
    
    first_result_elem = driver.find_element_by_xpath("//div[@class='r']/a/h3[@class='LC20lb DKV0Md']")
    # 按下搜尋結果連結
    first_result_elem.click()
    
except TimeoutException:
    print('time out')

driver.close()