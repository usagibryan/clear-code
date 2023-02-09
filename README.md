# Calculator

The basic setup was made following the tutorial [Introduction to GUIs in Python with PyQt5](https://youtu.be/8jrEVihl-E4) by [Clear Code](https://www.youtube.com/c/ClearCode).

## Changes Made
* Re-arranged buttons
* Added decimal point button
* Disabled user from typing in field
* Added keyPressEvent function so keyboard can be used
* Enter evaluates the expression
* Delete key clears the field
* Changed font and text size
* Created fixed size to prevent re-sizing of window
* Added error handling so that it doesn't crash if you press enter when the field is empty or an operator is at the end
* Changed style to 'Windows'

## Improvements to Make / Bugs to Fix
* Add history
* Add more features such as exponents, square roots, change sign buttons, etc.
* Fix backspace problem
* More elegant solution to error handling
* Prevent user from typing in more than one operator at a time