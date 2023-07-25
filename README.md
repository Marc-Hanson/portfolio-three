# A Day In The Life

## A day in the life is a text adventure which allows the player to experience a day in the life of a full stack software development student. It has two main forks following a good day or a bad day, both of which have successful and unsuccessful endings. The user is given select keywords to progress to the next node which are highlighted in green.

#### Live Site [Here](https://a-day-in-the-life-ae933bba8572.herokuapp.com/)

#### How to play
- Keywords are highlighted using a green colour and are contained in single quotes.
- Enter one of the highlighted keywords from the text to continue in the story.
- To begin playing the user must type the 'ready' keyword.
- You can quit at any time using the 'quit' keyword.
- After entering a keyword you progress to the next node, or reach a dead end.
- After reaching a successful or unsuccessful ending you are asked if you would like to try again.

## Features
- Upon running the game you are greeted with a picture of a keyboard and screen is ASCII art format. 
![alt text](assets/readme/ascii.jpg)

- All 3 options are working answers and have small custom messages, and once 'ready' is entered the game will begin. Other responses will give the user feeedback to provide a different answer.
![alt text](assets/readme/ready.jpg)

- Once 'ready' is entered the game will begin and the story starts.
![alt text](assets/readme/game_started.jpg)

- All inputs are checked and feedback is given to the player incase of mistakes. 
![alt text](assets/readme/wrong.jpg)

- All notes and comments in the run.py file follow the projects map which is provided in both the assets file as well as below. The 'good day' path is on the right side of the map, and the 'bad day' path is taken through the left side.
![alt text](assets/readme/the_map.jpg)


## Technologies used
- Languages:
1. `Python`

## Frameworks, Deployement & Libraries

* [Github](https://github.com/)

* [CodeAnywhere](https://app.codeanywhere.com/)

## Testing

* Testing was carried out constantly in the terminal as well as using Python debugger.
* After deployment text was modified to fit the 80 character wide window since hidden text is included in CI Linters character counter.

## Accessibility

* The whole project was built using python. No other languages were used.

## Issues and bugs

* None.

## Fixed bugs

* Countless bugs involving new lines and formatting were found and corrected after deployment.
* Colorama would not add to requirements through terminal so the file was modified manually.
* Indentation and white space errors were caught by CI Linter and corrected.

## Validator Testing
The project was ran through [](https://pep8ci.herokuapp.com/)
![alt text](assets/readme/linter.jpg)

## Deployment

This project was deployed using Code Institute's Heroku terminal.

- Clone this repository.
- Create a new Heroku app.
- When you create the app, you will need to add two buildpacks from the _Settings_ tab.
1. `heroku/python`
2. `heroku/nodejs`
- Link the Heroku app to the repository.
- Click Deploy.

## Credits
https://www.ascii.co.uk/art/ was used for inspiration for the keyboard/screen image.