# shell variables and expansions
This topic was aimed at understanding the following:-

### General
* What happens when you type $ ls -l *.txt

### Shell Initialization Files
* What are the /etc/profile file and the /etc/profile.d directory
* What is the ~/.bashrc file

### Variables
* What is the difference between a local and a global variable
* What is a reserved variable
* How to create, update and delete shell variables
* What are the roles of the following reserved variables: HOME, PATH, PS1
* What are special parameters
* What is the special parameter `$?`?

### Expansions
* What is expansion and how to use them
* What is the difference between single and double quotes and how to use them properly
* How to do command substitution with `$()` and backticks

### Shell Arithmetic
* How to perform arithmetic operations with the shell

### The alias Command
* How to create an alias
* How to list aliases
* How to temporarily disable an alias

The following task files were used in understanding the concepts better
## 0-alias
Create a script that creates an alias.
## 1-hello_you
script that prints hello user, where user is the current Linux user.
## 2-path
Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
## 3-paths
Create a script that counts the number of directories in the PATH.
## 4-global_variables
script that lists environment variables.
## 5-local_variables
script that lists all local variables and environment variables, and functions.
## 6-create_local_variable
script that creates a new local variable.
## 7-create_global_variable
script that creates a new global variable.
## 8-true_knowledge
script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
## 9-divide_and_rule
script that prints the result of POWER divided by DIVIDE, followed by a new line.
## 10-love_exponent_breath
script that displays the result of BREATH to the power LOVE
## 11-binary_to_decimal
Those who understand binary, and those who don't - script that converts a number from base 2 to base 10.
## 12-combinations
script that prints all possible combinations of two letters, except oo.
## 13-print_float
script that prints a number with two decimal places.
## 14-decimal_to_hexadecimal
script that converts a number from base 10 to base 16.
## 100-rot13
script that encodes and decodes text using the rot13 encryption. Assume ASCII.
## 101-odd
script that prints every other line from the input, starting with the first line.
## 102-water_and_stir
shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result
