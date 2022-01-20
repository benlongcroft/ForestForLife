# Forest For Life

### Introduction
Forest For Life is an informative website consisting of articles, blogs, and a game, all revolving around climate
change with an emphasis on deforestation. Forest For Life is a non-profit project, with all profit made through
donations being donated to charities relating to climate change and deforestation such as The Woodland Trust.

Notable features of Forest For Life is its ability to allow users to make generous donations and contact admins through
a contact us form, which when sent, is sent to an admins email.

Future possible features:
- A leaderboard displaying user information on Sonny's Forest page, alongside game
- Sonny's Forest retaining user game data, allowing user to continue game state, when logging out and logging back in
- Update donation feature, allowing user to choose how much they would like to donate

The game premise is as such:

- A factory has recently been built near our character, Sonny; it is producing pollution, effecting Sonny's quality of 
air. The pollution levels are slowly rising, creating an ever-worsening environment. It is Sonny's mission to plant 
trees to counteract the effects of pollution, turning pollution into clean air. Sonny's core goal is to eventually 
plant enough trees to offset the effects of pollution and lower the pollution levels to eventually zero.

## Running Project
Please note that the following information regarding how to run the project is done so under the impression that the 
user is using PyCharm IDE, other software may vary.
### Requirements to run project
- Python 3.9 +
- Please locate requirements.txt and download all files specified

### How to run project
- Copy and paste relevant code from below into terminal
- Once ran, click on 'https://127.0.0.1:8000/' highlighted in blue
#### Mac
./manage.py runserver_plus --cert /tmp/cert
#### Windows
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem

### User Information
####User
Username: testuser
Password: testpasswordd

####Admin
Please note that in order to access admin UI, user has to type '/admin' in front of url 'https://127.0.0.1:8000/' 
creating the full url 'https://127.0.0.1:8000/admin'.
Username: admin
Password: testpassword

### Login Attempt Reset
When testing user login and logout, please be aware that the best way to reset attempts if the user was to be
locked out would be to run the following command within the terminal:
**python manage.py axes_reset**
It is possible to reset the attempts through the admin UI however with axes locking accounts based off of IP
addresses, it is easier to use the command as found in the documentation
https://django-axes.readthedocs.io/en/latest/3_usage.html.

### Contact us information
Once a contact us form is sent and passes all criteria, the message is sent to the email address
'n.dawson3@newcastle.ac.uk'.
Please note that only the email 'n.dawson3@newcastle.ac.uk' works when sending emails.
This is due to operating a free SendGrid email hosting account. With a paid account being the only way of allowing
any user-entered email to send emails.

### Donation information
A test account has been set up with Stripe. As such, test money can be sent to the account and is visible within the 
Stripe account.
Please note that only the card number '4242 4242 4242 4242' will work when sending donations.
This is a test card number, allowing the user to send test money to simulate a real payment.
Alongside this, it is necessary to provide an in-date expiry date.
All other information is not important and can be a random name, email, CVC and post code in order to process the 
donation.

### Sonny's Forest
Information regarding how to play Sonny's Forest can be found on Sonny's Forest page. Clicking on both Sonny's Forest -
Backstory and Sonny's Forest - Tutorial to access dropdown text, further instructing the user.

### Social Media
Please note that all social media links, specifically ones found in the footer and the social media interaction buttons 
found within d_success.html (donation successful page) are all fully functional and send the user to the relevant 
social media accounts.

# Further Information Regarding Sonny's Forest

### Description

A short 2D isometric game created by Team 22 (Newcastle University) for the Forest For Life website. This game was built
in Unity for CSC2033.

### Prerequisites

-   Browser WebGL support
-   Keyboard

This game requires a browser supporting WebGL 1.0

**To play** the game, simply head to the Forest For Life website or check out https://simmer.io/@Team_22/sonny-s-forest to play. 

This game is 27.2MB once built into a Web GL application.

### About Sonny's Forest

Sonny's Forest is a fun web game for 8 year olds and older. 

30 years in the future, with climate change ravaging the planet, Sonny makes a promise to try and replant the trees. 
Starting with one field, explore Sonny's Forest, fight the pollution and collect seeds.

### How to Play

Playing Sonny's Forest is easy, use the **arrow keys** to move around the forest. 

press **P** to plant a tree while standing next to a plot.

press **tab** to change your loadout

Once a tree has died, you can press **C** when near the plot to free up space.

Watch your balance of Rune Coins grow on the counter at the top. Don't let the pollution get to 100%, or it's game over! 
Check out the tree stats for advice on strategy.

### Tree Stats

##### Nurgi Needle

*Lifespan - >* ~100 seconds

*Efficiency- >* 90%

*Seed Growth Time - >* ~9 seconds

*Price - >* 0.20 RC


##### Fovir Fir

*Lifespan - >* ~150 seconds

*Efficiency- >* 80%

*Seed Growth Time - >* ~14 seconds

*Price - >* 0.35 RC


##### Ackerieva Apple

*Lifespan ->* ~315 seconds

*Efficiency- >* 50%

*Seed Growth Time - >* ~28 seconds

*Price - >* 0.50 RC


##### Golucki Gladious 

*Lifespan ->* ~400

*Efficiency- >* 30%

*Seed Growth Time - >* 35 seconds

*Price - >* 0.70 RC
##Copyright Information
A list of all relevant hyperlinks to images used throughout Forest For Life. Alongside this, hyperlinks to data sources
are provided, which were used to help develop specified features within Forest For Life.

Logo - https://creazilla.com/nodes/79045-cartoon-tree-clipart

Home Page Background Image - https://www.freepik.com/free-photo/high-angle-shot-beautiful-forest-with-lot-green-trees-enveloped-
fog-new-zealand_10835665.htm#query=forest&position=7&from_view=keyword

Home Page Card Navs:
https://unsplash.com/photos/Xywi2MePlYQ
https://unsplash.com/photos/F5s2rcNtSi0

Home Page info sources:
- https://www.ukri.org/news/studying-how-trees-can-help-the-uk-reach-net-zero-emissions/
- https://climate.nasa.gov/evidence/
- https://www.nationalgeographic.com/environment/article/deforestation

Home Page content images:
- https://unsplash.com/photos/TknRspuNTJs
- https://unsplash.com/photos/Rfflri94rs8
- https://unsplash.com/photos/_MG2TCW6wJo

Footer Template - https://codingpoets.com/build-a-professional-web-application-with-php-and-mysql

About Page image - https://images.pexels.com/photos/3493777/pexels-photo-3493777.jpeg?cs=srgb&dl=pexels-aleksey-
kuprikov-3493777.jpg&fm=jpg

Donate Stripe code tutorial - https://testdriven.io/blog/django-stripe-tutorial/

D_success image - https://unsplash.com/photos/YtqUWAlL2GE

D_cancelled image - https://www.freeimages.com/photo/autumn-tree-1408307

Article Images:
- https://media.nationalgeographic.org/assets/photos/239/748/b45dce32-21f4-4646-99d0-2057f6a12e49.jpg
- https://wwfint.awsassets.panda.org/img/original/deforestation_fronts_report_cover.jpg
- https://www.worldatlas.com/r/w1200/upload/6a/4b/49/shutterstock-1408605185.jpg
- https://youmatter.world/app/uploads/sites/2/2018/10/climate-change-definition-meaning.jpg
- climate_change1 - https://unsplash.com/photos/_whs7FPfkwQ
- climate_change2 - https://unsplash.com/photos/5sh24a7m0BU
- climate_change3 - https://unsplash.com/photos/n52HL8hmsdg
- climate_change4 - https://unsplash.com/photos/96iwiAxOuJw
- climate_change5 - https://unsplash.com/photos/BqYttheZzUo
- climate_change6 - https://unsplash.com/photos/NBwP2jjnATE
- deforest1 - https://unsplash.com/photos/K5KmnZHv1Pg
- deforest2 - https://unsplash.com/photos/AcdCWfbCI1g
- deforest3 - https://unsplash.com/photos/GCeOASk9my8
- deforest4 - https://unsplash.com/photos/TrUbzz4KamI
