# <p style="text-align: center;">Capstone Proposal</p>

### **<p style="text-align: center;">Job Application Tracker</p>**



## Project Overview
Track job applications and display the data through tables and graphs. 

The problem this app is attempting to solve is the lack of simple and easy to use trustworthy job application trackers by providing users with a modern and user friendly experience to keep track of job applications along with important information about each job in a more centralized way. 

Using Vue (front-end), Django(back-end), Google Visualization API(charts).

## Functionality
User will be able to:
- create an account and log in with username/email/password 
- input job applications:
  - add job title
  - add company name
  - add salary
  - add links to the job posting
  - assign status (color coded with a gradient color-to-white top-to-bottom style) *drop down menu*
  - assign job industry/field *drop down menu*
  - assign part-time/full-time/contract/internship employment *drop down menu*
  - assign day/night shift *drop down menu*
  - add date of application *drop down menu or calendar*
  - add a notes section
  - favorite a job
- search job applications by job title/status/date
- organize job applications by date/status/job title
- expand job application box

Welcome the user with a home page (content TBD) and nav bar with Dashboard(if logged  in), sign up, log in, log out(if logged in). When logged user will be redirected to their profile (Dashboard) page with a welcome message on the nav bar displaying their name (i.e. Welcome, John!).

Profile page will have a vertical nav bar on the left with applications/favorites/graphs and the main content using the rest of the screen. Each job application will be displayed inside a box

User will be presented with a "Add new job application" feature at the top of the page along with a search function and below they will see all of their current applications and by expanding an application user will be able to edit/delete the application or see more information.

The graphs page will display color coded graphs/charts all job applications by:
- number of applications
- earliest date to current date
- status
- field/industry
- type of employment
- shift
- salary


Vue will be taking data from the user and sending it back to Django to be stored in the database and Vue will also fetch data from Django and its database to display content back to the user.

## Data Model
User information:
- username
- email
- password


New application:
- job title
- company name
- date applied
- salary:
  - hourly
  - yearly
- type of hire:
  - part time
  - full time
  - contract
  - internship
- shift:
  - day
  - night
- links
- job field/industry (maybe have a drop down menu with all available options i.e IT, Construction, etc..)
- job status:
  - applied
  - not selected
  - selected for interview
  - ghosted
  - interviewed
  - offer
- favorite: 
  - boolean field

Favorites:
- list of all items with favorite=true



## Schedule
week 1 - back end
week 2 - front end
week 3 - ensure smooth data sharing between Vue and Django with post/get requests + debugging