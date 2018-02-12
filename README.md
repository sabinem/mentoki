![alt text](http://mentoki.com/static/img/mentoki_logo_untertitel.jpg "Logo Title Text 1")

# Mentoki Project
Mentoki is a platform for teaching and learning. The platform provides 
infrastructure to teachers/mentors for holding up online classes. 
For payments of the courses braintree is used as payment provider
#Structure
The platform splits up into a public part and a private part.
The private part is only accessible by registered users, mostly
teachers and their students.
Also generally data-handling and data-viewing are kept in seperate apps.
# App-Structure
## General Untilities
* apps_core: utils for handling emails, uploads and the like
## User-Data-Apps
* accounts: custom user model
* apps_accountdata: userprofiles
## Data-Handling-Apps
* apps_customerdata: handling of customerdata, orders, etc.
* apps_data: handling data that relate to courses or classrooms
* apps_pagedata: data handling for public pages
* apps_productdata: data handling for productdata
## Surface-Apps
* apps_internal: (registered users) views for desk, classroom and coursebackend 
* apps_public: (anonymous users) views for public pages and payment processing

# Architecture(Apps)

### apps_data: 
handles the data

### apps_internal:
handles all views for registered teachers and learners and has two apps: one 
for the classroom activity and one for the teachers managing and setting up 
the classrooms.

### apps_public
manages the public face of the website

### apps_core
handles emails and central utilities

