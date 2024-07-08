from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Data from Profile Page:
# Required data: Name, Tag Line, Profile Image, About, Languages, Experience, Education, Skills, Recommendations, Accomplishments, Interests
# Available Data: Name, Tag Line, Profile Image, About, Languages, Experience, Education, Certifications, Projects
# ExPass#@123
# Open the profile page
def open_profile_page(url):
    driver.get(url)
    print("\nOpened Profile Page")
    close_popup()

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
        name = driver.find_element(By.CLASS_NAME, 'top-card-layout__title').text
        return name
    except:
        return None

# Tag Line
def find_tag_line():
    try:
        tag_line = driver.find_element(By.CLASS_NAME, 'top-card-layout__headline').text
        return tag_line
    except:
        return None

# Profile Image
def find_profile_image():
    try:
        profile_image = driver.find_element(By.CLASS_NAME, 'top-card__profile-image').get_attribute('src')
        return profile_image
    except:
        return None

# About
def find_about():
    try:
        about = driver.find_element(By.CLASS_NAME, 'core-section-container__content').text
        return about
    except:
        return None

# Location
def find_location():
    try:
        location = driver.find_element(By.CLASS_NAME, 'not-first-middot').text
        return location[: -13].split(', ')
    except:
        return None

# Languages
def find_languages():
    try:
        languages = driver.find_element(By.CLASS_NAME, 'languages').text.split('\n')[1:]
        languages = [(languages[i], languages[i+1]) for i in range(0, len(languages), 2)]
        return languages
    except:
        return None

# Experience
def find_experience():
    try:
        experience_list = driver.find_element(By.CLASS_NAME, 'experience__list')
        # For each li in experience_list, get the data
        experience_list = experience_list.find_elements(By.TAG_NAME, 'li')
        experience_list = [exp.text for exp in experience_list]
        for i in range(len(experience_list)):
            experience_list[i] = experience_list[i].strip('Show more')
        return experience_list
    except:
        return None

# Education
def find_education():
    try:
        education_list = driver.find_element(By.CLASS_NAME, 'education__list')
        # For each li in education_list, get the data
        education_list = education_list.find_elements(By.TAG_NAME, 'li')
        education_list = [edu.text for edu in education_list]
        for i in range(len(education_list)):
            education_list[i] = education_list[i].strip('Show more')
        return education_list
    except:
        return None

# Certifications
def find_certifications():
    try:
        certifications_list = driver.find_element(By.CLASS_NAME, 'certifications')
        # For each li in certifications_list, get the data
        certifications_list = certifications_list.find_elements(By.TAG_NAME, 'li')
        certifications_list = [cert.text for cert in certifications_list]
        return certifications_list
    except:
        return None

# Projects
def find_projects():
    try:
        projects_list = driver.find_element(By.CLASS_NAME, 'projects')
        # For each li in projects_list, get the data
        projects_list = projects_list.find_elements(By.TAG_NAME, 'li')
        projects_list = [proj.text for proj in projects_list]
        return projects_list
    except:
        return None

# Close the driver
def close_driver():
    driver.quit()

def get_all_data(url, open_driver=None):
    global driver, options
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
        "projects": projects
    }
    print(profile)
    return profile

if __name__ == '__main__':
    url = 'https://www.linkedin.com/in/thej-venkat-purru-9941a6255/'

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--silent')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-logging')

    driver = webdriver.Chrome(options=options)
    
    open_profile_page(url)
    
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

    end = input("Press Enter to Exit\n")