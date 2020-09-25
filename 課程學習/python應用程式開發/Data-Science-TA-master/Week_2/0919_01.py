
# from selenium import webdriver
# imdb_home = "http://www.google.com"
# driver = webdriver.Firefox(executable_path="geckodriver.exe") # Use Firefox
# driver.get(imdb_home)


from selenium import webdriver
imdb_home = "https://drive.google.com/drive/u/0/folders/1FppKV9NLrDutKv27EoZPnZaSUfGR67nY"
driver = webdriver.Chrome(executable_path="chromedriver.exe") # Use Firefox
driver.get(imdb_home)