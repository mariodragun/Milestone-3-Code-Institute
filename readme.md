# Quiz -  Milestone project 3 Code Institute



## Summary:

The purpose of the project is to build a site where users, can play the quiz, tracked their scores and also where admin can easily modify data base, add and delete users and questions.
This site allows users to play short general knowledge quiz.


### The project has the following sections:  

- Home page contains main image and navigation bar with access to quiz, login and register

- Login page contains username field, password filed and login button

- Register page contains fields: first name, last name, username, email, password confirm password and register button

- Quiz page contains quiz for play after user / admin has been logged in

- Settings page for changing user details and passwords 

- Admin page, only accessible  for Admin


## UX stories:
 
 ### Admin stories:

 - As an admin I would like to manage a smoothly functioning game 

 - As an admin I would like to be able to add new questions

 - As an admin I would like to add users and to delete them

 
 ### User stories:

 - As a user I would like to register and login easily and conveniently through a simple process

 - As a user I would like to play quiz where I can test my general knowledge 

 - As a user I would like to track my previous score

## Structure:

### Wireframes:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/Home%20page%20wireframe.JPG)

- [Home page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/home%20page%20wireframe%20mobile.JPG)

- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/login%20page%20wireframe.JPG)

- [Login page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/login%20page%20wireframe%20mobile.JPG)

- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/register%20page%20wireframe.JPG)

- [Register page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/register%20page%20wireframe%20mobile.JPG)

- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/admin%20page%20wireframe.JPG)

- [Admin page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/admin%20page%20mobile%20wireframe.JPG)

## Design and colors:

### Fonts:

- I used Roboto from, from Google Fonts

### Images:

- I downloaded Welcome image from [WallpaperAccess](https://wallpaperaccess.com/)

### Colors:

Navbar:
- navbar-dark bg-dark (for the nav): #212529

Quiz:
Completed:
- <i> tag (icon): #9ABC66
- card box shadows (on questions overview and completed): #DEDEDE

Accounts:
Login/Register:
- on card box shadow: #DEDEDE
- card button: rgb(104, 145, 162)


Bootstrap colors in use:
Navbar:
- on login and register: btn-outline-light me-2 class is used

403 Error page:
- Go Back button (btn-danger class) #dc3545

Alert messages (flash messages):
- alert-danger #842029
- alert-success #0f5132

Quiz questions:
- Submit button (btn-primary class) #0d6efd

Quiz overview:
- Start new quiz button (btn-secondary class) #5c636
- Continue button (btn-secondar classy) #5c636
 

### Design

- [Home Page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/home_page_image.JPG)

- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/login_page_image.JPG)

- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/quiz_page_image.JPG)

- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/register_page_image.JPG)

- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/settings_page_image.JPG)

- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/admin_page_image.JPG)

## Technology Used:

 - HTML5

 - CSS3

 - [Bootstarp5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

 - [Python](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/requirements.txt)

 

 ## Tools Used:

 - Visual code studio

 - Git pod

 - Github for repository hosting service

 - [Heroku](https://dashboard.heroku.com/apps) to deploy web application

 - [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2-de?utm_content=rlsapostreg&utm_source=google&utm_campaign=gs_emea_rlsamulti_search_brand_dsa_atlas_desktop_rlsa_postreg&utm_term=&utm_medium=cpc_paid_search&utm_ad=b&utm_ad_campaign_id=14412646473&gclid=EAIaIQobChMItZq0nt358gIVDpftCh3FhQRAEAAYASAAEgKGnfD_BwE) for database

 - [PEP8](http://pep8online.com/) online for validation of Python code 

 - [W3C](https://validator.w3.org/) for HTML validation

 - [Jigsaw](https://jigsaw.w3.org/css-validator/) for CSS validation

 - [Moqups](https://moqups.com/?gclid=CjwKCAjwyvaJBhBpEiwA8d38vAw9ErkdYKdVqJZL-V-eMhg-lKZ_nlq20ONlAebM8DizNLHLdp6UvxoCOd8QAvD_BwE) for wireframes

 ## Deployment:

### Project setup:

Github:

- Create a new repository on Git Hub using code institute`s template

- Change repository visibility

- Press green button to open project in git pod

- Create readme.md file and make initial commit

- Make regular commits after project change with quality description using commands: git add -A and git commit -m "message"

- Use git push command in terminal for code commits

MongoDB:

- Navigate to [MongoDB](https://account.mongodb.com/account/login?signedOut=true)

- Create account 

- Create data base

Heroku:

- Navigate to [Heroku](https://id.heroku.com/login)

- Register account 

- Press button New

- Select create a New App, enter the app name and select region

- Press Resource and connect with database


Deployment`s final steps:

- After registration of test users, change status of one of the users to [admin](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/deployment/admin_MongoDB.JPG)

- Create quiz questions




## Testing

Throughout the development of the project, I carried out testing. I used the Chrome Developer Tools consistently.
The application structure and mobile-first layout was tested on Google Chrome, Firefox and Safari.
The application was tested on the following smartphone devices: iPhone11, Google Pixel 3, 

### Functional testing:

- That all of the links are open smoothly

- That application is mobile responsive

- That user can get logged in

- That quiz can not be run before user is logged in

- That user needs to create account 

- That user name and e-mail must be unique

- That user name and password length must be between 10 and 150 characters 

- That e-mail must be in valid form

- That users and admin can change passwords and other account settings

- That admin can delete users

- That admin can delete, add and modify questions

- If someone write \admin\ in URL gets [error message](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/error_link.JPG)

- That user can continue with unfinished session 

- That finished session is inaccessible for players



#### Testing examples:

Google Chrome:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/home_page_chrome.JPG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/login_page_chrome.JPG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/register_page_chrome.JPG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/quiz_page_chrome.JPG)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/settings_page_chrome.JPG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/admin_page_chrome.JPG)

Firefox:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/home_page_firefox.JPG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/login_page_firefox.JPG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/register_page_firefox.JPG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/quiz_page_firefox.JPG)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/settings_page_firefox.JPG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/admin_page_firefox.JPG)

Safari / mobile phone:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/home_page_mobile.PNG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/login_page_mobile.PNG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/register_page_mobile.PNG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/quiz_page_%20mobile.jpg)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/settings_page_mobile.PNG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/admin_page_mobile.PNG)

### Validation tests:

HTML:
- [Home page](https://ms3-mario.herokuapp.com/)------[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/home_page_html_validation.JPG)

- [Quiz page](https://ms3-mario.herokuapp.com/login/)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/quiz_page_html.JPG)

- [Quiz page, user logged](https://ms3-mario.herokuapp.com/quiz/)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/quiz_page_html_user.JPG)

- [Register page](https://ms3-mario.herokuapp.com/register/)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/register_page_html.JPG)

- [Login page](https://ms3-mario.herokuapp.com/login/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/login_page_html.JPG)

- [Settings page, user logged](https://ms3-mario.herokuapp.com/settings/)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/settings_page_html.JPG)

- [Admin page, admin logged](https://ms3-mario.herokuapp.com/admin/)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/admin_page_html.JPG)


Python:

- [__init__.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/__init__.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_init.JPG)

- [admin.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/admin.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_admin.JPG)

- [db.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/db.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_db.JPG)

- [forms.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/forms.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_forms.JPG)

- [helpers.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/helpers.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_helpers.JPG)

- [models.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/models.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_models.JPG)

- [views.py](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/views.py)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/python/pep8_views.JPG)

CSS: 

- [CSS/style.css](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/style.css)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/styel_jigsaw.JPG)

- [CSS/home.css](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/home.css)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/home_css_jigsaw.JPG)

- [CSS/quiz/style](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/quiz/style.css))-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/styel_jigsaw.JPG)

- [CSS/quiz/common/errors](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/common/error.css)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/error_css_jigsaw.JPG)

- [CSS/quiz/accounts/auth](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/accounts/auth.css)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/auth_css_jigsaw.JPG)

- [CSS/quiz/accounts/settings](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/quiz/static/css/accounts/settings.css)-----[test result](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css/setting_css_jigsaw.JPG)


## Conclusion:
This project was built only for educational purpose and won`t be in commercial use