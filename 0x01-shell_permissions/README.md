# shell permissions 

## 0-iam_betty
script that changes your user ID to betty.
## 1-who_am_i
script that prints the effective userid of the current user.
## 2-groups
script that prints all the groups the current user is part of.
## 3-new_owner
script that changes the owner of the file hello to the user betty.
## 4-empty
script that creates an empty file called hello.
## 5-execute
script that adds execute permission to the owner of the file hello
## 6-multiple_permissions
script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
## 7-everybody
script that adds execution permission to the owner, the group owner and the other users, to the file hello
## 8-James_Bond
I really enjoyed this one :) . script that sets the permission to the file hello as follows:
        * Owner: no permission at all
        * Group: no permission at all
        * Other users: all the permissions
## 9-John_Doe
script that sets the mode of the file hello to this:
```sh

-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

```
## 10-mirror_permissions
script that sets the mode of the file hello the same as olleh’s mode.
## 11-directories_permissions
script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
## 12-directory_permissions
script that creates a directory called dir_holberton with permissions 751 in the working directory.
## 13-change_group
script that changes the group owner to holberton for the file hello
## 14-change_owner_and_group
script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
## 15-symbolic_link_permissions
script that changes the owner and the group owner of the file _hello to betty and holberton respectively
## 16-if_only
script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
