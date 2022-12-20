<!-- Heading -->

# sonicetones - [Live link](https://sonictones-pp4.herokuapp.com/)

_On sonicetones you will find reviews of the latest and greatest new music releases. Whether you are a casual listener or a die-hard music fan, I hope that you will find something here that resonates with you._

sonictones is a fully responsive music blog website, It is a place where users can sign up and engage in conversations about new music. They also have the ability to like posts and bookmark blog posts for later.

<!-- Responsive Image -->

## User Experience
### User Stories

__As an unregistered user:__

-  _I can view a list of all blog posts so that I can get a overview of all the blogs posts._

- _I can search for blog posts by keywords so that I can find relevant content quickly._

- _I can view comments on a specific post so that I can see the conversation about that specific post._

- _I can register an account so that I can comment and like posts._


__As an registered user:__

- _I can log in so that I can use my role specific features._

- _I can log out from my account so that I can keep my information secure and prevent unauthorized access to my account._

- _I can create comments on a post so that I can share my thoughts with others._

- _I can like or unlike a post so that can give feedback on a post._

- _I can bookmark blog posts so that I can save them for later and easily access them again._

__As an administrator:__

- _I can create draft posts so that I can complete the content of the blog post later._

- _I can create, read, update and delete specific posts so that I can manage the content of the blog._

- _I can approve or disapprove comments so that I have the option to decide if a comment should be visible or not._


## Design
### Color Scheme
The main colors used throughout the blog were black, white, and grey. This creates a clean and easy-to-navigate look for the blog. The use of black for the navbar helps to create a cohesive and unified look, while the use of white for the text and buttons makes it easy for readers to find what they need. The use of grey adds a sense of sophistication and professionalism to the design.

### Typography
The main font used is called 'Playfair Display'
> Playfair is a transitional font from the 18th century that features high-contrast, delicate hairlines. It was influenced by the change from broad nib quills to pointed steel pens and advances in printing technology.

## Wireframes
The first sketched wireframes of the blog can be seen below. The final look of the blog ended up being very close to these mockups.

__[Wireframes](./readme_files/Wireframes/)__

As the project progressed, some elements was updated. However, I think that the layout changes were not so drastic that they needed new wireframes to be designed.

Under the wireframing process I gathered ideas for the design and features from the music reviews website called [Pitchfork](https://pitchfork.com/reviews/albums/).
The wireframes were made in Figma.

## Agile
The project management tool used was GitHub project board.

<!-- Add Agile github board picture here -->

Throughout the development process, the stories were constantly updated according to the progress and pushed into the right cloumn.


## Database ERD
<!-- databas image here -->
-- 
-- 
### Database

 - The database is a PostgreSQL database, hosted on [ElephantSQL](https://www.elephantsql.com/).

- I used [DBeaver](https://dbeaver.io/) as an extra tool to have better overview of the database.

## Data Models

### Post model
This model represents a blog post. Which contains the following fields -

- Title: a CharField that stores the title of the blog post.

- Slug: a SlugField that stores the slug for the blog post(which is a URL-friendly version of the title).

- Author: a ForeignKey field that references the User model and represents the user who wrote the blog post.

- Updated_on: a DateTimeField that stores the date and time when the blog post was last updated.

- Content: a TextField that stores the content of the blog post.

- Featured_image: a CloudinaryField that stores the featured image for the blog post.

- Excerpt: a TextField that stores an excerpt of the blog post.

- Created_on: a DateTimeField that stores the date and time when the blog post was created.

- Status: an IntegerField that stores the status of the blog post (draft or published).

- Likes: a ManyToManyField that represents the users who have liked the blog post.

- Bookmarks: a ManyToManyField that represents the users who have bookmarked the blog post.

### Comment Model
This Model represents a comment on a blog post and has the following fields -

- Post: a ForeignKey field that references the Post model and represents the blog post that the comment belongs to.

- Name: a CharField that stores the name of the person who left the comment.

- Email: an EmailField that stores the email address of the person who left the comment.

- Body: a TextField that stores the content of the comment.

- Created_on: a DateTimeField that stores the date and time when the comment was created.

- Approved: a BooleanField that indicates whether the comment has been approved or not.

## Technologies


### Workspace


#### GitPod
[GitPod](https://gitpod.io/) was the IDE workspace used to build this site.


### Version Control

#### Git
[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

#### GitHub
[GitHub](https://github.com/) is used to store the project.


### Wireframing & ERD

#### Figma
[Figma](https://www.figma.com/) was used to create wireframes during the design process.

#### Draw.io
[Draw.io](draw.io) was used to create the ERD overview.


### Languages used

#### HTML
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
#### CSS
- [CSS3](https://en.wikipedia.org/wiki/CSS)
#### JavaScript
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
#### Python
- [Python](https://www.python.org/)

## Website Design

#### Google Fonts
[Google Fonts](https://fonts.google.com/) was imported to change the font on the website.

#### Font Awesome
[Font Awesome](https://fontawesome.com/) was used on the website to add icons.

#### Bootstrap (5)
[Bootstrap](https://getbootstrap.com/) was imported for responsiveness and styling of the website.

### Development

#### Django
[Django](https://www.djangoproject.com/) was the web framework used to build this project.

_Additional packages/libraries/applications that were used to build this project_ -

- Django Crispy Forms
[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to give forms improved styling in the project.

- Summernote
[Summernote](https://summernote.org/) was used for the admin section/create blog posts section of the project to change the standard Django Editor. To give the admin more options to customize blog posts in the editor.

- Allauth
[Allauth](https://django-allauth.readthedocs.io/en/latest/) was used to allow users to create accounts and log in. Allauth is a third-party Django application.

## Hosting

### Heroku
[Heroku](https://www.heroku.com/) is used to host the application.

### Gunicorn
[Gunicorn](https://gunicorn.org/) is used for deploying the project to Heroku.

### Cloudinary
[Cloudinary](https://cloudinary.com/) is used to host media files and serve them to Heroku.

### ElephantSQL
[ElephantSQL](https://www.elephantsql.com/) is used to host my database. ElephantSQL is a cloud-based PostgreSQL database hosting service.

## Testing
The W3C Markup Validator, W3C CSS Validator Services, JSHint and PEP8 were used to validate the code to ensure there were no syntax errors in the project.

### HTML
I checked all the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)
- No Errors were found.

### CSS
I checked the CSS file using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- No errors were found.

### JavaScript
I checked the JavaScript file using [JSHint](https://jshint.com/)
- No Errors were found.

### Python
I checked for errors in these files: 
- admin.py - _no errors_
- apps.py - _no errors_
- forms.py - _no errors_
- models.py - _no errors_
- tests.py - _no errors_
- views.py - _no errors_

The remaning .py files (settings.py and env.py etc) have errors about lines being too long, this cannot really be fixed.

### Lighthouse
<!-- Lighthouse picture here -->


## Manual Testing

### Home Page/Navigation/Footer
| Test                                     | Testing Performed                           | Expected Outcome                                                                                                              | Pass/Fail |
|------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------|
| Navbar logo                              | Click "sonicetones" logo                    | Takes the user to the home page.                                                                                              | Pass      |
| Navbar Log in                            | Click link                                  | Takes the user to the Log In page.                                                                                            | Pass      |
| Navbar Sign Up                           | Click link                                  | Takes the user to the Sign Up page.                                                                                           | Pass      |
| Navbar Logout (when user is logged in)   | Click link                                  | Redirect user to Log Out page to confirm Log Out                                                                              | Pass      |
| Navbar About                             | Click Link                                  | Redirects user to the about page                                                                                              | Pass      |
| Navbar Bookmark (when user is logged in) | click icon/link                             | Redirect user to bookmarks page                                                                                               | Pass      |
| Navbar Search Bar                        | Add keywords to input & click submit button | Redirect user to search page with search results                                                                              | Pass      |
| Navbar small/medium screens              | Click hamburger icon                        | The Log In, Sign Up, Logout, about, bookmarks and search bar element are available and work the same way as on large screens. | Pass      |
| Blog Posts(Home page)                    | Click on post                               | Redirects user to Post detailed page                                                                                          | Pass      |
| Social Media Links/buttons               | Click social media links/buttons            | Redirects user to the LinkedIn & GitHub                                                                                       | Pass      |
### Blog Post Detailed Page
| Test                     | Testing Performed                                         | Expected Outcome                                  | Pass/Fail |
|--------------------------|-----------------------------------------------------------|---------------------------------------------------|-----------|
| Add Bookmark             | Click on bookmark icon                                    | Adds the chosen post to Bookmarks page            | Pass      |
| Delete Bookmark          | Click on bookmark icon(when post is all ready bookmarked) | Deletes the chosen post from Bookmarks page       | Pass      |
| Like Post                | Click on like button                                      | Adds a like to the chosen post                    | Pass      |
| Unlike Post              | Click on like button(when post is all ready liked)        | Deletes the like from the chosen post             | Pass      |
| Comment Form add comment | Enter text in to comment form and click submit            | Alert message "Your Comment is awaiting approval" | Pass      |
| Comment Form Empty       | Leave comment form empty and click submit                 | "Please fill in this form" message                | Pass      |
### Sign Up Page
| Test                    | Testing Performed           | Expected Outcome                                                                                                                                                 | Pass/Fail |
|-------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Sign Up form works      | Enter username/password     | The Django registration form is validating automatically if the username is valid and if the passwords match and are valid. Otherwise an error message is shown. | Pass      |
| Log In Link             | Click                       | Takes the user to the Log In page.                                                                                                                               | Pass      |
| Successful registration | Finish registration process | Success alert message appears. User is logged in automatically and redirected to home page.                                                                      | Pass      |
### Log In Page
| Test             | Testing Performed    | Expected Outcome                                                                                                          | Pass/Fail |
|------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------|-----------|
| Log In           | Add credentials      | Django login form checks automatically that username and password match (and exist in DB). Otherwise shows error message. | Pass      |
| Sign Up link     | click                | Takes the user to the Sign Up page.                                                                                       | Pass      |
| Successful login | Finish login process | User is logged in and redirected to home page. Success alert messages appears.                                            | Pass      |
### Log Out Page
| Test           | Testing Performed | Expected Outcome                                                      | Pass/Fail |
|----------------|-------------------|-----------------------------------------------------------------------|-----------|
| Log Out button | Click             | Takes the user back to the home page. Success alert messages appears. | Pass      |

## Automated testing
_Due to time constraints I unfortunately did not manage to add any automated test. I plan to do that in the future._

## Manual Testing on smaller screen sizes
The website was tested on all screen sizes (xl - desktop, l - laptop, m - iPad Air, sm - iPhone 12/iPhone 13).

## Bugs
### PEP8 Syntax errors
- line too long

In the code that I have written, I have followed the line length rule. However, in Django generated files like migrations. The migration files aren't generally going to be edited by humans so I feel comfortable leaving them as they are. So those errors are left as they are.

## Deployment
This project was developed in [GitPod](https://gitpod.io/) where everything was committed and pushed to [GitHub](https://github.com/). The Code Institute offered a [template](https://github.com/Code-Institute-Org/gitpod-full-template) that was used as a main structure for this repository. The main deployment was completed then on [Heroku](https://www.heroku.com/).
See the process of the deployment below:

### Step 1:
_Installing Django and supporting libraries_

1. Clone [this repository](https://github.com/Code-Institute-Org/gitpod-full-template)


2. Install Django, supporting libraries and Cloudinary libraries using these commands in the terminal
````
pip3 install 'django<4' gunicorn
pip3 install dj_database_url psycopg2
pip3 install dj3-cloudinary-storage
````

3. Create requirements file using this command in the terminal
`````
pip3 freeze --local > requirements.txt
`````

4. Create project using this command in the terminal
`````
django-admin startproject YOUR_PROJECT_NAME .
`````
_(Don't forget the .)_

5. Create app using this command in the terminal
````
python3 manage.py startapp YOUR_APP_NAME
````

6. Add installed apps to settings.py
`````
NSTALLED_APPS = [
    …
    'YOUR_APP_NAME',
]
`````

7. Migrate Changes using this command in the terminal
````
python3 manage.py migrate
````

8. Run server to test using this command in the terminal
````
python3 manage.py runserver
````

### Step 2:
_Create a new external database_

1. Sign Up/Log In on [ElephantSQL](https://www.elephantsql.com/)

2. Click "Create New Instance"

3. Set up your plan
- Give your plan a name
- Select the Tiny Turtle (Free) plan
- Tags field can be left blank

4. Click "Select Region"
- Select a data center near you

5. Click "Review"
- Check that your details are correct. Then click "Create instance"

6. Go to ElephantSQL dashboard and click on your database project

7. Copy your ElephantSQL database URL

### Step 3:
_Create a Heroku app_

1. Sign Up/Log In on [Heroku](https://www.heroku.com/)

2. From the dashboard click on "New" and create new Heroku App

3. Enter your app name and your location

4. Go to the settings tab

5. Click on "Reveal Config Vars"

6. Add a Config Var called DATABASE_URL
- The value should be the ElephantSQL database URL

### Step 4:
_Attach the database_

1. In GitPod create new file called env.py file on top level directory

2. In the env.py add these lines of code:
- Import os library
````
import os
````
- Set environment variables
````
os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
````
- Add secret key
````
os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
````

3. Go back to [Heroku](heroku.com)
- Add your secret key to Config Vars - SECRET_KEY, “randomSecretKey”

### Step 5:
_Prepare your environment and settings.py file_

1. In settings.py - reference env.py with this line of code:
````
from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
   import env
````

2. Remove the insecure secret key and replace - links to the SECRET_KEY variable on Heroku
````
SECRET_KEY = os.environ.get('SECRET_KEY')
````

3. Comment out the old ````DATABASES```` section.

4. Add a new ````DATABASES```` section _(links to the DATATBASE_URL variable on Heroku)_:
````
DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
````

5. Save all the files and make migrations in the terminal using this:
````
python3 manage.py migrate
````

### Step 6:
_Get your static and media files stored on [Cloudinary](https://cloudinary.com/):_

1. Sign Up/Log In on [Cloudinary](https://cloudinary.com/) and copy your CLOUDINARY_URL from the Cloudinary dashboard.

2. Add Cloudinary URL to env.py:
````
os.environ["CLOUDINARY_URL"] = "cloudinary://************************"
````

3. Go back to [Heroku](heroku.com) and add Cloudinary URL to Heroku Config Vars
- COUDINARY_URL, cloudinary://************************

4. Add DISABLE_COLLECTSTATIC to Heroku Config Vars:
- DISABLE_COLLECTSTATIC, 1

5. In the settings.py, add Cloudinary libraries to INSTALLED_APPS in this order:
````
INSTALLED_APPS = [
    …,
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    …,
]
````

6. Make Django use Cloudinary to store media and static files:
````
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
````

7. Link file to the templates directory in Heroku
Place this under the BASE_DIR line:
````
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
````

8. Change the templates directory to TEMPLATES_DIR
````
TEMPLATES = [
    {
        …,
        'DIRS': [TEMPLATES_DIR],
       …,
            ],
        },
    },
]
````

9. Add Heroku Hostname to ALLOWED_HOSTS:
````
ALLOWED_HOSTS = ["PROJ_NAME.herokuapp.com", "localhost"]
````

### Step 7:

1. In GitPod create 3 new folders on top level directory called:
- media
- static
- templates

2. Create a file called ````Procfile```` on the top level directory

3. In the Procfile add this code:
````
web: gunicorn PROJ_NAME.wsgi
````

4. In the Terminal Add, commit and push your files:
````
git add .
git commit -m “Deployment Commit”
git push
````

5. In Heroku go to the deploy tab.

6. Chose GitHub as deployment method and chose your repository.

7. At the bottom of the page chose Deploy branch (from the main branch).

## Production

1. In your settings.py file, set DEBUG to False
````
DEBUG = False
````

2. Make sure that X_FRAME_OPTIONS and ALLOWED_HOSTS are added to your settings.py file.
````
X_FRAME_OPTIONS = 'SAMEORIGIN'

ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']
````

3. Go to Heroku, in Settings - Reveal Config Vars

4. Remove DISABLE_COLLECTSTATIC

5. On Heroku, go to Deploy tab and scroll to the bottom of the page and chose Deploy(Main branch)

6. Click "View App" when the build is done.

## Credits

### Code
- The initial site functionality was made using the 'I Think There For I Blog' walkthrough by Matt Rudge via Code Institute. The code was adapted for what I needed.

- The [Django Documentation](https://docs.djangoproject.com/en/4.1/) 
and the were an invaluable source of information throughout this project

- The [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was a big source of information when the styling of the website was created.

-  This [video](https://www.youtube.com/watch?v=H4QPHLmsZMU) came in handy when I was building the Bookmark function of the blog.

- This [video series](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) helped me throughout the project.

- Django deployment instructions by [Code Institute](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

### Content
- The structure and layout of this README file was inspired by [kera-cudmore](https://github.com/kera-cudmore/readme-examples/blob/main/milestone1-readme.md)

### Acknowledgements
- My friend Lucas Holm for his ongoing help with all kinds of smaller issues and feedback throughout the project.
- My mentor, Antonio Rodriguez, at Code Institute, for continuous helpful feedback and support.
- The always friendly and helpful tutor support at Code Institute.
