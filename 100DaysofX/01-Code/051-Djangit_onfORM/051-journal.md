# 2019-04-23 | #100DaysofCode

## Day 051 / 100

---

## SELECT * FROM Project

### Project.abstract

    GOAL_onfORM : A simple form-based application for PDF generation  

### Project.loxocache(2019-04)

    LVL0_050 : Deploy to production server  
        TASK_050 : Install the Postgres.app CLI Tools / Configure $PATH  
        TASK_050 : $ pip install -r requirements.txt  
        TASK_050 : Complete prerequisites for deployment  

    LVL1_050 : Implement email with SendGrid  
    LVL1_050 : Create user account for jeffco  
    LVL1_044 : Ask if billing address is the same, if so, fill in automatically  

    LVL2_050 : Add success message to orderdetail  
    LVL2_050 : Randomish numbering scheme for orders  
    LVL2_050 : Fix labels on OrderFormView  
    LVL2_050 : Serialize model data + display PDF  

    LVL3_050 : render_pdf.js - loop through field_data for drawText  

--------ø--------

## SELECT * FROM Session

### Session.abstract

    GOAL_051 : Deploy v1.0 to Production  

#### Session.cache

- pass

---

## Session.journal(2019-04-23)

### Loxocache

--------ø--------

### 10:18 ~ Session.init

I've been doing some research on what method to use for deployment but ramped up that research recently for obvious reasons. I've come to the flippy-flop drop top conclusion (for now...read: flippy-flops) that doing a linux server is actually the way to go for this app.

Having our own linux server to use will make things much more flexible and powerful overall, without having to connect up a AWS bucket to heroku and all that.

I also want to learn as much as possible about using linux servers. This is the perfect opportunity to begin that journey.

---

### 10:18 ~ Linode Setup

Maybe I'm a little biased because Corey Schafer has [a tutorial on deploying with Linode](https://youtu.be/Sa_kQheCnds). Great to support him by using his code, as his tutorials have been so valuable to me.

Created a new nanode with Ubunto 19.04 at a datacenter in Dallas, TX.

> Linodes > Networking > Access Panel > SSH Access

For some reason when connecting to the server via SSH, it kept throwing an error:

    root@*****'s password:
    Permission denied, please try again.

Reset the root password to try again...

I'm in.

    Welcome to Ubuntu 19.04 (GNU/Linux 5.0.0-13-generic x86_64)
    ...
    System information as of Tue Apr 23 17:11:32 UTC 2019
    ...
    root@localhost:~#

----ø----

#### Install software updoots

    root@localhost:~# apt-get update && apt-get upgrade
    Get:1 http://mirrors.linode.com/ubuntu disco InRelease [257 kB]
    ...
    Get:24 http://security.ubuntu.com/ubuntu disco-security/multiverse amd64 c-n-f Metadata [116 B]
    Fetched 510 kB in 1s (605 kB/s)
    Reading package lists... Done
    ...
    Processing triggers for man-db (2.8.5-2) ...

----ø----

#### Set hostname of the server

    root@localhost:~# hostnamectl set-hostname onformer
    root@localhost:~# hostname
    onformer

----ø----

#### Set hostname in hostfile

> /etc/hosts

    root@localhost:~# nano /etc/hosts
    127.0.0.1       localhost
    ***.**.***.*    onformer

----ø----

#### Set up a new limited user

    # Creating new user
    root@localhost:~# adduser onformator
    Adding user `onformator' ...
    ...
    New password:
    ...
    Changing the user information for onformator
        Full Name []: Onform Admin

    # Give sudo POWERS!
    root@localhost:~# adduser onformator sudo
    Adding user `onformator' to group `sudo' ...
    Adding user onformator to group sudo
    Done.

    # Log out of server
    root@localhost:~# exit
    logout
    Connection to **.**.**.** closed.

    # Log back in as onformator
    $ ssh onformator@**.**.**.**
    onformator@**.**.**.**'s password:
    Welcome to Ubuntu 19.04 (GNU/Linux 5.0.0-13-generic x86_64)

----ø----

#### Sshetting up SSH

    # On the server
    onformator@onformer:~$ pwd
    /home/onformator

    onformator@onformer:~$ mkdir -p ~/.ssh

    onformator@onformer:~$ ls -la
    total 32
    drwxr-xr-x 5 onformator onformator 4096 Apr 23 17:45 .
    drwxr-xr-x 3 root       root       4096 Apr 23 17:29 ..
    -rw-r--r-- 1 onformator onformator  220 Apr 23 17:29 .bash_logout
    -rw-r--r-- 1 onformator onformator 3771 Apr 23 17:29 .bashrc
    drwx------ 2 onformator onformator 4096 Apr 23 17:41 .cache
    drwx------ 3 onformator onformator 4096 Apr 23 17:41 .gnupg
    -rw-r--r-- 1 onformator onformator  807 Apr 23 17:29 .profile
    drwxrwxr-x 2 onformator onformator 4096 Apr 23 17:45 .ssh

    # On my local machine
    # List out any existing keys (which I do)
    $ ls ~/.ssh/id_rsa*
    /Users/Tobias/.ssh/id_rsa     /Users/Tobias/.ssh/id_rsa.pub

    # Copy public key to server
    $ scp ~/.ssh/id_rsa.pub onformator@**.**.*.*:~/.ssh/authorized_keys
    onformator@**.**.*.*'s password:
    id_rsa.pub                      100%  735    10.6KB/s   00:00

    # Back on the server
    onformator@onformer:~$ ls .ssh
    authorized_keys

    # Setting up permissions for ssh
    onformator@onformer:~$ sudo chmod 700 ~/.ssh/
    [sudo] password for onformator:
    onformator@onformer:~$ sudo chmod 600 ~/.ssh/*

    # 7 0 0
        # 7 - r/w permissions for owner
        # 0 - Nada for group
        # 0 - Nada for everyone else

    # Testing out the ssh connection
    $ ssh onformator@**.**.**.**
    Welcome to Ubuntu 19.04 (GNU/Linux 5.0.0-13-generic x86_64)

----ø----

#### Best Practices: SSH Config

    # Modify sshd_config
    # Disallow root login and password auth
    onformator@onformer:~$ sudo nano /etc/ssh/sshd_config
    ...
    PermitRootLogin no
    ...
    PasswordAuthentication no

    # Restard ssh service to apply changes
    onformator@onformer:~$ sudo systemctl restart sshd

----ø----

#### Firewall

    # Install ufw - uncomplicated firewall
    onformator@onformer:~$ sudo apt-get install ufw
    ...
    ufw is already the newest version (0.36-1ubuntu1).
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

    # Set up basic rules
    # Allow outgoing
    onformator@onformer:~$ sudo ufw default allow outgoing
        Default outgoing policy changed to 'allow'
        (be sure to update your rules accordingly)

    # Deny incoming will lock me out of server
    # unless rule is set to allow ssh
    onformator@onformer:~$ sudo ufw default deny incoming
        Default incoming policy changed to 'deny'
        (be sure to update your rules accordingly)

    # Allow ssh
    onformator@onformer:~$ sudo ufw allow ssh
    Rules updated
    Rules updated (v6)

    # Allow Django dev server port
    onformator@onformer:~$ sudo ufw allow 8000
    Rules updated
    Rules updated (v6)

    # Enable firewall
    onformator@onformer:~$ sudo ufw enable
    Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
    Firewall is active and enabled on system startup
    onformator@onformer:~$ sudo ufw status
    Status: active

    # Port 22 is the SSH connection / port
    To                         Action      From
    --                         ------      ----
    22/tcp                     ALLOW       Anywhere
    8000                       ALLOW       Anywhere
    22/tcp (v6)                ALLOW       Anywhere (v6)
    8000 (v6)                  ALLOW       Anywhere (v6)

---