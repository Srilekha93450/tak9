from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the path to your WebDriver executable
EDGE_DRIVER_PATH = r'C:\Users\WELCOME\Downloads\edgedriver_win64\msedgedriver.exe'

# URL and login credentials
url = 'https://www.saucedemo.com/'
username = 'standard_user'
password = 'secret_sauce'

# Initialize Microsoft Edge WebDriver
edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=edge_service, options=edge_options)

try:
    # Open the URL
    driver.get(url)
    
    # Wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    # Find username and password fields, and login button
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    
    # Enter username and password, then click login
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
    # Wait for the page to load after login (adjust time as needed)
    WebDriverWait(driver, 10).until(EC.title_contains('Swag Labs'))
    
    # Fetch and print the title of the webpage
    print("Title of the webpage:", driver.title)
    
    # Fetch and print the current URL of the webpage
    current_url = driver.current_url
    print("Current URL of the webpage:", current_url)
    
    # Extract the entire contents of the webpage
    page_source = driver.page_source
    
    # Save the contents to a text file
    with open('Webpage_task_11.txt', 'w', encoding='utf-8') as file:
        file.write(page_source)
    
    print("Webpage contents saved to Webpage_task_11.txt")

finally:
    # Close the browser window
    driver.quit()
