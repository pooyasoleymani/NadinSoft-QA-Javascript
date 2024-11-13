from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

filepath = os.path.realpath('index.html')

#------------------------------------------------------------------------------
# for linux servises
# service = Service(executable_path='/snap/bin/firefox.geckodriver')
# driver = webdriver.Firefox(service=service)
#------------------------------------------------------------------------------
#for windows servise
servise = Service(executable_path='webdriver/chromedriver')
driver = webdriver.Chrome(service=servise)

driver.get('file:///' + filepath )


def add_task(task_text):
    task_input = driver.find_element(By.ID, "taskInput")
    task_input.send_keys(task_text)
    add_button = driver.find_element(By.XPATH, "//button[text()='Add']")
    add_button.click()

def complete_task(task_text):
    tasks = driver.find_elements(By.XPATH, "//li")
    for task in tasks:
        if task_text in task.text:
            done = task.find_element(By.CLASS_NAME, 'done-btn')
            done.click()
            break

def delete_task(task_text):
    tasks = driver.find_elements(By.XPATH, "//li")
    for task in tasks:
        if task_text in task.text:
            delete_button = task.find_element(By.CLASS_NAME, "delete-btn")
            delete_button.click()
            break

add_task("Task 1")
add_task("Task 2")
add_task("Task 3")

complete_task("Task 2")
delete_task("Task 1")
delete_task("Task 3")

time.sleep(5)
driver.quit()

