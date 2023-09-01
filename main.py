from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from email.message import EmailMessage
import random
import ssl
import smtplib

def sendEmail(accounts):
    apppass = 'gmail app password'
    email_sender = 'sender@gmail.com'
    email_password =  apppass
    email_receiver = 'receiver@gmail.com'
    subject = 'Punch fail!!!'
    bodyTxt = 'Failed accounts: ' + str(accounts)
    body = bodyTxt
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
        smtp.login(user=email_sender, password=email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return 0


def punchInOut(usernanme, password, chr_driver, delayLevels): 

    # Login
    sleep(delayLevels)
    chr_driver.find_element(By.ID, 'username').send_keys(usernanme)
    chr_driver.find_element(By.ID, 'password').send_keys(password)
    chr_driver.find_element(By.ID, 'submit-btn').click()
    sleep(delayLevels)
    print('Login -- OK')
    # Navigate to the punchInOut page
    
    driver.get("https://blueprint.cyberlogitec.com.vn/UI_TAT_028")
    sleep(delayLevels)

    #Punch
    chr_driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/button').click()
    sleep(delayLevels) 
    print('Punch -- OK')

    chr_driver.quit()

def launchBrowser():
    
    # chr_options = Options()
    chr_options = webdriver.ChromeOptions() 
    chr_options.add_argument("--headless=new")
    chr_options.add_argument("--window-size=1920,1080")
    chr_options.add_argument("--disable-extensions")
    chr_options.add_argument("--proxy-server='direct://'")
    chr_options.add_argument("--proxy-bypass-list=*")
    chr_options.add_argument("--start-maximized")
    chr_options.add_argument('--headless')
    chr_options.add_argument('--disable-gpu')
    chr_options.add_argument('--disable-dev-shm-usage')
    chr_options.add_argument('--no-sandbox')
    chr_options.add_argument('--ignore-certificate-errors')
    chr_driver = webdriver.Chrome( options=chr_options)
    chr_driver.get("https://blueprint.cyberlogitec.com.vn/")

    return chr_driver

delayLevels = 5
punchFails = []
accounts = [
    # ['admin', '1111'],
]
# Do punch
for index, account in enumerate(accounts): 
    try:
        driver = launchBrowser()
        punchInOut(account[0], account[1], driver, delayLevels)
        randomDelay = random.randint(0, 2)
        sleep(randomDelay)
    except:
        punchFails.append(account)
        print("Punch fail!!! --> account: ", account[0])

# Retry punch for punch fail accounts
for i in range(2): 
    if (len(punchFails)>0): 
        for account in punchFails: 
            try:
                # print(account[0], account[1])
                driver = launchBrowser()
                punchInOut(account[0], account[1], driver)
                randomDelay = random.randint(0, 2)
                sleep(randomDelay*60)
            except:
                print("Punch fail!!! --> account: ", account[0])
# Send Mail if punch fail
if (len(punchFails)>0):
    sendEmail(punchFails)


