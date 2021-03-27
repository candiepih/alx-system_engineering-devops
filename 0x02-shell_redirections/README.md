# Shell, I/O Redirections and filters
This topic aimed at understanding the following:-
### Shell, I/O Redirection
* What do the commands head, tail, find, wc, sort, uniq, grep, tr do
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* How to combine commands and filters with redirections

### Special Characters
* What are special characters
* Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

### Other Man Pages
* How to display a line of text
* How to concatenate files and print on the standard output
* How to reverse a string
* How to remove sections from each line of files
* What is the /etc/passwd file and what is its format
* What is the /etc/shadow file and what is its format

After reading about the topic the following task files helped to test my understanding on the various areas.
## 0-hello_world
script that prints “Hello, World”, followed by a new line to the standard output.
## 1-confused_smiley
script that displays a confused smiley "(Ôo)'.
## 2-hellofile
Display the content of the /etc/passwd file.
## 3-twofiles
Display the content of /etc/passwd and /etc/hosts
## 4-lastlines
Display the last 10 lines of /etc/passwd
## 5-firstlines
Display the first 10 lines of /etc/passwd
## 6-third_line
script that displays the third line of the file iacta. The file `iacta` is be in the working directory.
* Not allowed to use sed

## 7-file
shell script that creates a file named exactly `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)` containing the text Holberton School ending by a new line.
## 8-cwd_state
script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
## 9-duplicate_last_line
script that duplicates the last line of the file `iacta`
* The file iacta is in the working directory

## 10-no_more_js
script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
## 11-directories
script that counts the number of directories and sub-directories in the current directory.
* The current and parent directories should not be taken into account
* Hidden directories should be counted

## 12-newest_files
script that displays the 10 newest files in the current directory.
##### Requirements:
      * One file per line
      * Sorted from the newest to the oldest

## 13-unique
script that takes a list of words as input and prints only words that appear exactly once.
      * Input format: One line, one word
      * Output format: One line, one word
      * Words should be sorted

## 14-findthatword
Displays lines containing the pattern “root” from the file /etc/passwd
## 15-countthatword
Display the number of lines that contain the pattern “bin” in the file /etc/passwd
## 16-whatsnext
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
## 17-hidethisword
Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
## 18-letteronly
Display all lines of the file /etc/ssh/sshd_config starting with a letter.
       * includes capital letters as well

## 19-AZ
Replace all characters A and c from input to Z and e respectively.
## 20-hiago
Create a script that removes all letters c and C from input.
## 21-reverse
script that reverse its input.
## 22-users_and_homes
script that displays all users and their home directories, sorted by users.
       * Based on the the /etc/passwd file
