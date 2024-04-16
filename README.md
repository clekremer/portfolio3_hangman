# Hangman Game

The game is based on the typical Hangman word guess principle. It´s a terminal game hosted Heroku and written in Python. For each wrong guess the gallow is build up and stickman is going to be hung up. You have 7 attempts to guess to correct word. 
![Image of landing page]()
[url to prod site](https://portfolio3-hangman-3c9d3306a756.herokuapp.com/)


## User Experience
Aim of this project is to provide an easy to handle and easy to use guess game for the interested user.

### User Stories
 - As a user I want to easily understand the idea and instructions of the game
 - As a user I want to have the possibility to skip the instructions because everyone knows the rules for Hangman 
 - As a user I want to have a seamless game flow and direct feedback from the software in case of incorrect inputs (validation of input)
 - As a user I want to directly understand if my guess was correct or wrong
 - As a user I want to see the progress of the game 
 - As a user I want to know which letters I have already used
 - As a user I want to have the possibility to restart the game or play it again


## Process diagram / Flowchart
The diagram shows the following steps:
- xxx
![Diagram]()

## Wordart/Fonts
I used the font "acrobatic" font from figlet (http://www.figlet.org/fontdb_example.cgi?font=acrobatic.flf). It based on stickman figures, so it matches very well to the idea of the game.

## Features
### Existing features
The starting screen, should give a non verbal direct Idea about what the game is about. It shows the titel of the game "Hangman" in stickman fonts. So every user who knows Hangman directly understand that this is a hangman guessing game. If as user don´t knows Hangman he has the option to read the instruction.


![Landing page]()

* Instruction
    * xxx

![Introduction]()

* Gameplay 
    * xxxx

![Gamplay]()

* End of game
    * xxxx

![End of game]()) 

### Future Features
 * 

## Testing
### Manual testing
Test Cases

### Automated testing
Code Institutes  validator https://pep8ci.herokuapp.com/ to check the code automatically.
![Screenshot validator]()
## Technologies Used
* Languages: 
    * Python
* Libraries:
    * random to randomize the guess word
    * os for the clear function to clear the terminal
* Others:
    * Github as repository
    * Heroku as dpeloyment platform to host the live version 
    * pyfiglet
    * Flowchart 
## Bugs
### Fixed bugs

### Remaining bugs


## Deployment
 The app was deployed through Heroku. The steps are as following:

1. Create new app in Heroku
2. Add unique name for the app and select Europe as region and click "Create app".
3. In settings add buildpacks for `Python` and `NodeJS`(Config_vars were not required for the game.).
4. In "Deploy-Tab" select GitHub as deployment method and connect the Github repository with Heroku
5. For the initial deployment I used manual deployment; afterwards I enabled automatic deployment. So deployment happens automatically with the execution of every "git push" command.  
## Credits
### Code
* 
* 
### Acknowledgements