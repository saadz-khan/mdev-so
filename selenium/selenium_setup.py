from selenium.webdriver.common.action_chains import ActionChains

from fake_useragent.utils import get
from selenium import webdriver
from fake_useragent import UserAgent
import os
import wget
import pickle
import zipfile
#from selenium.webdriver.common.proxy import Proxy, ProxyType
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

def extract_chrome_version(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return(google_version.strip())
    except TypeError:
        return


def selenium_setup():

	# Add Random delays but less than some amount of time so that you go untracked and unnoticed.
	"""
	Selenium setup with proper argument setup for chrome webdriver
	Args:
	None

	Returns:
	webdriver object (Chrome or Firefox) 
	For firefox uncomment the code below at the end

	"""
		
	"""	Proxy Snippet
	ip_port = '24.106.221.230:53281'
	proxy = Proxy()
	proxy.proxy_type = ProxyType.MANUAL
	proxy.http_proxy = ip_port
	proxy.ssl_proxy = ip_port
	capabilities = webdriver.DesiredCapabilities.CHROME
	proxy.add_to_capabilities(capabilities)
	"""
	options = webdriver.ChromeOptions()
	
	# Argument setups for the chrome driver
	#ua = UserAgent()
	#userAgent = ua.chrome
	#options.add_argument(userAgent)

	options.add_argument("window-size=1280,800")
	options.add_experimental_option("prefs", {
		"profile.default_content_setting_values.notifications": 1 
		})	
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-infobars')
	options.add_argument('--disable-gpu')
	options.add_experimental_option('useAutomationExtension', False)
	options.add_experimental_option('excludeSwitches', ['enable-logging',"enable-automation"])
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--disable-blink-features=AutomationControlled')
	options.add_extension('./ad-block.crx')
	
	try:	
		driver = webdriver.Chrome(executable_path='./chromedriver.exe' ,options=options, desired_capabilities=capabilities)
		driver.delete_all_cookies()
		driver.create_options()
	except:
		stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
		output = stream.read()
		chrome_version = extract_chrome_version(output)

		# build the download url
		download_url = "https://chromedriver.storage.googleapis.com/" + chrome_version +"/chromedriver_win32.zip"

		# download the zip file using the url built above
		latest_driver_zip = wget.download(download_url,'./chromedriver.zip')

		# extract the zip file
		with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
			zip_ref.extractall() # you can specify the destination folder path here
		
		# delete the zip file downloaded above
		os.remove(latest_driver_zip)
		driver = webdriver.Chrome(executable_path='./chromedriver.exe' ,options=options)
		driver.delete_all_cookies()
		driver.create_options()


	"""For Firefox webdriver use this snippet "uncomment it out"
	Firefox profile for the neccessary for download the files

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList",2)
	profile.set_preference("browser.download.manager.showWhenStarting",False)
	profile.set_preference("browser.download.dir", getcwd())
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	driver = webdriver.Firefox(executable_path='<Add_Path>', firefox_profile =profile
	"""
	return driver

	
def forbes_links(driver, total):
	links = []
	for item in range(total):
		element = driver.find_element_by_xpath(f'/html/body/div[1]/main/div[1]/div[1]/div[4]/div/article[{item+1}]/div[1]/h3/a')
		links.append(element.get_attribute('href'))
	return links

def load_more(driver):
	element = driver.find_element_by_xpath("/html/body/div[1]/main/div[1]/div[1]/div[5]")
	actions = ActionChains(driver)
	actions.move_to_element_with_offset(element, 75, 5)
	actions.click()
	actions.move_to_element(element).perform()


def save_cookie(driver):
	#store cookies from current session
	pickle.dump(driver.get_cookies(), open('cookie_file.pkl', 'wb'))


def load_cookie(driver):
	#load cookies from a previous session
	cookies = pickle.load('./cookie_file.pkl', 'rb')
	for cookie in cookies:
		driver.add_cookie(cookie)


def main():
	driver = selenium_setup()
	driver.get('https://www.forbes.com/search/?q=Bitcoin&sh=62585f79279f')
	counter = 0
	times = 10

	for t in range(times):
		load_more(driver)
		driver.implicitly_wait(3)
	links = forbes_links(driver, 100)
	with open('link.txt', 'w') as f:
		for link in links:
			f.write(link)
			f.write('\n')

	
if __name__== "__main__" :
	main()


"""
Bypassing Google Recaptcha V2 Using 2Captcha

import requests
import time
from selenium import webdriver

siteKey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
apiKey = "Place Your 2Captcha Site key here"
pageUrl = "https://google.com/recaptcha/api2/demo"

form = {"method": "userrecaptcha",
	"googlekey": site_key,
	"key": apiKey,
	"pageurl": pageUrl,
	"json": 1}
response = requests.post('http://2captcha.com/in.php', data=form)
requestId = response.json()['request']

url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
status = 0

while not status:
	res = requests.get(url)
	if res.json()['status']==0:
		# Response is not ready
		time.sleep(3)
	else:
		# Response is ready
		requ = res.json()['request']

		# Open the Website with form using Selenium
		driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
		driver.get(pageurl)

		# Place the the request id received into the HTML of the Captcha
		js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
		driver.execute_script(js)

		# Click submit button
		driver.find_element_by_id("recaptcha-demo-submit").submit()
		status = 1
                     

"""


"""
!pip install undetected_chromedriver
import undetected_chromedriver.v2 as uc
options = uc.ChromeOptions()

# setting profile
options.user_data_dir = "c:\\temp\\profile"

# another way to set profile is the below (which takes precedence if both variants are used
options.add_argument('--user-data-dir=c:\\temp\\profile2')

# just some options passing in to skip annoying popups
options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
driver = uc.Chrome(options=options)

with driver:
    driver.get('https://nowsecure.nl')  # known url using cloudflare's "under attack mode"

"""