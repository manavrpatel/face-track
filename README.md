# Face-Track

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="project/static/images/logo.jpg" alt="Logo" width="90" height="90">
  </a>

  <h3 align="center">Face-Track</h3>

  <p align="center">
    Attendance Tracking made Super Easy!!!
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

There are great attendance tracking tools out there. However, Marking Attendance of students or staff especially when there are more than a few people, takes a lots of time and consumes a vast portion of the lecture/meeting time. So, how this web-app can help out??

Here's how:
* This web-app uses face recognition model to identify different faces and mark their presence at the same time.
* UI of the "Face-Track" is smooth and easy to understand. So, a user who visited the app for the first time can easily navigate through different features. :smile:
* this web app is built to mark Attendance in physical mode(using camera) and online mode(using screen capture).


### Built With

This section lists all major frameworks/libraries used to bootstrap this project.

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [Flask SQLAlchemy](https://www.sqlalchemy.org/)
* [Flask WTFORMS](https://wtforms.readthedocs.io/en/3.0.x/)
* [face_recognition](https://pypi.org/project/face-recognition/)
* [openCV python](https://pypi.org/project/opencv-python/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Bootstrap](https://getbootstrap.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This section will giude you through the installation process.


### Installation

_Follow the steps to Clone and Run the project._

1. Clone the repo
   ```sh
   git clone https://github.com/manavrpatel/face-track.git
   ```
2. Install required packages
   ```sh
   pip3 install -r requirements.txt
   ```
3. Run the Flask Project.
   ```sh
   $ export FLASK_APP=hello
   $ flask run
   ```
3. Run the Flask Project in Debug mode.
   ```sh
   $ export FLASK_APP=hello
   $ export FLASK_ENV=development
   $ flask run
   ```


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Features -->
## Features
This web-app offers following features:
* User can create Multiple classrooms for different subjects and use it to track attendance of a certain group.
* Every classroom card displays a summary of attendance. e.g (25 out of 30).
* User can Add as Many Classrooms and Add any number of people in it.
* "People" section shows the list of all the participants of that particular class.
* Cards of the Students that are present will be highlighted as green to mention that they are present.
* User can manually toggle the attendance of a student.
* Face-Track provide User with different ways to mark presence.

### the X-Factor
* Attendance can be marked using camera feed or can be switched to screen capture by simply clicking capture which will then capture the screen and retreive data from there. 
* This feature make this Web-App very unique, as it serves as an All-in-one app for both the physical mode and online meetings.



<!-- CONTACT -->
## Contact

Email - manavrpatel2111@gmail.com

Project Link: [https://github.com/manavrpatel/face-track.git](https://github.com/manavrpatel/face-track.git)

<p align="right">(<a href="#top">back to top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->

[product-screenshot]: project/static/images/Getstarted.jpg
