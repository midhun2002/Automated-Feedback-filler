from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(
    executable_path='E:\\chromedriver_win32\\chromedriver.exe')

EMAIL = "sheik_1901cs53@iitp.ac.in"
PASSWORD = "9390262413@Sk"
LIST = ['90', 'explains concepts clearly', 'Nothing']


def login():
    driver.find_element_by_xpath(
        '//*[@id="mail_server_list"]/input[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="user_login"]').send_keys(EMAIL)
    driver.find_element_by_xpath(
        '//*[@id="user_password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="btn"]').click()
    return


def opinion():
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/input').send_keys(LIST[0])
    selects_container = driver.find_element_by_xpath(
        '/html/body/div/div[2]')
    selects = selects_container.find_elements_by_tag_name('select')
    for i in range(len(selects)):
        select = Select(driver.find_element_by_id(i+1))
        size = len(select.options)
        if(size >= 5):
            select.select_by_value('5')
        else:
            select.select_by_value('10')
    driver.find_element_by_xpath('//*[@id="strength"]').send_keys(LIST[1])
    driver.find_element_by_xpath('//*[@id="weakness"]').send_keys(LIST[2])
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[2]/button').click()
    return


driver.get('http://172.16.26.43/feedbackIITP/index.php')
login()
driver.implicitly_wait(8)
time.sleep(2)
courses_container = driver.find_element_by_xpath('/html/body/div/div[2]')
courses = courses_container.find_elements_by_tag_name("div")
homeUrl = driver.current_url
for i in range(len(courses)):
    course = driver.find_element_by_xpath(
        '/html/body/div/div[2]/div['+str(i+1)+']')
    course.click()
    time.sleep(2)
    prof_container = driver.find_element_by_xpath('/html/body/div/div[2]')
    time.sleep(2)
    prof = prof_container.find_elements_by_tag_name("div")
    for i in range(len(prof)):
        path = '/html/body/div/div[2]/div'
        if(len(prof) > 1):
            path += '['+str(i+1)+']'
        professor = driver.find_element_by_xpath(path)
        professor.click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="course_code"]').click()
        time.sleep(2)
        opinion()
        driver.back()
        time.sleep(2)
        driver.back()
        driver.implicitly_wait(5)
    driver.get(homeUrl)
    driver.implicitly_wait(5)

driver.implicitly_wait(5)
driver.quit()
