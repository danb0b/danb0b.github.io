---
title: Using Github with two accounts
tags:
  - git
  - github
  - bash
  - linux
  - ubuntu
---



## Instructions

1. Create a new, separate key for each github account


    follows this tutorial: <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>
    
    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    
    and follow the prompts.  USE A PASSPHRASE.  Or do it in one line, with filename and passphrase supplied
    
    ```bash
    ssh-keygen -t ed25519 -C "user1_email@corporate.com" -f /the/path/to/user1_github_key -N my_passphrase_here
    ssh-keygen -t ed25519 -C "user2_email@personal.com" -f /the/path/to/user2_github_key -N my_passphrase_here
    ```

1. Add each key to each github account
    
    Uses: <https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/>

    1. Log in
    1. Go to profile-->settings-->"SSH and GPG keys"-->"Add New"
    1. Give it a name (like the filename you created) and paste in the public key
    1. Repeat adding each key to each github account

1. Create/edit your ~/.ssh/config file

Note: I have the following settings at the top of my config file to make it more secure:

```
AddKeysToAgent yes

Host *
   IdentitiesOnly yes
   PreferredAuthentications publickey 
   #...and other settings
```

Then I add the following.  To ensure the gitman package is setup correctly, make sure user1 and user2 are your _actual_ github usernames

```
Host user1.github.com
   HostName github.com
   User git
   IdentityFile /the/path/to/user1_github_key
   
Host user2.github.com
   HostName github.com
   User git
   IdentityFile ~/the/path/to/user2_github_key
```

## External References:

* <https://gist.github.com/oanhnn/80a89405ab9023894df7>
* <https://jeffbrown.tech/multiple-github-accounts-ssh/>
* <https://www.section.io/engineering-education/using-multiple-ssh-keys-for-multiple-github-accounts/>
* <https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca>
* <https://stackoverflow.com/questions/3225862/multiple-github-accounts-ssh-config>