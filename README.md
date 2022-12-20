<!-- Heading -->

# sonicetones - [Live link]()

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


### Languages used

#### HTML
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
#### CSS
- [CSS3](https://en.wikipedia.org/wiki/CSS)
#### JavaScript
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
#### Python
- [Python](https://www.python.org/)
