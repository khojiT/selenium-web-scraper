#It's khoji <a.khoji2001@gmail.com>
# * in this code means that you should put your individual information

#pip install bs4,selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#to use your default google chrome account (not Guest account) you should do that by this method
#To find path to your chrome profile data you need to type chrome://version/ into address bar . For ex. mine is displayed as C:\Users\pc\AppData\Local\Google\Chrome\User Data\Default, to use it in the script I had to exclude \Default\ so we end up with only C:\Users\pc\AppData\Local\Google\Chrome\User Data.
#Also if you want to have separate profile just for selenium: replace the path with any other path and if it doesn't exist on start up chrome will create new profile and directory for it.
#if you use default account you could customize that page and then run code
options = Options()
options.add_argument("user-data-dir=C:\\Users\\pc\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument(' --profile-directory=Profile 2') #to use an account that isn't default
driver = webdriver.Chrome(chrome_options=options)
url = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131F'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
#for scraping the text you want , go to that page press [ctrl + shift + I] and select that place then realize that 
r = soup.find_all('a', {'class': 'inst'})
l1 = []
for i in range(len(r)):
    if i % 2 ==0:
        l1 = l1 + [r[i].text]
print(l1)
