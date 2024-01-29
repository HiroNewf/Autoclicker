# Autoclicker
## Table of Contents 
* [Description](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#desciption)
* [Installation](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#installation)
  * [Windows](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#windows)
  * [Linux](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#linux)
* [Usage](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#linux)
* [License](https://github.com/HiroNewf/Autoclicker/blob/main/README.md#linux)
## Description
This is a basic autoclicker tool that works on both Windows and Linux operating systems. This autoclicker will allow you to select any keyboard or mouse input and have it be repeted for a given number of times or indefinitely. You will also be able to set the amount of time between each key press within the *very* high quality GUI. 
## Installation
### Windows
> Note: this application was made with Windows 10 in mind, it *should* work on Windows 11, but this has not been tested. 
1. Download the most recent .exe file from the [Releases](https://github.com/HiroNewf/Autoclicker/releases) section of this github page.
2. Open the application.
### Linux
1. Clone the github repo `git clone https://github.com/HiroNewf/Autoclicker.git`.
2. Move into the directory for the cloned repo `cd Autoclicker`.
3. Install the requirements `pip install -r requirements.txt`.
4. Run the python script `python3 autoclicker.py`.
## Usage
> Note: upon opening the application a command line window will also open, this can be mostly ignored but may provide some useful debugging / troubleshooting information if you are having trouble using the application.  Additionally if you sumbit an issue for this application please include any text from this command line to help me resolve your issue easier. 
1. Upon opening the application there are only a few inputs / buttons presented to the user, the first of which being a `Button` field. Here you will enter the button you wish to have the autoclicker repeatedly press. Inputs like "1, f, F6, & right" are accepted. For the mouse buttons use the keywords right, left, & middle. 
2. After you have set your button you may set the `Press Interval`. Whole numbers and decimal numbers are accepted in this field and the Interval is in the form of seconds. Some example of inputs would be "1, 0.5, 0.002". Please note that if you try and the have the program enter in key presses too quickly it may crash the program and/or the application you are trying to input the text into, so if you are having stability issues please try and increase the time between button presses.
3. After you have set the Press Interval you can then tell the application rather you want it to press the button until the `Stop` button is pressed with the `Repeat Forever` option or you can set a given number of times the button will be pressed with the `Repeat ___ Times` button. If you choose the later, upon pressing the button a new small window will pop up in which you can enter the number of button presses that you desire (Up to 999).  
4. Once all of your options are set you can press the `Start` button to start the autoclicker. The input fields will be locked while the autoclicker is running, but once the `Stop` button is hit or your set number of presses is reached the input fields will be unlocked again. 
## License 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/
