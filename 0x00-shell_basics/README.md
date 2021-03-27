# learning about shell basics
Topic aim was to understand several concepts on shell basics, such as:-
### General
* What does RTFM mean?
* What is a Shebang

### What is the Shell
* What is the shell
* What is the difference between a terminal and a shell
* What is the shell prompt
* How to use the history (the basics)

### Navigation
* What do the commands or built-ins cd, pwd, ls do
* How to navigate the filesystem
* What are the . and .. directories
* What is the working directory, how to print it and how to change it
* What is the root directory
* What is the home directory, and how to go there
* What is the difference between the root directory and the home directory of the user root
* What are the characteristics of hidden files and how to list them
* What does the command cd - do

### Looking Around
* What do the commands ls, less, file do
* How do you use options and arguments with commands
* Understand the ls long format and how to display it
* A Guided Tour
* What does the ln command do
* What do you find in the most common/important directories
* What is a symbolic link
* What is a hard link
* What is the difference between a hard link and a symbolic link

### Manipulating Files
* What do the commands cp, mv, rm, mkdir do
* What are wildcards and how do they work
* How to use wildcards

### Working with Commands
* What do type, which, help, man commands do
* What are the different kinds of commands
* What is an alias
* When do you use the command help instead of man

### Reading Man Pages
* How to read a man page
* What are man page sections
* What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash
* Common shortcuts for Bash

### LTS
* What does LTS mean?


## 0-current_working_directory
script that prints the absolute path name of the current working directory
## 1-listit
contents list of your current directory.
## 2-bring_me_home
script that changes the working directory to the user’s home directory
## 3-listfiles
Display current directory contents in a long format
## 4-listmorefiles
Display current directory contents, including hidden files (starting with .). Use the long format.
## 5-listfilesdigitonly
Display current directory contents.
## 6-firstdirectory
Script that creates a directory named holberton in the /tmp/ directory.
## 7-movethatfile
Move the file betty from /tmp/ to /tmp/holberton.
## 8-firstdelete
Deletes the file betty.
## 9-firstdirdeletion
Delete the directory holberton that is in the /tmp directory.
## 10-back
Write a script that changes the working directory to the previous one.
## 11-lists
script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
## 12-file_type
script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
## 13-symbolic_link
symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
## 14-copy_html
script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
## 15-lets_move
Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
## 16-clean_emacs
script that deletes all files in the current working directory that end with the character ~.
## 17-tree
script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
## 18-commas
command that lists all the files and directories of the current directory, separated by commas (,).
