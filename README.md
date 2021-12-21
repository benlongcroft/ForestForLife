# Forest For Life

### Introduction
Forest For Life is an informative website consisting of articles, blogs, and a game, all revolving around climate
change with an emphasis on deforestation.

The game premise is as such:

- A factory has recently been built near the user; it is producing pollution, effecting the user’s quality of air. 
The pollution levels are slowly rising, creating an ever-worsening environment. It is the user’s task to plant trees to
counteract the effects of pollution, turning pollution into clean air. The users core mission is to eventually plant 
enough trees to offset the effects of pollution and lower the pollution levels to eventually zero.

### To-Do:
- Add filler content to pages for design purposes
- Add admin functionality
- Add RSS feed to explore page
- Add two-factor authorisation
- Banner copywrite

### Known Bugs:
- Navbar hamburger not expanding or collapsing
- SQlite is used instead of MYSQL for prototype

### Current Functionality:
- User is able to move between all pages
- User is able to register, in-which case they are re-directed to the login page
- User is able to login
- User is greeted by an additional welcome page after logging in
- User is greeted by an additional goodbye page after logging out
- Sonny's game and logout page is only visible on navbar after user is logged in
- User passwords are hashed
- Admin is able to login, view all users and access login attempts
- Security headers inplace, enforcing HTTPS and other security related features

## How to run game
#### Mac
./manage.py runserver_plus --cert /tmp/cert
#### Windows
python manage.py runserver_plus --cert /tmp/cert

### Temporary User Information
User:
Username: testuser
Password: testpasswordd

Admin:
Username: admin
Password: testpassword

##Copyright Information
Logo - https://creazilla.com/nodes/79045-cartoon-tree-clipart
Home Page Image - https://www.pinterest.co.uk/pin/672162313131260922/
Footer Template - https://codingpoets.com/build-a-professional-web-application-with-php-and-mysql

