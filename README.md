# Viscous

> It is the Social site webapp developed with Django, python.

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://www.azwane.pythonanywhere.com) 

## Table of Contents (Optional)

- [Introduction](#introduction)                                                                                                
   1. General structure of web app                                                                                  
   1. How to use this report                                                                                             
   1. Overview of requirements                                                                                     
- [Problem statement](#problem statement)                                                                                     
- [Objectives](#objectives)                                       
- [Theoretical Background](#theoretical background)                                                                             
   1. Structure of web app                                                                                               
   1. Working theory                                                                                                       
   1. Testing and maintenance                 
- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)

# INTRODUCTION
## General structure of web app
Viscous is a social networking web app that runs on a browser which is created with an aim for solving social networking problems digitally specially designed with a concept for the students of the college. In this app people can share information about each other add their personal shareable information, mails, thoughts, given assignments notices and everything that is possible The report is made to show the structure of this web app its functional and nonfunctional requirements, how the models are managed, how data are extracted and handled in a database especially using sqlite, the design of the web app and further extension plans. This project encourages us to view existing similar platforms, make use of modern extensions and specially add problem-solving features. The project development follows the waterfall model but not strictly  there is is always room for improvement and new features could easily be added without compromising the previous build the whole web app is developed with the use of  HTML, JavaScript, CSS with python as the backbone programming language and its popular framework Django. The further extension is made possible due to compact development within the framework due to its facility of packaging apps for reusability.

## How to use this report 
The whole report can be divided into two parts, one understood by the end users and another by the system analyst or software developer. The functional requirements shows the overall structure and facilities of the app in DFD level 0 and DFD level 1 and the overall system view diagram present under methodology topic which is easily understood by the end users, while the non-functional requirements shows the inter-connection between the models and system, the process and the data flow between them which is shown in DFD level 2 and  viscous system diagram.

## Overview of the Requirements 
Viscous social web app is a browser based software application system, it will provide various functional and non-functional requirements for: 
• Being hub for people with interests
• View the recent information post 
• Know each other’s view and share knowledge
• Have contact information of each other
• Announcing events

# PROBLEM STATEMENT 
The project idea took the real form when there arrived a problem for sharing information of classroom and college events with fellow students among each other. There is no proper platform provided by college where student-student and teacher-student could share information with each other. There is no direct communication between teacher and student when needed. Most of the information is shared through messaging apps which aren't commonly used by everybody and not everyone does have an account. Therefore, circulation of information to everyone is difficult and in such a chat all information gets lost among other communication messages. Neither one can share their knowledge and views and social messages reaching everyone.

# OBJECTIVES
- Share information among each other
- Get notified about recent activities
- Reduce communication distance and delay

# THEORETICAL BACKGROUND

## Structure of web app
The processing and structure of the viscous app could be shown mainly in two ways, they are:
Front-end structure: It is the user view-point structure which is the main way of interacting with the system directly. The system is run on a browser so would be using HTML5, for content designing purpose it would be using CSS and JavaScript. At first the layout of the app is designed using software like Gravit Designer and Figma on the basis of the possible user interactions. Only the structure is programmed as required by design which outputs all templates possible in the web app. This is very useful to start from layout design before functional development because it gives the idea what needs to be developed and preserves the initial design idea for the future.

### Backend structure : This is the structure which defines the functionality to the templates designed. The viscous web app would be using:
- **Python** as the main programming language. Python programming language is very scalable,easy to understand, implement and maintain codes.
- **Django Framework** as a backbone for data managing and view  controls development. Django is a large framework that helps to create error-free, packageable, maintainable apps within the same project. It has well maintained documentation in each and every thing used in the framework.
- **SQlite** as a main database for the web app. SQLite is a relational database management system contained in a C library. In contrast to many other database management systems, SQLite is not a client–server database engine. Rather, it is embedded into the end program. SQLite is ACID-compliant and implements most of the SQL standard, generally following PostgreSQL syntax.
- **MVC** which is an architectural pattern that separates the application into three logical components: model, view and controller. Each of these components is built to handle specific development aspects of an application. It is one of the most frequently used industry standard web development frameworks to create scalable and extensible projects.

#Testing and maintenance
The testing is also done. The first unit test for models is done in the python console provided under Django framework. Then the views are tested on every browser specifically Google chrome and Mozilla Firefox of different screen resolution. Then the control testing is done with the concept of white box and black box. Furthermore, SEO test, latency and overall test is done with the Google Lighthouse present on the browser. First release is also tested within other people for review and enhancement.
The app is maintained and each new feature to add is tested locally and then only gets finally pushed to the main server. The web app is hosted on [here](https://azwane.pythonanywhere.com/) . On further extension new hosting service is chosen for great speed delivery of the site.



## Installation

🚀&nbsp; To install in your local machine follow the steps below:

### Clone

- Clone this repo to your local machine using `https://github.com/azwyane/Covid19.git`

Goto to your terminal and type:

```sh
git clone https://github.com/azwyane/viscous.git
```

### Setup

- Inside your cloned folder create a virtual environment with *venv* and activate it
```sh
python3 -m venv venv
. venv/bin/activate
```
> which puts you inside virtual environment like this:
```
(venv)$
```
> Now install the requirements:
```
(venv)$pip install -r requirements.txt
```

- Run the project

> Now to run the project type in your terminal:
```
(venv)$python manage.py run
```

## Features
❤️&nbsp; 
> 

---

##  Contributing
🤝&nbsp;
> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/azwyane/viscous.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/azwyane/Covid19/compare" target="_blank">`https://github.com/azwyane/viscous/compare`</a>.


---

###  📫&nbsp; Found a bug? Missing a specific feature?

Feel free to **file a new issue** with a respective title and description on the the [azwyane/visvous](https://github.com/azwyane/viscous/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 

