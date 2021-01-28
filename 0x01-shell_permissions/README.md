# shell permissions 

0. My name is Betty - script that changes your user ID to betty.
1. Who am I - script that prints the effective userid of the current user.
2. Groups - script that prints all the groups the current user is part of.
3. New owner - script that changes the owner of the file hello to the user betty.
4. Empty! - script that creates an empty file called hello.
5. Execute - script that adds execute permission to the owner of the file hello
6. Multiple permissions - script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
7. Everybody! - script that adds execution permission to the owner, the group owner and the other users, to the file hello
8. James Bond - this had a sense of humor :) . script that sets the permission to the file hello as follows:Owner: 
    no permission at all
    Group: no permission at all
    Other users: all the permissions
9. John Doe - script that sets the mode of the file hello to this:
    -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
10. Look in the mirror - script that sets the mode of the file hello the same as olleh’s mode.
11. Directories -  script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not      be changed.
12. More directories - script that creates a directory called dir_holberton with permissions 751 in the working directory.
13. Change group -  script that changes the group owner to holberton for the file hello
14. Owner and group - script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
15. Symbolic links - script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
16. If only - script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
