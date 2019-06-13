# 2019-04-28 | Onform

## Day 056 / 100

- [2019-04-28 | Onform](#2019-04-28--onform)
  - [Day 056 / 100](#day-056--100)
  - [---- SELECT * FROM Project ----](#-----select--from-project-----)
    - [Project.abstract](#projectabstract)
    - [Project.loxocache(2019-04)](#projectloxocache2019-04)
    - [Global.loxicache(2019-04)](#globalloxicache2019-04)
  - [---- SELECT * FROM Session(2019-04-28) ----](#-----select--from-session2019-04-28-----)
    - [Session.abstract](#sessionabstract)
    - [Session.cache](#sessioncache)
  - [Session.sojourn](#sessionsojourn)
    - [02:31 ~ Deploy Fully](#0231--deploy-fully)
      - [Allow HTTP/TCP](#allow-httptcp)
      - [Gettin' Live](#gettin-live)
    - [03:41 ~ More Errors](#0341--more-errors)

## ---- SELECT * FROM Project ----

### Project.abstract

    GOAL_Onform : A simple form-based application for PDF generation  

### Project.loxocache(2019-04)

    LVL0_051 : Copy sojourn into Challanges + redact sensitive info  

    GOAL_051 : Deploy to production server  

    TASK√051 : Install git on the onform server  
    TASK√050 : Connect server to GitHub remote repo  
    LVL1_051 : Go through the Django Deployment Checklist  
        TASK√051 : Set up env vars on server  
        TASK√051 : No more SECRETs shall PASS  
        TASK√051 : Commit the newly private django + push to github  
        TASK√051 : Fetch the newly private django repo  
        TASK√051 : Set up env vars on local machine  
        LVL1_054 : Set production Postgres to only accept connections from application  
    LVL1_051 : Install + Configure Web Server  
    LVL1_051 : Configure subdomain  
    LVL1_050 : Add success message to orderdetail  
    TASK√054 : Format billing_phone/fax like normal phone  
    LVL1_050 : Create user account for jeffco  

    LVL2_050 : Implement email feature with SendGrid  
        LVL2_054 : Set email environment variables in production  

    TASK√051 : Footer should be stuck to bottom of page (login page)  
    TASK√051 : Add our phone number to footer  
    LVL2_050 : Serialize model data + display PDF  
    LVL2_050 : Fix labels on OrderFormView  

    LVL3_044 : Ask if billing address is the same, if so, fill in automatically  
    LVL3_050 : Randomish numbering scheme for orders  
    LVL3_050 : Fix formatting of OrderDetail info @top - unless displaying PDF  

    IDEA_050 : render_pdf.js - loop through field_data for drawText  

### Global.loxicache(2019-04)

    CUE_043 : Set up script to automatically post parts of this coding journal to blog app  
    CUE_043 : Save the output PDF into a django/postgres table  
    CUE_047 : Start learning Django REST Framework  
    CUE_047 : Read up on REST = Representational State Transfer  

    IDEA_01 : Write CLI tool that sets up the basic Django template with a couple of commands  

--------ø--------

## ---- SELECT * FROM Session(2019-04-28) ----

### Session.abstract

    GOAL_056 : Set up the OnForm application on a subdomain  
    GOAL_056 : Set up email functionality  

### Session.cache

---

## Session.sojourn

--------ø--------

### 02:31 ~ Deploy Fully

#### Allow HTTP/TCP

    # Remove port 8000
    (venv) onformator@onformer:~$ sudo ufw delete allow 8000
    Rule deleted
    Rule deleted (v6)

    # Allow http through the firewall
    (venv) onformator@onformer:~$ sudo ufw allow http/tcp
    Rule added
    Rule added (v6)

    (venv) onformator@onformer:~$ sudo service apache2 restart

#### Gettin' Live

If everything was set up correctly, the site should be running at the server's IP address.

Well...something isn't set up correctly because I got a 500 Internal Server Error. Found the apache error logs...

> /var/log/apache2/error.log

[mpm_event:notice] AH00489: Apache/2.4.38 (Ubuntu) mod_wsgi/4.6.5 Python/3.7 configured -- resuming normal operations
[core:notice] AH00094: Command line: '/usr/sbin/apache2'
Failed to exec Python script file '/home/onformator/onform/onform_pdf/onform_pdf/wsgi.py'.
Exception occurred processing WSGI script '/home/onformator/onform/onform_pdf/onform_pdf/wsgi.py'.
...
ModuleNotFoundError: No module named 'onform_pdf.settings'

Maybe I made a typo in the apache config.

> /etc/apache2/sites-available

    (venv) onformator@onformer:~$ sudo a2ensite onform_pdf
    Enabling site onform_pdf.
    To activate the new configuration, you need to run:
        systemctl reload apache2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onform_pdf.settings')

---

### 03:41 ~ More Errors

Now I seem to be getting a different error:

    File "/home/onformator/onform/onform_pdf/onform_pdf/settings.py", line 17, in <module>
        onfile = json.load(config_onfile)
    File "/usr/lib/python3.7/json/__init__.py", line 296, in load
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
    File "/usr/lib/python3.7/json/__init__.py", line 348, in loads
        return _default_decoder.decode(s)
    File "/usr/lib/python3.7/json/decoder.py", line 337, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    File "/usr/lib/python3.7/json/decoder.py", line 353, in raw_decode
        obj, end = self.scan_once(s, idx)
        on.decoder.JSONDecodeError: Expecting ',' delimiter: line 10 column 5 (char 352)

Ahhh there are slashes in the secret key?

Nope...BUT HOLY SHIT I GOT IT TO LOAD!!

Unfortunately it's not loading very well for some reason. It seems that none of the static files are loading?

It was a FUCKING MISSING COMMA. Oh maaaaannnn. Now I'd like to remember what I else I did to get the new JSON error...So I'll copy the relevent files over.

> config_onform.conf

    Alias /static/ /home/onformator/onform/onform_pdf/static_assets
    <Directory /home/onformator/onform/onform_pdf/static_assets>
            Require all granted
    </Directory>

    <Directory /home/onformator/onform/onform_pdf/onform_pdf>
            <Files wsgi.py>
                    Require all granted
            </Files>
    </Directory>

    WSGIScriptAlias / /home/onformator/onform/onform_pdf/onform_pdf/wsgi.py
    WSGIDaemonProcess onform_pdf python-path=/home/onformator/onform/onform_pdf python-home=/home/onformator/onform/venv
    WSGIProcessGroup onform_pdf

I remember know...I think it was the python-path. Before it was pointing to the onform dir not onform/onform_pdf.

I'm going to try changing the static directory to see if I can get those to load. After scoping the logs.

sbin/apache2'
01630: client denied by server configuration: /home/onformator/onform/onform_pdf/static_assetscss, referer: http://**.**.**.****/accounts/login/?next=/

It looks like the path is missing a slash. Yep. The django docs examples have a trailing slash. YESSSSS!

For some reason the footer isn't aligned. Ah probably because I didn't run the `collectstatic` command.