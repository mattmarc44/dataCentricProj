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

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### photo  creds:
Photo by Amir Ghoorchiani from Pexels
Photo by Skitterphoto from Pexels
Photo by luizclas from Pexels
Photo by Donald Tong from Pexels

### Acknowledgements

- pagination inspired by:https://www.youtube.com/watch?v=Lnt6JqtzM7I
- flask tests inspired by discover flask series: https://www.youtube.com/watch?v=1aHNs1aEATg

references for movie descriptions 
https://www.rottentomatoes.com/m/shaun_of_the_dead
https://www.rottentomatoes.com/m/hot_fuzz


issues: 
-had trouble trying to implement a file upload mechanism to the forms. It would crash when clicked. I think its something to do with materialise as it worked as a standalone item, although I abondoned it before I could use it with the backend, instead choosing to link images via URL's.


 text was contrast checked
 https://webaim.org/resources/contrastchecker/

 