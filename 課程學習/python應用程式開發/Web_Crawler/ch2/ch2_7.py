# ch2_7.py
import csv
import time

time1 = time.localtime()
fn = str(time1.tm_hour) + str(time1.tm_min) + str(time1.tm_sec) + '.csv'
with open(fn, 'w', newline = '') as csvFile:    # 開啟csv檔案
    csvWriter = csv.writer(csvFile)             # 建立Writer物件   
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])
    time = time.localtime()


