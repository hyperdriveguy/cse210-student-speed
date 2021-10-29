# Speed
Think you can type faster than your peers? Start a <i>Speed</i> 
tournament and you'll know! The rules are simple. Type the words you 
see as they move across the screen. Press enter to clear the buffer at 
any time. Type a word correctly and your score goes up.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed 
and running on your machine. You can install Asciimatics by opening a terminal 
and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 speed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- speed               (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

### Class Structure
| Class                                         | Description                                              | Stereotypes        | Public Methods                                                                   | Dependencies                         |
| --------------------------------------------- | -------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------- | ------------------------------------ |
| Director                                      | Controls play sequences.                                 | Controller         | start\_game                                                                      | All Local Classes                    |
| Point                                         | Holds information for the position of the word.          | Information Holder | get\_x<br>set\_x<br>get\_y<br>set\_y<br>add<br>equals<br>velocity                |                                      |
| Word                                          | Holds information for a given word on screen.            | Information Holder | (All Point Methods)<br>compare\_word<br>length                                   | Point (Inherited)                    |
| CurWords                                      | Contains information for all words on screen.            | Information Holder | check\_word\_match<br>add\_word<br>remove\_word                                  | WordListService (Inherited?)<br>Word |
| InputService                                  | Detects player input and translates keypresses.          | Service Provider   | get\_letter<br>get\_key                                                          |                                      |
| OutputService                                 | Sends outputs to the console.                            | Service Provider   | clear\_screen<br>place\_word<br>del\_word<br>flush\_buffer                       |                                      |
| FileService                                   | Handles file inputs and outputs.                         | Service Provider   | read\_file\_line<br>read\_whole\_file<br>write\_file\_line<br>write\_whole\_file |                                      |
| WordListService                               | Fetches words from given wordlists to put on the screen. | Service Provider   | get\_new\_word                                                                   | FileService (Inherited)              |
| SettingsService<br>(For Stretch Requirements) | Gets persistent user data and settings.                  | Service Provider   | get\_hi\_score<br>get\_game\_mode                                                | FileService (Inherited)              |

## Required Technologies
---
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
---
* Carson Bush - hyperdriveguy@byui.edu
