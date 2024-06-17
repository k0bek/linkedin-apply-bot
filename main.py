from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3936539326&distance=25&f_AL=true&geoId=105072130&keywords=Java&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

login_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login_button.click()

email_input = driver.find_element(By.ID, 'username')
email_input.send_keys(os.getenv('EMAIL'))

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(os.getenv('PASSWORD'))

login_button = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
login_button.click()

time.sleep(2)

job_cards = driver.find_elements(By.CLASS_NAME, 'job-card-container__link')

for job_card in job_cards:
    job_card.click()
    time.sleep(1)

    try:
        fast_apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        fast_apply_btn.click()

        apply_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
        if apply_button.text == "Dalej":
            quit_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--2')
            quit_button.click()
            delete_button = driver.find_element(By.CSS_SELECTOR, 'button[data-control-name="discard_application_confirm_btn"]')
            delete_button.click()
        else:
            number_input = driver.find_element(By.CLASS_NAME, 'artdeco-text-input--input')
            number_input.send_keys(123456789)
            apply_button.click()
            time.sleep(1)
            no_button = driver.find_element(By.CLASS_NAME, 'artdeco-button')
            no_button.click()
            time.sleep(3)

    except Exception as e:
        print(f"Nie udało się zastosować do oferty: {e}")

    time.sleep(2)

driver.quit()
