from django.shortcuts import render
from .find_profile import get_all_data
from selenium import webdriver
from selenium.webdriver.remote.command import Command
from django.shortcuts import redirect
from .forms import ProfileForm
import json

profile_data_path = r"C:\Users\Thej Venkat\Desktop\Projects\LinkedIn Profile Displayer\linkedin_profile_displayer\profile_data"

def view_profile(request, url):
    url = 'https://www.linkedin.com/in/' + url
    profile = get_all_data(url, driver)
    # Convert profile dict to json and save it to a file in profile_data_path
    try:
        with open(profile_data_path + '\\' + url.split('/')[-1] + '.json', 'w') as f:
            json.dump(profile, f)
    except:
        pass
    
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
    try:
        driver.quit()
    except:
        pass
    driver = None
    options = None
    return render(request, 'recruiter_logout.html')

def home(request):
    return render(request, 'home.html')

def profile_input(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url'].split('/')[-1]
            return redirect('profile_view', url=url)
    else:
        form = ProfileForm()
    return render(request, 'profile_input.html', {'form': form})
