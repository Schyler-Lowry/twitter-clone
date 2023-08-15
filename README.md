# twitter-clone
This was a project for my web development class at my college. We had to design a twitter clone (called "Tweeter"). It features full CRUD operations, elegant styling (at least I'd like to say it does), and connects with a PostgreSQL database.

## Example Screenshots:

#### Login
![Login](https://i.imgur.com/KY5N2WP.png)

#### Signup
![Signup](https://i.imgur.com/Qsd6Umg.png)

#### Home page/main feed (scrolled to bottom)
![homepage](https://i.imgur.com/DLfJjpI.png)

#### User profile page (displays all twits from this user)
![userprofile](https://i.imgur.com/MKg7M3O.png)

#### Write a new twit
![newtwit](https://i.imgur.com/8BUPl2p.png)

#### Edit a twit
![twitedit](https://i.imgur.com/dPfCayZ.png)

#### Post a comment
![comment](https://i.imgur.com/Jsk5TDb.png)

#### Twit detail page with commments
![twitdetail](https://i.imgur.com/j3L0LmI.png)



#### The following section was copied from the original assignment readme:
## Known Problems, Issues, And/Or Errors in the Program
On the home page, the template renders out a modal for each Twit. I don't think this is the most optimal way of doing things. This would cause a lot of loading time if there were lots of twits in the database, since it would be rendering modals for each twit. (Perhaps pagination would be a good idea...?)

My "characters remaining" javascript doesn't update automatically when you change a textarea. For example, if I start typing on one textarea, but then go to the next textarea, it still has the same value from the previous textarea - until I start typing again - then it updates. 

The other main issue is that it looks awful on mobile. Actually, it's practically unusable. Now I need to learn how to edit for mobile too....