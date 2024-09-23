from bs4 import BeautifulSoup
import requests
from IPython.display import HTML

page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0001.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rising-it-cities-and-their-impact-on-the-economy-environment-infrastructure-and-city-life-in-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0002.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/internet-demands-evolution-communication-impact-and-2035s-alternative-pathways/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0003.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-in-upcoming-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0004.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0005.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/the-rise-of-the-ott-platform-and-its-impact-on-the-entertainment-industry-by-2040/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0006.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/rise-of-cyber-crime-and-its-effects/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0007.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0008.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0009.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0010.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0011.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0012.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0013.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = Thetitle.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0014.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0015.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0016.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-chatbots-and-its-impact-on-customer-support-by-the-year-2040/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0017.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0018.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-does-marketing-influence-businesses-and-consumers/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content2 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

content3 = content2

# print(content3)

with open('blackassign0019.txt', 'w', encoding="utf-8") as file:
    file.write(Thetitle)
    file.write(content3)
    file.flush()
    file.close()

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0020.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/negative-effects-of-marketing-on-society/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0021.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-advertisement-marketing-affects-business/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0022.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rising-it-cities-will-impact-the-economy-environment-infrastructure-and-city-life-by-the-year-2035/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0023.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0024.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-electric-vehicles-and-its-impact-on-livelihood-by-2040/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0025.txt", "w", encoding="utf-8")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/rise-of-electric-vehicle-and-its-impact-on-livelihood-by-the-year-2040/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0026.txt", "w", encoding="utf-8")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0027.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/an-outlook-of-healthcare-by-the-year-2040-and-how-it-will-impact-human-lives/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0028.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"}).text

# content1 = content.find('div', attrs = {"class":"td-post-content tagdiv-type"}).text

# print(content)

file = open("blackassign0029.txt", "w")
file.write(Maintitle)
file.write(content)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0030.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0031.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0032.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0033.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0034.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0035.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------

# Webpage Not Working

# page_to_scrape = requests.get("https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/")

# soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# head = soup.find('header', attrs={'class':'td-post-title'})

# Thetitle =head.find('h1',attrs={'class':'entry-title'}).text

# print(Thetitle)

# content = soup.find('div', attrs={"class":"td-ss-main-content"})

# content1 = content.find('div', attrs = {"class":"td-post-content tagdiv-type"}).text

# print(content1)

# file = open("blackassign0036.txt","w")
# file.write(Thetitle)
# file.write(content1)
# file.flush()
# file.close


# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0037.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0038.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0039.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0040.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0041.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0042.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = Thetitle.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0043.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0044.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0045.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0046.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/evolution-of-advertising-industry/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0047.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0048.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------

# Page is not working

# page_to_scrape = requests.get("https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/")

# soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

# head = soup.find('header', attrs={'class':'td-post-title'})

# Thetitle =head.find('h1',attrs={'class':'entry-title'}).text

# print(Thetitle)

# content = soup.find('div', attrs={"class":"td-ss-main-content"})

# content1 = content.find('div', attrs = {"class":"td-post-content tagdiv-type"}).text

# print(content1)

# file = open("blackassign0049.txt","w")
# file.write(Thetitle)
# file.write(content1)
# file.flush()
# file.close


# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0050.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0051.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0052.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0053.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0054.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0055.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0056.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0057.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-we-forecast-future-technologies/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0058.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0059.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0060.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0061.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0062.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0063.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0064.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0065.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0066.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0067.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0068.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0069.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0070.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0071.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0072.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0073.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0074.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0075.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0076.txt", "w", encoding="utf-8")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0077.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0078.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0079.txt", "w", encoding="utf-8")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0080.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0081.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0082.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/human-rights-outlook/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = Thetitle.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0083.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'}).text

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0084.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0085.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0086.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0087.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0088.txt", "w", encoding="utf-8")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0089.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0090.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0091.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0092.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/travel-and-tourism-outlook/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0093.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0094.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0095.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0096.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0097.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get(
    "https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('header', attrs={'class': 'td-post-title'})

Thetitle = head.find('h1', attrs={'class': 'entry-title'}).text

print(Thetitle)

content = soup.find('div', attrs={"class": "td-ss-main-content"})

content1 = content.find('div', attrs={"class": "td-post-content tagdiv-type"}).text

# print(content1)

file = open("blackassign0098.txt", "w")
file.write(Thetitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0099.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close

# ------------Next URL--------------


page_to_scrape = requests.get("https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/")

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

head = soup.find('div', attrs={
    'class': 'td_block_wrap tdb_title tdi_122 tdb-single-title td-pb-border-top td_block_template_1'})

Thetitle = head.find('div', attrs={'class': 'tdb-block-inner td-fix-index'})

Maintitle = head.find('h1', attrs={'class': 'tdb-title-text'}).text

print(Maintitle)

content = soup.find('div', attrs={
    "class": "td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type"})

content1 = content.find('div', attrs={"class": "tdb-block-inner td-fix-index"}).text

# print(content1)

file = open("blackassign0100.txt", "w")
file.write(Maintitle)
file.write(content1)
file.flush()
file.close
