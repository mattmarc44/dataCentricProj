deployed via heroku (automatic github integration)

https://tapes-film-reviews.herokuapp.com/

# Tapes Film Reviews

Tapes is a community orientated film review site, relying on posts from users to make new entries. The aim is to generate pages dynamically using a python and flask backend routing. It is used to get movie descriptions and details, like who made it and what it's about. Each entry also contains a star rating on a scale of five.

It is possible to refine your search by genre and all results will give a brief overlay. When on selection of a movie you are directed to a more detailed overview.
 
## UX
 
#### Strategy
- Dynamically generated website to demonstrate CRUD functionality.
- goals:
    ..* Provide a list of films with descriptions and ratings.
    ..* Provide an ability to add more, edit or delete films from the list.
    ..* Potentially use these entries to create sale revenue by introducing a link to buy or rent.

Target audience = film buffs
Focus = create a collection of movies for browsing.
Definition = A film review site.
value = Information on films to user. Sales for streaming services or similar.

#### User Stories
As a user, I want to watch a film, what can I watch?
As a user, I want to watch a film but only the kind I want right now(genre.)
As a user, I want to know what the film is about before I commit to it.
As a user, I want to know If this film is worth watching (review.)
As a user, I want to add a film suggestion that isn't on the list.
As a user, I want a way to watch the film I'm looking at.
As a movie producer, I want a way to publicise/sell my work.
As a critic, I want to be able to comment on a film.
As a critic, I want to be able to leave my own rating of a film.
As a user, I want to be able to see the collective rating of everyone who contributed.

#### Scope
##### Planned features priority 1-3
-Home page with whole collection = 1
-Movie specific pages dynamically created = 1
-CRUD functionality = 1
-Star rating system = 1
-Search function = 2
-Genre listings = 2 
-Sale options = 3 (more theoretical, for example a link on a movie page that redircts to a streaming service. The link could be generated to a search page from the streaming site matching titles of the same name for example.)
-Comment functionality = 3 (Not necessary for main foccus but nice for users and community aspect.)

#### wireframe
The wireframe in this project is attached to the directory under wireframe. It is a PDF.

NOTE: I would like to expand on wireframes in the future. Invest in proper wireframe making tech as free sources are quite limited in what you can do. Albeit this does leave some room for flexibility later in the project.

## Features

- Genre Selection: filters options by routing. getting the selected value and matching all films in the database with the selected genre.

- Star rating: The star rating takes a string value from the database. Then using Jquery and a loop inserts a materialise star icon the approopriate amount of times. This solution appeals to me because of simplicity and a chance to practice earlier things I've learnt. (ratings.js)

- Movie pages: All movie pages use routing to get the correct entry and then jinja templating to generate it's relevent page.

- CRUD: all implemented via flask routing and mongo atlas. On update movie, returns the same form from add movie but with fields filledd in. Similar to course.

### Features Left to Implement
- Search function.
- Better way to store images.
- Comments
- group rating

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Sass](https://sass-lang.com/)
    - Sass is used for styling as I find its use of mixins, nesting and ways if creating mediaqueries a huge asset.
- [Flask/Jinja](http://flask.palletsprojects.com/en/1.1.x/, https://jinja.palletsprojects.com/en/2.10.x/)
    - Flask and jinja were used for back-end and templating.
- [Python](https://www.python.org/)
    - Python was used as the main language.
- [MongoDB](https://www.mongodb.com/)
    - Used for database as taught.
- [Materialize](https://materializecss.com/)
    -I decided to use materialize as the front end framework as with sass I could change it's main color scheme to fit mine by quickly changing its sass variables. This minimised overriding to many of its classes. Also many other helpers. like its grid helps.
- [unittest](https://docs.python.org/2/library/unittest.html)
    - unittest was used for testing. I saw this as the best option available.

## Testing

Automated testing is conducted through python unittest. Although this is still quite simple as I find there to be a huge gap between any simple tutorials and building a proper project. I will continue to look into this and develop.

It mostly relies on setting up certain routing ooptions and verifying the result.
naturally, this would leave room for failures with continued changes. As such, I have manually tested also. 

All CRUD functionality was tested in app as well and then compared to mongodb for any unexpected errors or differences. 

1. Home page:
    1. Go to the home page.
    2. Check list populates and layout presentable on all screen sizes.
    3. Ensure each card displays with its relevent information with no duplicates or unexpected errors. 
    4. Ensure images display on cards and if no image is supplyed then the default placeholder image.
    5. Check pagination links work in both directions. Top and bottom links.
    6. Card buttons are redirecting to correct pages.

2. Movie pages:
    1. Go to movie page.
    2. Check information is displayed correctly on all screen sizes and is correct relevent to the selection made.
    3. Check star ratings are displaying.
    4. Check edit button directs you to a prepopulated form with this films info.
    5. Check delete function redirects you to the homepage. That movie should no longer display. Confirm by using mongo dashboard to inspect collection.

3. Add/Update pages:
    1. Go to add/update page.
    2. Check form displays correctly(with right data if applicable).
    3. Check form validates entries.
    4. Check slider and calender section works.
    5. Check invalid forms don't submit. Check this with several diferent variations.
    6. Check form submits when necessary entries are filled. Check against mongoDB dashboard for errors. Check this with several diferent variations.
    7. Ensure redirects to home page where the relevent info should now display.

4.  General:
    1. check all break points function and displays on different devices on dev tools
    2. rerun previous tests on sizes mobile/tablet.
    3. rerun tests from deployed heroku app.
    4. Send to various family and friends to use. get feedback on anythong broken, feneral feedback.

 - text was contrast checked
 https://webaim.org/resources/contrastchecker/
 - html and css validated.


- issues: 
    -had trouble trying to implement a file upload mechanism to the forms. It would crash when clicked. I think its something to do with materialise as it worked as a standalone item, although I abondoned it before I could use it with the backend, instead choosing to link images via URL's. (there is a solution using base64 and mongo with the form input I believe)

## Deployment

I decided to use heroku to deploy this project and it looks to my github master for the most current version of the site.




## Credits

### Content
references for movie descriptions: 
https://www.rottentomatoes.com/m/shaun_of_the_dead
https://www.rottentomatoes.com/m/hot_fuzz


### photo  creds:
Photo by Amir Ghoorchiani from Pexels
Photo by Skitterphoto from Pexels
Photo by luizclas from Pexels
Photo by Donald Tong from Pexels

### Acknowledgements

- pagination inspired by:https://www.youtube.com/watch?v=Lnt6JqtzM7I
- flask tests inspired by discover flask series: https://www.youtube.com/watch?v=1aHNs1aEATg