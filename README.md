# Instagram Clone
#### By Lucas Otieno Owino
## Description
A clone of the website for the popular photo app Instagram.
## Screenshots of the app
* Home page
![Screenshot from 2020-06-04 02-06-13](https://user-images.githubusercontent.com/60548928/83697687-56892880-a608-11ea-8fcb-b6b3e8e3ad55.png)
* Comment modal
![Screenshot from 2020-06-04 02-06-21](https://user-images.githubusercontent.com/60548928/83697698-5f79fa00-a608-11ea-8aa3-ada6c49cfd88.png)
* Search page
![Screenshot from 2020-06-04 02-06-28](https://user-images.githubusercontent.com/60548928/83697704-643eae00-a608-11ea-97cb-db305cd762bc.png)
* Upload Post Page
![Screenshot from 2020-06-04 02-06-52](https://user-images.githubusercontent.com/60548928/83697709-686acb80-a608-11ea-8e12-48f9f2702fd2.png)
## User Story
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
## System Features
* Your Project must contain an Image model with the following properties:
1.Image
2.Image Name.
3.Image Caption.
4.Profile Foreign key
5.Likes
6.Comments
* You must implement the save, update and delete methods in the models.
* Your project must have a search form that when submitted calls a search function in the view function and redirects to a search results page.
* When a user clicks on an Image he/she should be redirected to where the image is displayed and should also see the details of the Image.
* Your application should have a solid authentication system that allows users to sign in or register into the application before using it. When a user registers with your application they should receive a confirmation email.
* Your project should be deployed to Heroku when you have finished with the set features. You should provide the link to your project in the description part of your project repository.
## Technical Requirements
* Create a specs markdown file that lists down all the projects specifications.
* All your models should contain unit tests to test the different behaviours. All your test should pass.
* Your project should follow the proper folder structure.
* Your project should be deployed to Heroku.
* Your project should contain proper commit messages.
## Technologies Used
  * Python 3.6.9
  * HTML5, CSS and Bootstrap
  * Django Framework
  * Postgressql
  * Heroku
## BDD
| Input                                         | Behaviour                                                                                | Output                                                                                                                                 |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| User registers for an account by filling form | Page redirects user to login page                                                        | User is redirected tpo login page                                                                                                      |
| User logs in                                  | User is taken to the home page                                                           | Redirect you to the homepage where the user is greeted with a feed of most recent photos posted                                        |
| User clicks upload button and fills the form  | The page reloads                                                                         | User's new post is displayed on the feed                                                                                               |
| User clicks on the like button                | The page reloads                                                                         | Like count of the post is increased by one value                                                                                       |
| User clicks on the comment button             | A modal appears with a comment form | The comment is stored in post                                                                                         |
## Link to live site
[](link)
## License
Copyright (c) [2020] [Lucas Otieno]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.