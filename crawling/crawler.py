import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

def executeTest():
    global driver
    driver.get('https://scholar.google.com/citations?hl=ko&user=d5u7NnAAAAAJ&view_op=list_works&sortby=pubdate')
    time.sleep(10)
    
    # getting more data 
    for _ in range(2):
        element = driver.find_element_by_css_selector("button#gsc_bpf_more")
        element.click()
        time.sleep(10)
    

    title_data = driver.find_elements_by_css_selector('#gsc_a_b > tr > td.gsc_a_t > a') #tr.gsc_a_tr > td.gsc_a_t> a.gsc_a_t
    writer_data = driver.find_elements_by_css_selector('#gsc_a_b > tr > td.gsc_a_t > div:nth-child(2)')
    workshop_data = driver.find_elements_by_css_selector('#gsc_a_b > tr > td.gsc_a_t > div:nth-child(3)')
    year_data =  driver.find_elements_by_css_selector('#gsc_a_b > tr > td.gsc_a_y > span')
    
    
    total = len(title_data)
    print(len(workshop_data), len(writer_data), len(year_data))
    

    f = open('crawled_data.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    header_list = ['year','title','writer','ws']
    wr.writerow(header_list)
    
    for i in range(total):
        row = [year_data[i].text, title_data[i].text, writer_data[i].text, workshop_data[i].text]
        if len(row[0])==0:
             continue
        wr.writerow(row)

    f.close()

def startWebDriver():
    global driver
    options = Options()
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=options, executable_path="/Users/heeju/Desktop/program/chromedriver")
    

    

if __name__ == "__main__":
    startWebDriver()
    executeTest()
    driver.quit()
    
'''

dr.maximize_window()
dr.get("http://www.nytimes.com/column/corner-office")

btn = dr.find_element_by_css_selector("button.load-more-button")
btn.click()

print( len(dr.find_elements_by_xpath("//h2[@class='headline']")))
dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print( len(dr.find_elements_by_xpath("//h2[@class='headline']")))


with requests.Session() as session:
    html = session.post("https://scholar.google.com/citations?hl=ko&user=d5u7NnAAAAAJ&view_op=list_works&sortby=pubdate", data={'start':1})
    soup = BeautifulSoup(html.text, "html.parser")
    rows = soup.select('tr.gsc_a_tr > td.gsc_a_t> a.gsc_a_at')
    print([i.text for i in rows])
    print(len(rows))

'''