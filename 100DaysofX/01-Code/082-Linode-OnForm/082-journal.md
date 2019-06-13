# 2019-05-24 | #100DaysofCode

    GOAL-05-24 ~ Deploy new changes to the OnForm Linode Server  

## Day 082/100 | 144/365

- [2019-05-24 | #100DaysofCode](#2019-05-24--100daysofcode)
  - [Day 082/100 | 144/365](#day-082100--144365)
  - [14:20 ~ Secure Staphyline](#1420--secure-staphyline)
    - [SSL Certification](#ssl-certification)
    - [Get Started](#get-started)
      - [LVL1-OnForm : Set up Django Logging](#lvl1-onform--set-up-django-logging)
      - [Allow HTTPS (and TCP?)](#allow-https-and-tcp)
    - [21:16 ~ Other Riziform Rivage](#2116--other-riziform-rivage)
      - [IDEA-AptDraft : Generate PDF art using text as an input (and output - generative word maps)](#idea-aptdraft--generate-pdf-art-using-text-as-an-input-and-output---generative-word-maps)
    - [22:42 ~ Organization Gyrostatics](#2242--organization-gyrostatics)
    - [23:14 ~ API - Acatamathesiastic Psychotaxis Ivresse](#2314--api---acatamathesiastic-psychotaxis-ivresse)
    - [23:46 ~ Checking the Castrametation](#2346--checking-the-castrametation)

---- Tasks ----

    LVL1-OnForm : Set up [Django Logging](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#logging)  

---- Notes ----

    IDEA-AptDraft : Generate PDF art using text as an input (and output - generative word maps)  

---- Resources ----

- [CertBot StackOverflow post](https://stackoverflow.com/questions/47803081/certbot-apache-error-name-duplicates-previous-wsgi-daemon-definition?rq=1)
- [The https section of the Django Docs](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#https)
- [Apache Docs](https://httpd.apache.org/docs/2.4/)
- [Set up ufw to accept https traffic](https://www.linode.com/docs/security/securing-your-server/)
- [Digital Ocean Firewall Essentials](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands).

---- Selects ----

- [Arrested Development](https://en.wikipedia.org/wiki/Arrested_development)

---- Sojourn ----

## 14:20 ~ Secure Staphyline

Staphyline: Like a bunch of grapes.
Stasimorphy: Structural modification by [arrested development](https://en.wikipedia.org/wiki/Arrested_development).

    In anthropology and archaeology, the term "arrested development" means that a plateau of development in some sphere has been reached.

### SSL Certification

Time to get going on that ssl token. [I wish I had used Ubuntu 18.04](https://certbot.eff.org/lets-encrypt/ubuntuother-apache) for the server, but oh well. This will be fun! Learning all the time.

First, I'm going to update the server's OS with any patches and such...

    onformator@onformer:~$ sudo apt-get update
    [sudo] password for onformator:
    Hit:1 http://mirrors.linode.com/ubuntu disco InRelease
    ...
    Get:8 http://mirrors.linode.com/ubuntu disco-updates/universe amd64 Packages [38.6 kB]
    Fetched 472 kB in 0s (1,203 kB/s)
    Reading package lists... Done

Then install the certbot-auto...

    onformator@onformer:~$ wget https://dl.eff.org/certbot-auto
    ...
    HTTP request sent, awaiting response... 200 OK
    Length: 68023 (66K) [application/octet-stream]
    Saving to: ‘certbot-auto’

    certbot-auto                       100%[===============================================================>]  66.43K  --.-KB/s    in 0.002s

    2019-05-24 20:28:15 (38.2 MB/s) - ‘certbot-auto’ saved [68023/68023]

    onformator@onformer:~$ sudo mv certbot-auto /usr/local/bin/certbot-auto
    onformator@onformer:~$ sudo chown root /usr/local/bin/certbot-auto
    onformator@onformer:~$ sudo chmod 0755 /usr/local/bin/certbot-auto

### Get Started

Certbot has an Apache plugin, which is supported on many platforms, and automates certificate installation.

    sudo /usr/local/bin/certbot-auto --apache

Running this command will get a certificate for you and have Certbot edit your Apache configuration automatically to serve it. If you're feeling more conservative and would like to make the changes to your Apache configuration by hand, you can use the `certonly` subcommand:

    sudo /usr/local/bin/certbot-auto --apache certonly

To learn more about how to use Certbot read our [documentation](https://certbot.eff.org/docs/).

    onformator@onformer:~$ sudo /usr/local/bin/certbot-auto --apache
    Bootstrapping dependencies for Debian-based OSes... (you can skip this with --no-bootstrap)
    ...
    Deploying Certificate to VirtualHost /etc/apache2/sites-available/onform_pdf-le-ssl.conf
    Enabling available site: /etc/apache2/sites-available/onform_pdf-le-ssl.conf
    Error while running apache2ctl configtest.
    Action 'configtest' failed.
    The Apache error log may have more information.

    AH00526: Syntax error on line 42 of /etc/apache2/sites-enabled/onform_pdf.conf:
    Name duplicates previous WSGI daemon definition.

    Rolling back to previous server configuration...
    ...
    IMPORTANT NOTES:
    - We were unable to install your certificate, however, we
    successfully restored your server to its prior configuration.
    - Congratulations! Your certificate and chain have been saved at:
    /etc/letsencrypt/live/jeffco.pyramidprint.graphics/fullchain.pem
    ...

Here is lines 42 of that file:

    onformator@onformer:~$ sudo nano /etc/apache2/sites-enabled/onform_pdf.conf
    ===
    WSGIDaemonProcess onform_pdf python-path=/home/onformator/onform/onform_pdf python-home=/home/onformator/onform/venv

And here's the apache error log:

    onformator@onformer:~$ sudo nano /var/log/apache2/error.log
    ===
    [Fri May 24 20:55:23.939430 2019] [mpm_event:notice] [pid 6688:tid 140300695583680] AH00493: SIGUSR1 received.  Doing graceful restart
    AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 50.116.21.87. Set the 'ServerName' directive globally to suppress this message
    [Fri May 24 20:55:24.042950 2019] [mpm_event:notice] [pid 6688:tid 140300695583680] AH00489: Apache/2.4.38 (Ubuntu) mod_wsgi/4.6.5 Python/3.7 configured -- resuming normal operations
    [Fri May 24 20:55:24.042977 2019] [core:notice] [pid 6688:tid 140300695583680] AH00094: Command line: '/usr/sbin/apache2'

I'm going to check up on the ol hosts file...nvm...

Going off of [the answer in this StackOverflow post](https://stackoverflow.com/questions/47803081/certbot-apache-error-name-duplicates-previous-wsgi-daemon-definition?rq=1), I edited the onform_pdf.conf file as follows (Moved the Daemon Process outside of the VirtualHost definition):

    WSGIDaemonProcess onform_pdf python-path=/home/onformator/onform/onform_pdf python-home=/home/onformator/onform/venv
    WSGIProcessGroup onform_pdf

    <VirtualHost *:80>
            # The ServerName directive sets the request scheme, hostname and port that
            # the server uses to identify itself. This is used when creating
            # redirection URLs. In the context of virtual hosts, the ServerName
            # specifies what hostname must appear in the request's Host: header to
            # match this virtual host. For the default virtual host (this file) this
            # value is not decisive as it is used as a last resort host regardless.
            # However, you must set it for any further virtual host explicitly.

            ServerName jeffco.pyramidprint.graphics # new
            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html

            # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
            # error, crit, alert, emerg.
            # It is also possible to configure the loglevel for particular
            # modules, e.g.
            #LogLevel info ssl:warn

            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined

            # For most configuration files from conf-available/, which are
            # enabled or disabled at a global level, it is possible to
            # include a line for only one particular virtual host. For example the
            # following line enables the CGI configuration for this host only
            # after it has been globally disabled with "a2disconf".
            #Include conf-available/serve-cgi-bin.conf

            Alias /static/ /home/onformator/onform/onform_pdf/static_assets/
            <Directory /home/onformator/onform/onform_pdf/static_assets>
                    Require all granted
            </Directory>

            <Directory /home/onformator/onform/onform_pdf/onform_pdf>
                    <Files wsgi.py>
                            Require all granted
                    </Files>
            </Directory>

            WSGIScriptAlias / /home/onformator/onform/onform_pdf/onform_pdf/wsgi.py

    </VirtualHost>

I might have to still add the section for the other port...

    <VirtualHost *:443>
        ServerName example.com
        ...
    </VirtualHost>

Nope I didn't have to because it went through without error!

    (venv) onformator@onformer:~$ sudo /usr/local/bin/certbot-auto --apache
    Saving debug log to /var/log/letsencrypt/letsencrypt.log
    Plugins selected: Authenticator apache, Installer apache

    Which names would you like to activate HTTPS for?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: jeffco.pyramidprint.graphics
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate numbers separated by commas and/or spaces, or leave input
    blank to select all options shown (Enter 'c' to cancel): 1
    Cert not yet due for renewal

    You have an existing certificate that has exactly the same domains or certificate name you requested and isn't close to expiry.
    (ref: /etc/letsencrypt/renewal/jeffco.pyramidprint.graphics.conf)

    What would you like to do?
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: Attempt to reinstall this existing certificate
    2: Renew & replace the cert (limit ~5 per 7 days)
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 1
    Keeping the existing certificate
    Created an SSL vhost at /etc/apache2/sites-available/onform_pdf-le-ssl.conf
    Enabled Apache socache_shmcb module
    Enabled Apache ssl module
    Deploying Certificate to VirtualHost /etc/apache2/sites-available/onform_pdf-le-ssl.conf
    Enabling available site: /etc/apache2/sites-available/onform_pdf-le-ssl.conf

    Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: No redirect - Make no further changes to the webserver configuration.
    2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
    new sites, or if you're confident your site works on HTTPS. You can undo this
    change by editing your web server's configuration.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2
    Enabled Apache rewrite module
    Redirecting vhost in /etc/apache2/sites-enabled/onform_pdf.conf to ssl vhost in /etc/apache2/sites-available/onform_pdf-le-ssl.conf

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Congratulations! You have successfully enabled
    https://jeffco.pyramidprint.graphics

    You should test your configuration at:
    https://www.ssllabs.com/ssltest/analyze.html?d=jeffco.pyramidprint.graphics
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    IMPORTANT NOTES:
    - Congratulations! Your certificate and chain have been saved at:
    /etc/letsencrypt/live/jeffco.pyramidprint.graphics/fullchain.pem
    Your key file has been saved at:
    /etc/letsencrypt/live/jeffco.pyramidprint.graphics/privkey.pem
    Your cert will expire on 2019-**-**. To obtain a new or tweaked
    version of this certificate in the future, simply run certbot-auto
    again with the "certonly" option. To non-interactively renew *all*
    of your certificates, run "certbot-auto renew"
    - If you like Certbot, please consider supporting our work by:

    Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
    Donating to EFF:                    https://eff.org/donate-le

Now I believe that I need to tell Django that I do not want to use http anymore—all traffic should be redirected to https.

I also remembered that I still have DEBUG_MODE set to True. Switched it back to False in config_onform.json.

[The https section of the Django Docs](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#https) say to set two settings...

    Once you’ve set up HTTPS, enable the following settings.

        CSRF_COOKIE_SECURE¶

    Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.

        SESSION_COOKIE_SECURE¶

    Set this to True to avoid transmitting the session cookie over HTTP accidentally.

> onform_pdf/settings.py

    # ==== https ==== #
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

Ok time to give it a whirl to see how she spins!

Not loading still...I wonder if I should restart the apache service.

Before that, I tried inserting only the WSGIDaemonProcess's name (and the ProcessGroup) inside the new virtualhost...

    <IfModule mod_ssl.c>
    <VirtualHost *:443>
        ...
            ServerName jeffco.pyramidprint.graphics
            ServerAdmin webmaster@localhost
            DocumentRoot /var/www/html
        ...
            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static/ /home/onformator/onform/onform_pdf/static_assets/
        <Directory /home/onformator/onform/onform_pdf/static_assets>
                Require all granted
        </Directory>

        <Directory /home/onformator/onform/onform_pdf/onform_pdf>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIScriptAlias / /home/onformator/onform/onform_pdf/onform_pdf/wsgi.py
        WSGIDaemonProcess onform_pdf
        WSGIProcessGroup onform_pdf

    SSLCertificateFile /etc/letsencrypt/live/jeffco.pyramidprint.graphics/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/jeffco.pyramidprint.graphics/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf
    </VirtualHost>
    </IfModule>

Same thing...just not resolving to the page at all...

Now, I'm going to try a simple reload of apache and see what happens.

    (venv) onformator@onformer:~$ systemctl reload apache2
    Failed to reload apache2.service: The name org.freedesktop.PolicyKit1 was not provided by any .service files
    See system logs and 'systemctl status apache2.service' for details.
    (venv) onformator@onformer:~$ systemctl status apache2.service
    ● apache2.service - The Apache HTTP Server
    Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
        Active: active (running) since Fri 2019-05-24 19:05:53 UTC; 2h 53min ago
            Docs: https://httpd.apache.org/docs/2.4/
        Process: 6674 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SUCCESS)
    Main PID: 6688 (apache2)
            Tasks: 73 (limit: 1096)
        Memory: 33.5M
        CGroup: /system.slice/apache2.service
                ├─6688 /usr/sbin/apache2 -k start
                ├─9950 /usr/sbin/apache2 -k start
                ├─9951 /usr/sbin/apache2 -k start
                └─9952 /usr/sbin/apache2 -k start

That doesn't provide much info...except maybe that...yeah I don't even know, Maybe I'll check out the docs link provided if I get desparate.

    (venv) onformator@onformer:~$ sudo service apache2 restart
    Job for apache2.service failed because the control process exited with error code.
    See "systemctl status apache2.service" and "journalctl -xe" for details.

    (venv) onformator@onformer:~$ systemctl status apache2.service
    ● apache2.service - The Apache HTTP Server
    Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
        Active: failed (Result: exit-code) since Fri 2019-05-24 22:01:34 UTC; 1min 8s ago
            Docs: https://httpd.apache.org/docs/2.4/
    Process: 10182 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)

Yeah I probably should've taken a look at the docs when I first started using Apache. Oh well...[HERE THEY ARE!](https://httpd.apache.org/docs/2.4/)

I didn't think to install what it says is missing, as [this askubuntu post](https://askubuntu.com/questions/1113470/org-freedesktop-policykit1-was-not-provided-by-any-service-files?rq=1) says. It only has one vote so I'm not sure how trustworthy it is. 

    sudo apt install policykit-1

Might do a little more digging.

---- Ø ----

SideNote:

#### LVL1-OnForm : Set up [Django Logging](https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/#logging)  

---- Ø ----

DUH...

I didn't use sudo with the `systemctl` command...

    (venv) onformator@onformer:~$ sudo systemctl reload apache2
    apache2.service is not active, cannot reload.

    (venv) onformator@onformer:~$ sudo systemctl status apache2.service
    ● apache2.service - The Apache HTTP Server
    Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
    Active: failed (Result: exit-code) since Fri 2019-05-24 22:01:34 UTC; 14min ago
        Docs: https://httpd.apache.org/docs/2.4/
    Process: 10182 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)

    May 24 22:01:34 onformer systemd[1]: Starting The Apache HTTP Server...
    May 24 22:01:34 onformer apachectl[10182]: AH00526: Syntax error on line 1 of /etc/apache2/sites-enabled/onform_pdf.conf:
    May 24 22:01:34 onformer apachectl[10182]: Name duplicates previous WSGI daemon definition.
    May 24 22:01:34 onformer apachectl[10182]: Action 'start' failed.
    May 24 22:01:34 onformer apachectl[10182]: The Apache error log may have more information.
    May 24 22:01:34 onformer systemd[1]: apache2.service: Control process exited, code=exited, status=1/FAILURE
    May 24 22:01:34 onformer systemd[1]: apache2.service: Failed with result 'exit-code'.
    May 24 22:01:34 onformer systemd[1]: Failed to start The Apache HTTP Server.
    May 24 22:15:12 onformer systemd[1]: apache2.service: Unit cannot be reloaded because it is inactive.

Based on that log, changed the file back - removed the extra WSGDaemonProcess Line...

    (venv) onformator@onformer:~$ sudo nano /etc/apache2/sites-available/onform_pdf-le-ssl.conf

> /etc/apache2/sites-available/onform_pdf-le-ssl.conf

    WSGIScriptAlias / /home/onformator/onform/onform_pdf/onform_pdf/wsgi.py
    # removed
    WSGIProcessGroup onform_pdf

#### Allow HTTPS (and TCP?)

Realized that I had not [set up the firewall](https://www.linode.com/docs/security/securing-your-server/) ufw to accept https traffic...found [this article on Digital Ocean](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands).

    # Allow https through the firewall
    (venv) onformator@onformer:~$ sudo ufw allow https
    Rule added
    Rule added (v6)

    (venv) onformator@onformer:~$ sudo service apache2 restart

Yay! No errors...

Aaaaaand *no worries, **m8***!

Because it worked! Fuck ya. We have a secure connection, yo!

I'm starting to find that I like this digging around on the server. Quite enjoyable, particularly when I end up with results like this one.

Loads up securely on all devices I've tried thus far. Trying to submit an order via Firefox on my iPhone. But before I submit I want to open up the apache logs.

Submitted via my phone and the email + PDF attachment was in the inbox within 10 seconds. Crazy!

WordPress / Cornerstone is being difficult. I'm hoping I can go through CPanel to redirect traffic from `pyramidprint.graphics/jeffco` to `jeffco.pyramidprint.graphics`...

Fawk ya I'm on a roll right now...it's a smooth experience now. Going to /jeffco and being securely redirected.

Feelin good.

---

### 21:16 ~ Other Riziform Rivage

I was going to write down a reminder I'd set regarding building another version of OnForm that I can use in my portfolio. However, that will be part of tobias.fyi.

It would be pretty cool to integrate some of the things I've learned from the OnForm Build into AptDraft / Flask. Would give me more experience implementing that type of thing in different circumstances.

I'm not sure exactly what I would use it for yet, but I can probably find a cool use-case.

I mean it is an app about books / text. Maybe it can cobble together random pages from PDF versions of copyright-free books. Including some sort of random aspect would be pretty neat.

What would be even neater is to combine ReportLab + PyPDF + Processing.py + p5.js to create some crazy generative PDF graphics based off of words found in a given passage or page.

#### IDEA-AptDraft : Generate PDF art using text as an input (and output - generative word maps)  

---

### 22:42 ~ Organization Gyrostatics

Just spent the last while organizing my session journals. I haven't opened up any other can of code in a while, but I don't want to get caught up in those right now.

I spent enough time just now that I want to get down on some more learning!

But first, a word from my sponsors...

    Celestial Seasonings Tea is Tastea!
    ...
    Our vape juice is addicting.
        - Vapergate

---

### 23:14 ~ API - Acatamathesiastic Psychotaxis Ivresse

Began watching the next CS50 lecture and was pleasantly surprised that it is also part of Project 1. I thought that the flask and SQL lectures were the only ones I was supposed to watch before finishing the project. As it turns out, I do get to learn about OOP + ORMs + APIs while working on it.

---

### 23:46 ~ Checking the Castrametation

Castrametation: The art of designing a camp.
Castophrenia: The belief that one's thoughts are being stolen.

As I was going through the journal from today (after copying to fyi journal), I remembered that link that was given by the certbot to check the certificate status. I ran it and [it did really well](https://www.ssllabs.com/ssltest/analyze.html?d=jeffco.pyramidprint.graphics)!

We got an A overall.

Buenos A+, Amigos!
