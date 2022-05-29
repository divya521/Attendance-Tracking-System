<!-- <div id="top"></div> -->
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div> -->



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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <!-- <li><a href="#roadmap">Roadmap</a></li> -->
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The project involves a website application for tracking attendance using facial recognition.This attendance tracking system not only marks the presence of people but also marks the time-in and time-out of individual persons.

This web application intends to serve as an effficient substitute for traditional attendance systems like marking attendance physically or by scanning id cards which invloves proxy attendances.It  enables an organization to maintain its records like in-time, out time and attendance digitally.

This web application can be used in corporate offices, schools, big organizations  and many public places where security is essential.

<!-- It  enables an organization to maintain its records like in-time, out time and attendance digitally. Now such digitalization of the system will help in better visualization of the data using graphs to display the no. of employees present today and total work hours of each employee. -->

### Features:
This web application lets it's users to :
* First register them if they are new by clicking on register new entry button.
* Secondly marking their in-time by clicking on login button.
* And marking their out-time by clicking on login button

<!-- Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template! -->

<!-- Use the `BLANK_README.md` to get started. -->

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

 Tools used are :

* [React.js](https://reactjs.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)

Frameworks/Libraries used are :
* [Google firebase](https://firebase.google.com/?gclid=CjwKCAjwkMeUBhBuEiwA4hpqEK3GpdhUdascT_h2jzUfJk-3nEQxQZdgOTYuxeidAStFt1DrdVX8phoC9TkQAvD_BwE&gclsrc=aw.ds)

    *  Authentication
    *  Database 

* [face_recognition](https://pypi.org/project/face-recognition/)
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

<!-- This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps. -->

### Prerequisites

This project has been tested with windows 10 and ubuntu 20.04 
* npm
* Node.js
* Python>=3.7.9

### Installation

#### Windows
_Follow the below instructions step wise for proper running of this project ._

1. Install visual studio build tool [https://visualstudio.microsoft.com/downloads/?q=build+tools](https://visualstudio.microsoft.com/downloads/?q=build+tools)  (this step is not required for linux users)
2. Setup a virtual environment :

   * first create a virtual environment

      ```sh
      python -m venv my_venv[any name of your environment]
      ```
   * then activate the virtual environment

      ```sh
      my_venv\Scripts\activate
      ```
   * change the working path to virtual environment setup 
      ```sh
      cd my_venv
      ```
3. git clone the repo 
   ```sh
   git clone https://github.com/divya521/Attendance-Tracking-System.git(my repo url)
   ```
4. After cloning change the working path to cloned git repository
   ```sh
   cd Attendance-Tracking-System
   ```
5. Install all the requirements 
   ```sh
   pip install -r requirements.txt
   ```
6. Change the working path to flask-frontend folder
   ```sh
   cd flask-frontend
   ```
7. In the flask-frontend folder install the node modules  
   ```sh
   npm install
   ```

8. Navigate to the flask-backend directory :
   ```sh
   cd ../flask-backend
   ```

9. Create known-people and stranger directory :
    ```sh
    mkdir known-people
    mkdir stranger
    ```
<!-- #### Linux
_Follow the same steps as above with different command line for linux terminal :

1. Install visual studio build tool [] -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Open 2 terminals one for running frontend and other for running backend.
2. Change your directory to flask-frontend for running frontend in one terminal and to flask-backend for running backend in another.
3. In terminal for the frontend run : 

    ```sh
    npm run dev
    ```
   and for the backend run :

    ```sh
    flask run
    ```
4. After running both the terminals, frontend terminal will provide with a link which by ctrl+click will direct to the website where :

   * The home page provides with the options to register and mark the presence by logging in and logging out.


   ![Screenshot (213)](https://user-images.githubusercontent.com/64090048/170852899-634246dc-1484-410f-83d5-3d87dc2bf131.png)

      
   * First to register click on register new entry button which directs to the new entry registration page where first write the roll no and  by looking properly in the web cam click on the register button which will then pop up the dialog box displaying "successfully registered" if properly registered and "unsuccessfully registered" if not.

   ![Screenshot (215)](https://user-images.githubusercontent.com/64090048/170853022-918cfea4-29a3-4c83-abf8-3c4231dc9eb6.png)


   * After successfully registration is done , click on back to home page button which redirects to the home page where to mark the presence look properly in the web cam and click the login button which then pop up the dialog box displaying :logged in successfully" and when logging out repeat the same as above and click on logout button which then pop up the dialog box displaying "logged out successfully".


   ![Screenshot (217)](https://user-images.githubusercontent.com/64090048/170853046-0d6b4b3e-6cdf-4e5c-9e58-e78ababdd395.png)


   ![Screenshot (218)](https://user-images.githubusercontent.com/64090048/170853984-4499c8f7-569a-4032-ab60-562c809c3353.png)


   ![Screenshot (219)](https://user-images.githubusercontent.com/64090048/170854002-a4b40d38-de3a-422c-bc18-715b41c93da0.png)

   ![Screenshot (220)](https://user-images.githubusercontent.com/64090048/170854014-2e35717f-a891-4589-b390-8045e4f9d4c3.png)


5. And finally for viewing database please check this : 
  [Firestore Realtime Database](https://console.firebase.google.com/u/0/project/face-recognition-d754f/database/face-recognition-d754f-default-rtdb/data)



     Hope you all enjoy this !



<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues). -->

<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

 --> 

<!-- CONTACT -->
## Contact

Email address  -  divyahsrathore@gmail.com

Project Link: [https://github.com/divya521/Attendance-Tracking-System.git](https://github.com/divya521/Attendance-Tracking-System.git)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
