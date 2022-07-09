from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import csv
import json
import requests



EMAIL = 'tech@adaveo.com'
PASSWORD = 'Adaveo123!'



def get_and_wait_element(browser, xpath, sec_wait=15):
    WebDriverWait(browser, sec_wait).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return browser.find_element(By.XPATH, xpath)



def get_and_wait_elements(browser, xpath, sec_wait=15):
    WebDriverWait(browser, sec_wait).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return browser.find_elements(By.XPATH, xpath)


def ini_browser():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    opts = Options()
    opts.add_argument("user-agent=" + USER_AGENT)
    s=Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=opts)
    return browser

browser = ini_browser()


# open the browser
browser.get('https://app.snov.io/login')
browser.maximize_window()


# %%

# login page
time.sleep(6)
email_text_box = get_and_wait_element(browser, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
email_text_box.click()

email_text_box_input = get_and_wait_element(browser, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[1]/input')
email_text_box_input.send_keys(EMAIL)

password_text_box = get_and_wait_element(browser, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
password_text_box.click()



password_text_box_input = get_and_wait_element(browser, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[2]/input')
password_text_box_input.send_keys(PASSWORD)


login_button = get_and_wait_element(browser, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/button')
login_button.click()

# %%

time.sleep(5)


#browser.get("https://app.snov.io/domain-search?name=ihousedesign.com&tab=emails")


domain_name = ""


link = "https://app.snov.io/domain-search?name=" + domain_name + "&tab=emails"

table_xpath = '/html/body/div[2]/main/div/div[2]/div[3]/div[3]/table/tbody/tr'

tablename_xpath = '/html/body/div[2]/main/div/div[2]/div[3]/div[4]/table/tbody/tr'

city_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]'

founded_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]'

industry_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]'

website_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[4]/div[2]/a'

sizeer_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]'

social_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/a/svg'


url = "http://samurai3.keenetic.link/csv/queue.php?check=1&limit=50"

r = requests.get(url)

urls = r.json()['list']['data']

print(urls)

domains = []

for link in urls:
	domains.append(link['url'])


lines = domains

#size = len(get_and_wait_elements(browser, table_xpath))

global allnames

global table_row

table_row = []

global size


for line in lines:
#	ln = line.strip(" ")

#	domain_name = ln	
#	allnames = []
#	link2 = "https://app.snov.io/domain-search?name=" + domain_name
#	time.sleep(10)
#	browser.get(link2)
#	try:
#		tablename_row = get_and_wait_elements(browser, tablename_xpath)
#	except:
#		pass
			
#	try:
#		for name in tablename_row:
#		allnames.append(name)
#	except:
#		pass
#	print(allnames)
	 
	 
	city_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]'
	founded_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]'
	industry_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]'
	website_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[4]/div[2]/a'
	sizeer_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]'
	social_xpath = '/html/body/div[2]/main/div/div[2]/div[2]/div[2]/div[3]/div[3]/div[2]/a/svg'
	ln = line.strip(" ")

	domain_name = ln
	

#	print(domain_name)
	link = "https://app.snov.io/domain-search?name=" + domain_name + "&tab=emails"
#	print(link)
	time.sleep(15)
	browser.get(link)
	time.sleep(5)
	path = '/home/eliander/Desktop'
	filename = "emails.csv"
	complete = os.path.join(path, filename)	
	browser.refresh()
	time.sleep(5)
	
	try:
		time.sleep(10)
		table_row = get_and_wait_elements(browser, table_xpath)
		city = get_and_wait_element(browser, city_xpath)
		founded = get_and_wait_element(browser, founded_xpath)
#		website = get_and_wait_element(browser, website_xpath)
		industry = get_and_wait_element(browser, industry_xpath)
		sizeer = get_and_wait_element(browser, sizeer_xpath)
		social = browser.find_element(by=By.CLASS_NAME, value="company__link").get_attribute("href")
		
	except:
		pass
	time.sleep(5)

		
	for row in table_row:
		list_data = []
		
		try:
#			print(row)
#			print(table_row)
#			print(len(table_row))
			domain_name1 = domain_name
			list_data.append(domain_name1)
			list_data.append(row.text)
			list_data.append(city.text)
			list_data.append(founded.text)
#			list_data.append(website.text)
			list_data.append(industry.text)
			list_data.append(sizeer.text)
			list_data.append(social)
			print(domain_name1)
			print(list_data)
			csvfile = open(complete, "a")
			csv_writer = csv.writer(csvfile)
			csv_writer.writerow(list_data)
			csvfile.close()
			list_data.clear()
			allnames.clear()

		except:
			pass

r = requests.get("http://salesrock.ddns.net:5006/emails")	
print(f"Status Code: {r.status_code}")
