from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest
import pdb

options = webdriver.ChromeOptions()

options.add_argument('--disable-notifications')
options.add_argument("start-maximized")

def send_email(driver):
    driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp0jwP1PVC_SvwlydeF5RWWOHFJGsU_Hd1mGRngfgBhClXU7E_ssBoknZ321-Bs8ab4cKI1iIQ&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S419911905%3A1701411309646255&theme=glif')
    time.sleep(5)

    email_input = driver.find_element(By.XPATH,'//*[@id="identifierId"]')
    email_input.send_keys('email')  
    time.sleep(5)

    next_button = driver.find_element(By.ID,'identifierNext')
    next_button.click()
    time.sleep(3)

    password_input = driver.find_element(By.NAME,'Passwd')
    password_input.send_keys('password')  

    login_button = driver.find_element(By.ID,'passwordNext')
    login_button.click()
    time.sleep(5)

    # Compose email
    compose_button = driver.find_element(By.XPATH,'/html/body/div[8]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div')
    compose_button.click()
    time.sleep(5)

    
    driver.find_element(By.XPATH, '//*[@id=":mh"]/div/div[3]/div/div/div/div/div').send_keys('email of receipients')
    #recipients_button.send_keys('')
    time.sleep(5)
    #to_input = driver.find_element(By.XPATH,'(//div[@peoplekit-id="pQPeT"])[1]')
    # recipients_button.send_keys('avic3929@gmail.com')  # Enter email of whom you want to send
    time.sleep(5)
    subject_input = driver.find_element(By.XPATH,'//*[@id=":n6"]')
    subject_input.send_keys('incubyte')

    body_input = driver.find_element(By.XPATH,'//*[@id=":f9"]')
    body_input.send_keys('QA test for incubyte')

    send_button = driver.find_element(By.XPATH,'//*[@id=":dp"]')
    send_button.click()
    time.sleep(5)

    # Assertion to verify the email was sent (you can improve this assertion)
    assert "Message sent" in driver.page_source

@pytest.fixture
def browser():
    driver = webdriver.Chrome(options=options)
    yield driver
    # driver.quit()


# Traditional style test case
def test_send_email(browser):
    send_email(browser)
