# Assignment 4 - Creating Tweeter (A Twitter Clone)

## Author

Schyler Lowry

## Description

You will be creating a social website called Tweeter that will allow users to
be able to make posts called Twits that other users can view.
Users of the site will be able to make Twits that contain both text and
pictures via a URL to a picture, and like Twits that other users make.

Ensure that you have a `requirements.txt` file with your required packages. I will not grade the assignment if I can't restore the packages easily!

The program should allow the following functionality:

1. A Custom User model that adds a date of birth.
2. Full user authentication so that only authenticated users can use the site.
3. Sign up and authentication forms / views so that users can authenticate with the system.
4. Ability for users to be able to change and reset their password. (Just use the same fake SMTP as the in-class.)
5. A profile page where a user can update details about themselves. (username, fname, lname, email, date of birth)
6. A Dashboard for each user that will show all the Twits in the system listed with the most recent ones first.
7. Pages / forms to be able to CUD a Twit. Update and Delete should be limited to the person that made the twit.
8. New Twits should allow both text and URL for a picture. Image URL can then be used with a img tag to render the image.
9. A Public Profile page for each user that shows all the Twits for that user. Similar to dashboard feed, but only contains all Twits for that specific user. Also most recent first.
10. Ability for users to like or unlike a particular Twit that someone has made using AJAX.
11. Ability for users to add a comment on Twits. This will only be create functionality. No need for update / delete.
12. Sufficient automated tests to verify all functionality.
13. Ensure `requirements.txt` is included in your project.


Documentation should include the following for this, and all future assignments:
* Comments at the top of each source code file that you add or edit with:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. I would highly suggest you use the ''' (triple quote) method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

### Database Requirements
Here are the requirements for the database in an ERD. There are other authentication related tables that I did not include but are provided via Django's auth system. The Users table is the only one that really needed to be shown since there are so many relations between Users and our other tables. There are no relations between the other authentication tables and our tables, which is why I omitted them.

NOTE: For the URL field on the Twit model, you are not using an ImageField. Those are extremely hard to properly set up. Perhaps if the semester was twice as long we could consider. Instead, you are simply loading images via a URLField. Meaning that the user will provide a URL to image that already exists on the internet. This will be WAY easier for you to implement. If you have questions about it, ask.

![Database Entity Relationship Diagram](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_erd.png "Database Entity Relationship Diagram")

### Screenshots

Here are some images of the non-admin pages that I made for my key. This is more or less to give you an idea as to what the general concept is in case the written description is not clear. I realize that your assignment may not end up as elaborate in style as mine, so don't feel as though it needs to visually match mine exactly. I am looking for the general concept though. I will also mention that I used Bootstrap to do my styling.

#### Sign Up
![Sign Up](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_sign_up.png "Sign Up")

#### Login
![Login](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_login.png "Login")

#### Forgot Password
![Forgot Password](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_forgot_password.png "Forgot Password")

#### Dashboard
![Dashboard](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_feed.png "Dashboard")

#### Private Profile
![Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_personal_profile.png "Profile")

#### Public Profile
![Public Profile](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_public_profile.png "Public Profile")

#### Twit Create
![Twit Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_add.png "Twit Creation")

#### Twit Edit
![Twit Edit](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_edit.png "Twit Update")

#### Twit Delete
![Twit Delete](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_delete.png "Twit Delete")

#### Comment Add
![Comment Creation](https://barnesbrothers.net/cis218/assignment_images/assignment_4/cis218_assignment_4_screenshot_twit_comment_add.png "Comment Creation")


### Notes
Once you have added any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all available Bootstrap examples here:

https://getbootstrap.com/docs/4.0/examples/

In addition, you can find the documentation for Bootstrap here:

https://getbootstrap.com/docs/4.0/getting-started/introduction/

## Grading
| Feature                                     | Points |
|---------------------------------------------|--------|
| Custom User Model                           | 5      |
| Full User Sign Up / Authentication          | 5      |
| Password change / reset functionality       | 5      |
| Personal Profile page                       | 5      |
| Public Profile page. Twits from one user.   | 10     |
| Dashboard feed of Twits from all users      | 10     |
| CUD Twit                                    | 10     |
| Allowing Text and Picture URL in Twit       | 5      |
| Liking / Unliking a Twit                    | 10     |
| New Comment Form                            | 10     |
| Styling                                     | 5      |
| Automated Tests                             | 10     |
| Documentation                               | 5      |
| Readme                                      | 5      |
| **Total**                                   | **100**|

## Outside Resources Used
https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
I learned how to render crispy forms fields individually.

https://stackoverflow.com/questions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
I learned how to render the date of birth field as a calender widget.

https://stackoverflow.com/questions/1898544/django-template-slice-reversing-order
I learned how to display a list in reverse order.

https://stackoverflow.com/questions/43974983/how-to-iterate-python-django-loop-for-n-times-in-template
I learned about the the |slice filter so that I could only display the first 3 objects in a for loop.

https://stackoverflow.com/questions/66296575/how-to-get-time-elapsed-since-creation-date-of-an-objectpost-in-django
I learned how to display "created" as "time elapsed" since created.

https://stackoverflow.com/questions/12233210/math-on-django-templates
I learned how to create a custom template tag to perform a math operation in the template.

https://mdbootstrap.com/docs/standard/extended/scroll-div/
I learned how to create a scrollable div. I used this for the comments on the Twit detail view.

https://www.valentinog.com/blog/testing-django/#testing-a-many-to-many-relationship
I learned a method for testing M2M fields.

https://www.w3resource.com/jquery-exercises/part1/jquery-practical-exercise-9.php
Using the jQuery snippet shown in this tutorial to add a "characters remaining" count to various text fields.

https://stackoverflow.com/questions/4565381/scrolltop-jquery-scrolling-to-div-with-id
https://stackoverflow.com/questions/2369081/how-to-scroll-to-top-of-a-div-using-jquery
https://mdbootstrap.com/snippets/standard/mdbootstrap/2964350#js-tab-view
https://www.youtube.com/watch?v=FixZpR7TWTc
https://www.youtube.com/watch?v=AwgODLLSgwU
From these videos/posts, I learned how to write a jQuery script that scrolls to the top of a div. 

https://stackoverflow.com/questions/5777674/how-can-i-clear-the-input-text-after-clicking
I learned how to clear the input of a text field.

https://stackoverflow.com/questions/72755101/pass-html-for-value-to-django-view-for-querying-database-models?rq=3
From this post, I finally learned what I needed to do in order to enable comment submission from a "list view". Specifically, I needed to know how to pass a parameter into the form for submission, so that the comment could be added. Since there's no url change when using the comment submission form from the list view, I had to find another means of attaching the twit to the comment. After 4 days of research, this was the solution that finally worked for me.

https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django
Learned how to do placeholder text in form.

https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#date
I learned how to display, and compare times in specific increments - example: {{ twit.created|date:"m/d/y H:i:s"}} - which enabled me to solve a problem.

## Known Problems, Issues, And/Or Errors in the Program
On the home page, the template renders out a modal for each Twit. I don't think this is the most optimal way of doing things. This would cause a lot of loading time if there were lots of twits in the database, since it would be rendering modals for each twit. (Perhaps pagination would be a good idea...?)

My "characters remaining" javascript doesn't update automatically when you change a textarea. For example, if I start typing on one textarea, but then go to the next textarea, it still has the same value from the previous textarea - until I start typing again - then it updates. 

