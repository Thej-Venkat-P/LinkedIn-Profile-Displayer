from time import sleep
# ExPass#@123
# https://www.linkedin.com/in/thej-venkat-purru-9941a6255
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Data from Profile Page:
# Required data: Name, Tag Line, Profile Image, About, Languages, Experience, Education, Skills, Recommendations, Accomplishments, Interests
# Available Data: Name, Tag Line, Profile Image, About, Languages, Experience, Education, Certifications, Projects

# Open the profile page
def open_profile_page(url):
    driver.get(url)
    sleep(3)
    print("\nOpened Profile Page")
    # close_popup()

# Close the login popup
def close_popup():
    elems = driver.find_elements(By.CLASS_NAME, 'contextual-sign-in-modal__modal-dismiss')
    for elem in elems:
        try:
            if elem.is_enabled() and elem.is_displayed():
                elem.click()
                print("Closed Login Popup")
                break
        except:
            pass 
    
# Name
def find_name():
    try:
        name = driver.find_element(By.CLASS_NAME, 'text-heading-xlarge').text
        return name
    except:
        return None

# Tag Line
def find_tag_line():
    try:
        tag_line = driver.find_element(By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]').text
        return tag_line
    except:
        return None

# Profile Image
def find_profile_image():
    try:
        profile_image = driver.find_element(By.CLASS_NAME, 'pv-top-card-profile-picture__image--show').get_attribute('src')
        return profile_image
    except:
        return None

# About
def find_about():
    try:
        about = driver.find_element(By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[2]/div[3]/div/div/div/span[1]').text
        return about
    except:
        return None
    
# Location
def find_location():
    try:
        location = driver.find_element(By.XPATH, '//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]').text
        return location.split(', ')
        
    except:
        return None

# Languages
def find_languages():
    try:
        driver.get(url+'/details/languages/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(2)
        languages = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        languages = [elem.text.split('\n')[::2] for elem in languages]
        return languages
        
    except:
        return None

# Experience
def find_experience():
    try:
        driver.get(url+'/details/experience/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(2)
        experience = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        experience = [elem.text.split('\n')[::2] for elem in experience]
        return experience
    except:
        return None

# Education
def find_education():
    try:
        driver.get(url+'/details/education/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(2)
        education = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        education = [elem.text.split('\n')[::2] for elem in education]
        return education
    except:
        return None

# Certifications
def find_certifications():
    try:
        driver.get(url+'/details/certifications/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(2)
        certifications = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        certifications = [elem.text.split('\n')[::2] for elem in certifications]
        return certifications
    except:
        return None

# Projects
def find_projects():
    try:
        driver.get(url+'/details/projects/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(2)
        projects = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        projects = [elem.text.split('\n')[::2] for elem in projects]
        return projects 
    except:
        return None

def find_skills():
    try:
        driver.get(url+'/details/skills/')
        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)
        skills = driver.find_elements(By.CLASS_NAME, 'pvs-list__paged-list-item')
        skills = [elem.text.split('\n')[0] for elem in skills]
        temp = []
        for elem in skills:
            if elem:
                temp.append(elem)
        skills = temp
        return skills
    except:
        return None

# Close the driver
def close_driver():
    driver.quit()

def get_all_data(curr_url, open_driver=None):
    global driver, options, url
    url = curr_url
    if not open_driver:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-logging')
        driver = webdriver.Chrome(options=options)
    else:
        driver = open_driver

    open_profile_page(url)
    
    name = find_name()
    tagline = find_tag_line()
    profile_image = find_profile_image()
    about = find_about()
    location = find_location()
    languages = find_languages()
    experience = find_experience()
    education = find_education()
    certifications = find_certifications()
    projects = find_projects()
    skills = find_skills()
    # close_driver()

    profile = {
        "url": url,
        "name": name,
        "tagline": tagline,
        "profile_image": profile_image,
        "about": about,
        "location": location,
        "languages": languages,
        "experience": experience,
        "education": education,
        "certifications": certifications,
        "projects": projects,
        "skills": skills
    }
    print(profile)
    return profile

if __name__ == '__main__':
    url = 'https://www.linkedin.com/in/thej-venkat-purru-9941a6255'

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--silent')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-logging')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.linkedin.com/login")
    cont = input("Input")
    open_profile_page(url)
    sleep(5)

    print()
    print("Data from Profile Page:")
    print()

    print("Name:")
    name = find_name()
    print(name)

    print()

    print("Tag Line:")
    tagline = find_tag_line()
    print(tagline)

    print()

    print("Profile Image:")
    profile_image = find_profile_image()
    print(profile_image)

    print()

    print("About:")
    about = find_about()
    print(about)

    print()

    print("Location:")
    location = find_location()
    print(location)

    print()

    print("Languages:")
    languages = find_languages()
    print(languages)

    print()

    print("Experience:")
    experience = find_experience()
    print(experience)

    print()

    print("Education:")
    education = find_education()
    print(education)

    print()

    print("Certifications:")
    certifications = find_certifications()
    print(certifications)

    print()

    print("Projects:")
    projects = find_projects()
    print(projects)

    print()
    
    print("Skills:")
    skills = find_skills()
    print(skills)
    
    print()

    end = input("Press Enter to Exit\n")