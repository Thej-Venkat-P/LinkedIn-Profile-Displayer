from django.shortcuts import render
from .find_profile import get_all_data
from selenium import webdriver
from selenium.webdriver.remote.command import Command

def view_profile(request, url):
    url = 'https://www.linkedin.com/in/' + url
    profile = get_all_data(url, driver)
    return render(request, 'view_profile.html', {'profile': profile})

driver = None
options = None

def is_working():
    try:
        driver.execute(Command.STATUS)
        return True
    except:
        return False
        
def recruiter_login(request):
    global driver, options
    if not is_working():
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-logging')
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.linkedin.com/login')
        message = "Please login to your LinkedIn account"
    else:
        message = "You are already logged in"
    return render(request, 'recruiter_login.html', {'message': message})

def recruiter_logout(request):
    global driver, options
    driver.quit()
    driver = None
    options = None
    return render(request, 'recruiter_login.html')

def home(request):
    return render(request, 'home.html')