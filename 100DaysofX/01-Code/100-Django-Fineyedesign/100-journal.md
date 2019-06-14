# 2019-06-11 | #100DaysofCode

    GOAL-06-11 ~ Fineyedesign, Phase I, v0.1  

## THE LAST DAY OF THE CHALLENGE

## Day 100/100 | 162/365

- [2019-06-11 | #100DaysofCode](#2019-06-11--100daysofcode)
  - [THE LAST DAY OF THE CHALLENGE](#the-last-day-of-the-challenge)
  - [Day 100/100 | 162/365](#day-100100--162365)
    - [11:32 ~ CRUD](#1132--crud)
      - [Let's Work them Abbs](#lets-work-them-abbs)
    - [11:49 ~ Recept React](#1149--recept-react)
      - [14:14 ~ Initial Testing Illutation](#1414--initial-testing-illutation)
      - [14:50 ~ Inferiae DB Seeding](#1450--inferiae-db-seeding)
    - [14:58 ~ React and Django Together, Irroborated](#1458--react-and-django-together-irroborated)
    - [15:23 ~ Create React App](#1523--create-react-app)
      - [LVL1-FYI ~ Find new colors for: lt + yl + dk](#lvl1-fyi--find-new-colors-for-lt--yl--dk)
      - [TASK-163 ~ Fix Stradder program](#task-163--fix-stradder-program)
      - [15:57 ~ Isotropic Installations](#1557--isotropic-installations)
      - [16:04 ~ Mass Reaction Isophote](#1604--mass-reaction-isophote)
      - [16:29 ~ Enchorial Endeict Endpoint Access](#1629--enchorial-endeict-endpoint-access)
      - [17:04 ~ Game of Abbrevas: CORS](#1704--game-of-abbrevas-cors)
      - [ACC-162 ~ Popped my React + Django cherry](#acc-162--popped-my-react--django-cherry)
    - [17:27 ~ Catogenic Action / React(ion) Cathexis](#1727--catogenic-action--reaction-cathexis)
      - [CUE--FYI ~ Ask Philip about Static Site Generator vs ...?](#cue--fyi--ask-philip-about-static-site-generator-vs-)
    - [21:35 ~ Level 2 React Latration](#2135--level-2-react-latration)
      - [21:37 ~ Basic Toggle Locellate](#2137--basic-toggle-locellate)
      - [CUE--FYI ~ Look at what other nice shortcuts are in React n frenz extension](#cue--fyi--look-at-what-other-nice-shortcuts-are-in-react-n-frenz-extension)
    - [21:55 ~ Understanding RenderProps Unzymotic](#2155--understanding-renderprops-unzymotic)
      - [LVL1-FYI ~ Pick out 3 awesome fonts for Fineyedesign](#lvl1-fyi--pick-out-3-awesome-fonts-for-fineyedesign)
      - [22:50 ~ Fragment Fortuitism](#2250--fragment-fortuitism)
      - [23:06 ~ Penannular Portal](#2306--penannular-portal)
    - [23:36 ~ Swappitty Floppitty Floop](#2336--swappitty-floppitty-floop)
    - [00:42 ~ Swoopity Floppity Noopity Doop](#0042--swoopity-floppity-noopity-doop)
      - [Back 2 Bay6...1ce Again](#back-2-bay61ce-again)
    - [00:44 ~ No REST For the Weary](#0044--no-rest-for-the-weary)
    - [01:06 ~ Customized Aquarelle](#0106--customized-aquarelle)
      - [KB+-+FYI ~ HTTP 304 Response = Client has a cache of the asset](#kb-fyi--http-304-response--client-has-a-cache-of-the-asset)
      - [02:00 ~ Template Arpenteur](#0200--template-arpenteur)
      - [LVL2-FYI ~ Image resizer](#lvl2-fyi--image-resizer)
      - [LVL1-FYI ~ Use unsplash images for color themes](#lvl1-fyi--use-unsplash-images-for-color-themes)
    - [02:22 ~ Malabuano](#0222--malabuano)

---- Tasks ----

    TASK-162 ~ Hook up React with DRF to make first site prototype  

    LVL1-FYI ~ Use unsplash images for color themes  
    LVL1-FYI ~ Find new colors for: lt + yl + dk  
    LVL1-FYI ~ Pick out 3 awesome fonts for Fineyedesign  
    LVL2-FYI ~ Image resizer  
    LVL3-FYI ~ Bash List for ALLOWED_HOSTS EnviroVar  

---- Notes ----

    ACC-162 ~ Popped my React + Django cherry  

    CUE--FYI ~ Ask Philip about Static Site Generator vs ...?  
    CUE--FYI ~ Look at what other nice shortcuts are in React n frenz extension  

    KB+-+FYI ~ HTTP 304 Response = Client has a cache of the asset  
    IDEA-161 ~ Keyboard Shortcut of the Day  

---- Resources ----

- React
  - [Learning React Roadmap from Scratch to Advanced](https://www.freecodecamp.org/news/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6/)
- [coverage.py](https://coverage.readthedocs.io/en/v4.5.x/)
- With Django
  - [Also, here's that Dockerizing Django with Postgres, Gunicorn, and Nginx article once again.](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
  - [wsvincent tutorial on React and Django](https://wsvincent.com/django-rest-framework-react-tutorial/)
  - [Django REST with React](https://www.valentinog.com/blog/drf/)
  - [Val düsseldorf has a Webpack tutorial](https://www.valentinog.com/blog/webpack/)
  - [Django Docs article on writing reusable apps](https://docs.djangoproject.com/en/2.2/intro/reusable-apps/)

---- Selects ----

- [Matthew Butterick - Practical Typography](https://practicaltypography.com/)
- [Netlify](https://www.netlify.com/)

---- Sojourn ----

### 11:32 ~ CRUD

#### Let's Work them Abbs

Callipygous: having a beautiful buttocks.
Revirescent: growing young or strong again.
Uranophobic: fear of heaven.
Doublette: copy of own artwork made by an artist.

Crapulent: physically ill from overeating or overdrinking.
Reptation: act of squirming along a smooth-walled narrow passage.
Uvid: moist; wet.
Dentiologist: one who speaks with closed teeth.

---- ∫ ----

Implementing CRUD functionality into the current setup is as easy as changing the generic class that the DetailView instantiates.

```python
class RepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rep.objects.all()
    serializer_class = RepSerializer
```

Viola! Vuala! Koala!Now I can CRUD all over the place using this API...

And with that, the wsvinvent tutorial is done. Time to move onto the [REST + React article from ValentinoG](https://www.valentinog.com/blog/drf/).

---

### 11:49 ~ Recept React

Recept: idea or image formed by repeated similar perceptions.

[Django Docs article on writing reusable apps](https://docs.djangoproject.com/en/2.2/intro/reusable-apps/)

#### 14:14 ~ Initial Testing Illutation

- Illutation: mud bath.
- Illocution: an act which is performed by speaking words.
- Illiquation: the melting of one thing into another.
- Illision: the act of striking against something.

---- ∫ ----

Mr. Valentino says that there's no point in testing vanilla Django models or Django ORM. According to him, a good starting point for testing in Django is...

- Do not test Django built-in code (models, views, etc)
- Do not test Python built-in functions

Those are already tested! Instead, he suggests installing [coverage](https://coverage.readthedocs.io/en/v4.5.x/)

    Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

    Coverage measurement is typically used to gauge the effectiveness of tests. It can show which parts of your code are being exercised by tests, and which are not.

So...I installed coverage for the first time, evurr.

    ╭─ Fineyedesign » tobiasfyi » ..cts/fineyedesign »  master ● ?     19.06.11 ∫ 14:23:53
    ╰─ pip install coverage
    Collecting coverage
      Using cached https://files.pythonhosted.org/packages/a8/39/5334b42cc81a40d50901eca26f4fac4480b44ac318db55d2b621d0aaca09/coverage-4.5.3-cp37-cp37m-macosx_10_13_x86_64.whl
    Installing collected packages: coverage
    Successfully installed coverage-4.5.3

Valentino Guy recommends that I run the following every time I add new code...

    $ coverage run --source='.' manage.py test

    $ coverage html
    # to generate the report

I ran those commands and received a report saying I have 75% coverage. Obviously none of that is from me.

---- ∫ ----

Changed up the `ListAPIView` into ...

```python
class RepList(generics.ListCreateAPIView):
    queryset = Rep.objects.all()
    serializer_class = RepSerializer
```

---

#### 14:50 ~ Inferiae DB Seeding

Inferiae: offerings to the spirits of the dead.

Ah I remember seeing something about fixtures—they are a way to insert data into the database. This would be useful, so I might as well do it just to see how.

...I learn best by *doing* things. That's something I wish I could remember at all times, even when I'm lazy.

    ╭─ Fineyedesign » tobiasfyi » ..yedesign/sojourn »  master ● ?     19.06.11 ∫ 14:55:10
    ╰─ mkdir fixtures

    ╭─ Fineyedesign » tobiasfyi » ..cts/fineyedesign »  master ● ?     19.06.11 ∫ 14:55:21
    ╰─ touch sojourn/fixtures/reps.json

> sojourn/fixtures/reps.json

For now I'm just going to copy/paste the json that was serialized from the data I created last night. Not actually going to run it, as the data is already there.

```json
...
{
    "id": 1,
    "title": "A Nu Start",
    "author": 1,
    "body": "A nu start...a nu starts for everybody!\r\n\r\nI hope everyone tries a nu start at some point in their lifetime. It's an experience.\r\n\r\nIt's a whole mood.\r\n\r\nBest regards,\r\nTobias",
    "motif": "Retrophilia",
    "lit_dev": "Hyperbaton",
    "created": "2019-06-10T23:58:05.305293-06:00",
    "updated": "2019-06-10T23:58:05.387645-06:00"
},
...
```

To insert the data into the database, use `python manage.py loaddata sojourn`.

---

### 14:58 ~ React and Django Together, Irroborated

Irroborate: to strengthen.

There are many ways to set up a Django project with React. ValeGino sees the following patterns:

1. React in its own "frontend" Django app
   1. Load a single HTML template
   2. Let React manage the frontend
   3. Difficulty = Medium
2. Standalones
   1. Django REST as a standalone API
   2. React as a standalone SPA
   3. Difficulty = Hard
      1. It involves VWT for authentication
   4. Use this method if...
      1. More advanced things are needed
3. Mix and Match
   1. mini React apps inside Django templates
   2. Difficulty = simple
   3. Use this method if...
      1. The site doesn't need much javascript
      2. SEO Matters

ValenGino advises for people like me—just tarting out with DRF / React—avoid option 2. This tutorial will go through Option 1. This [Val düsseldorf has a tutorial on Webpack](https://www.valentinog.com/blog/webpack/) as well. He uses webpack and whatnot in the React + Django tutorial.

Good ol' William has a [tutorial on React and Django](https://wsvincent.com/django-rest-framework-react-tutorial/) as well. I'm going to pick this project up with that tutorial, then maybe go back to the VG one if I'd feeling groovy about it.

---

### 15:23 ~ Create React App

I already have the npm package installed globally.

    ╭─ Fineyedesign » tobiasfyi » ..cts/fineyedesign »  master ● ?             19.06.11 ∫ 15:26:48
    ╰─ create-react-app frontend
    Creating a new React app in ~/workshop/Fineyedesign/08-Projects/fineyedesign/frontend.
    ...
    Installing react, react-dom, and react-scripts...
    ...
    Success! Created frontend at ~/workshop/Fineyedesign/08-Projects/fineyedesign/frontend
    Inside that directory, you can run several commands:
      npm start
        Starts the development server.
      npm run build
        Bundles the app into static files for production.
      npm test
        Starts the test runner.
      npm run eject
        Removes this tool and copies build dependencies, configuration files
        and scripts into the app directory. If you do this, you can’t go back!

    We suggest that you begin by typing:
      cd frontend
      npm start

    Happy hacking!

Aw, thanks Facebook! You seem so human, Zuckmanburger. What's your secret?

#### LVL1-FYI ~ Find new colors for: lt + yl + dk  

My stradder program is getting hung up on setting a custom width for the column. Going to take care of that really quick...but not really quick as in 'right now'. I mean I'll take care of it quickly when I do get to it...

#### TASK-163 ~ Fix Stradder program  

#### 15:57 ~ Isotropic Installations

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 15:55:48
    ╰─ npm install react-router-dom
    npm WARN @typescript-eslint/eslint-plugin@1.6.0 requires a peer of typescript@* but none is installed. You must install peer dependencies yourself.
    ...
    npm WARN tsutils@3.14.0 requires a peer of typescript@>=2.8.0 || >= 3.2.0-dev || >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= 3.6.0-dev but none is installed. You must install peer dependencies yourself.

    + react-router-dom@5.0.1
    added 12 packages from 6 contributors and audited 889038 packages in 15.763s
    found 0 vulnerabilities

I remember this happening when I worked on Vibrary. Going to look through those notes to see what I installed. Pretty sure it was just the TypeScript package though. In ther spirit of experimentation, I'm just going to send the thing...

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 15:56:19
    ╰─ npm install typescript
    + typescript@3.5.1
    added 1 package from 1 contributor and audited 889039 packages in 17.351s
    found 0 vulnerabilities

---- ∫ ----

#### 16:04 ~ Mass Reaction Isophote

Isophote: line connecting points of equal light intensity from a given source.

Time to finish this tutorial so I can start learning more dope Reactness from Scotty my Boii.

Copied over a few of the records from `replist-1.json` to `App.js` to use as mock data while building. Converting the function App component into a ClassBasedComponent...

```jsx
// From this...
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome to the Finest of Designs
        </p>
      </header>
    </div>
  );
}
```

```jsx
// To This!
class App extends Component {
  state = { repList };

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div>
          {this.state.repList.map(rep => (
            <div>
              <h1>{rep.title}</h1>
              <p>{rep.body} </p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}
```

And that successfully iterated through the list above. I also got the header and logo all situated for the time being.

#### 16:29 ~ Enchorial Endeict Endpoint Access

Enchorial: belonging or used in a country; domestic.
Endeictic: glowing and warmly enthusiastic praise.

I get to hook into the DRF API now! Stoked...

The code is very similar to the code I wrote for Vibrary, as that was just another API that I was accessing. Noice.

Forgot about the eslint config.

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 16:38:26
    ╰─ npm install eslint
    + eslint@5.16.0
    updated 1 package and audited 889223 packages in 16.348s
    found 0 vulnerabilities

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 16:37:46
    ╰─ touch .eslintrc.js

But actually, I only want to install it as a dev dependency. I found my old notes from the React Level 1 course...

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 16:41:49
    ╰─ npm install --save-dev eslint eslint-config-airbnb eslint-plugin-react
    + eslint@5.16.0
    + eslint-config-airbnb@17.1.0
    + eslint-plugin-react@7.13.0
    added 7 packages from 7 contributors, updated 2 packages and audited 889345 packages in 13.133s
    found 0 vulnerabilities

And it needs to be init'd...

    ╭─ Fineyedesign » tobiasfyi » ..edesign/frontend »  master ● ?     19.06.11 ∫ 16:42:39
    ╰─ eslint --init
    ? How would you like to configure ESLint? Use a popular style guide
    ? Which style guide do you want to follow? Airbnb (https://github.com/airbnb/javascript)

    ? Do you use React? Yes
    ? What format do you want your config file to be in? JavaScript
    Checking peerDependencies of eslint-config-airbnb@latest
    ...
    + eslint-plugin-react@7.13.0
    + eslint@5.16.0
    + eslint-plugin-import@2.17.3
    + eslint-config-airbnb@17.1.0
    + eslint-plugin-jsx-a11y@6.2.1
    added 16 packages from 6 contributors, updated 5 packages and audited 889470 packages in 14.778s
    found 0 vulnerabilities

    Successfully created .eslintrc.js file in /Users/Tobias/workshop/Fineyedesign/08-Projects/fineyedesign/frontend

Ah and that creates the .eslintrc file. Nice to be reminded of all of these steps.

Here's the App component...

```jsx
class App extends Component {
  state = {
    reps: [],
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      console.log(res);
      const reps = await res.json();
      console.log(reps);
      this.setState({
        reps,
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
        <div>
          {this.state.reps.map(rep => (
            <div>
              <h1>{rep.title}</h1>
              <p>
                {rep.body}
              </p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}
```

#### 17:04 ~ Game of Abbrevas: CORS

Cacaesthesia: morbid sensation.
Orchesis: act of dancing or rhythmical moving of the body.
Ramus: branch of anything.
Satisdation: provision of security.

Catena: series, chain, or sequence.
Ordalian: of, like, or pertaining to an ordeal.
Rhumb: compass point.
Scagliola: stone-like plasterwork for interior decoration.

---- ∫ ----

When I tried running it, none of the items showed up. I looked around and found an error in the console that let me know what was happening...

    Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://127.0.0.1:8000/api/. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing).

I forgot to set up the CORS on Django to accept requests from the React App. I'm going to go the route that Mr Vin2Cents does. Time to install some middleware...

    ╭─ Fineyedesign » tobiasfyi » ..cts/fineyedesign »  master ● ?          19.06.11 ∫ 17:03:37
    ╰─ pip install django-cors-headers
    ...
    Successfully installed django-cors-headers-3.0.2

Then I updated my settings to allow these darn Catena Ordalians. It took me a few tries until the server ran without falling down...

> fineyedesign/settings.py

```python
# ======== URLs ======== #
# First attempt = Fail
CORS_ORIGIN_WHITELIST = ("localhost:3000",)
# (corsheaders.E013) Origin 'localhost:3000/' in CORS_ORIGIN_WHITELIST is missing scheme or netloc
# HINT: Add a scheme (e.g. https://) or netloc (e.g. example.com).

# Interim attempt = Fail!
CORS_ORIGIN_WHITELIST = ("localhost:3000/",)
# (corsheaders.E014) Origin 'http://localhost:3000/' in CORS_ORIGIN_WHITELIST should not have path

# Final attempt = Succyess!
CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)
```

Reloaded the React App and...

    [11/Jun/2019 17:25:58] "GET /api/ HTTP/1.1" 200 3115

BoooooOoOOOoooom! Got it to connect up and everythaaaaang...

#### ACC-162 ~ Popped my React + Django cherry  

Before I move on, gotta set that unique id on the state.

    Warning: Each child in a list should have a unique "key" prop.

    Check the render method of `App`. See https://fb.me/react-warning-keys for more information.
        in div (at App.js:32)
        in App (at src/index.js:7)

I fixed it by adding a key to the div that holds the rep items...

```jsx
<div>
  {this.state.reps.map(rep => (
    <div key={rep.id}>
      <h1>{rep.title}</h1>
      <p>
        {rep.body}
      </p>
    </div>
  ))}
</div>
```

Now time for some Level 2 (Action /) React(ion)

---

### 17:27 ~ Catogenic Action / React(ion) Cathexis

Catogenic: formed from above.
Cathexis: investment of emotional energy into a thought or idea.

[This tutorial](https://hackernoon.com/creating-websites-using-react-and-django-rest-framework-b14c066087c7) goes over some authentication stuff, which I will probably need to learn.

Found Matthew Butterick's book [Practical Typography](https://practicaltypography.com/) while reading through Mr Vincwind's post about the design of his website.

I also started thinking about the technology that I want to use to publish the Fineyedesign site when the first prorotype is complete. I'm not sure if a static site generator would be good or not because I'll be changing things somewhat regularly. I'll do some more research.

#### CUE--FYI ~ Ask Philip about Static Site Generator vs ...?  

---

### 21:35 ~ Level 2 React Latration

Latration: the act of yelping or barking.

#### 21:37 ~ Basic Toggle Locellate

Locellate: divided into small compartments.

Installed a React & Friends snippets extension. `rcc` creates a new component.

#### CUE--FYI ~ Look at what other nice shortcuts are in React n frenz extension  

Created a basic toggle component, which is how we started the previous series as well. Just reviewing. Started typing in `rcc` to get the component structure...

```jsx
import React, { Component } from 'react';

export default class Toggle extends Component {
  state = {
    on: false,
  }

  toggle = () => {
    this.setState({
      on: !this.state.on,
    });
  }

  render() {
    return (
      <div>
        {this.state.on && <h1>Toggle Me</h1>}
        <button onClick={this.toggle}>Show/Hide</button>
      </div>
    );
  }
}
```

We are going to be learning RenderProps.

---

### 21:55 ~ Understanding RenderProps Unzymotic

Unzymotic: fabulous.

Finally decided to stop looking through my journals for the link to the Learning React Roadmap and search it on Google. Found it within 30 seconds.

[Learning React Roadmap from Scratch to Advanced](https://www.freecodecamp.org/news/learning-react-roadmap-from-scratch-to-advanced-bff7735531b6/)

[Also, here's that Dockerizing Django with Postgres, Gunicorn, and Nginx article once again.](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)

---- ∫ ----

He's going pretty fast and I'm not exactly understanding all of it. However, I'm glad I remembered this: I need to pick out a few unique fonts that I can include in the brand styleguide along with a few more colors.

#### LVL1-FYI ~ Pick out 3 awesome fonts for Fineyedesign  

```jsx
// ToggleRenderProps.js
render() {
  const { render } = this.props;
  return (
    <div>
      {render({
        on: this.state.on,
        toggle: this.toggle,
      })}
    </div>
  );

// App.js
<Toggle render={({ on, toggle }) => (
  <div>
    {on && <h1>She Me The Money</h1>}
    <button onClick={toggle}>Show / Hide</button>
  </div>
)} />
```

Basically, writing the Toggle like it's written above in the first block makes it reusable as shown below—without needing to anything else to the actual Toggle component. That is rather nice.

Also, it's called a RenderProp because the "render" is being passed in as a prop. However, it doesn't have to be named render.

```jsx
<Toggle render={({ on, toggle }) => (
  <div>
    {on && <nav>Menu Item</nav>}
    <button onClick={toggle}>Menu</button>
  </div>
)} />
```

Next up - Children-based Render Props. Swapped out render for children.

```jsx
// ToggleRPC.js
render() {
  const { children } = this.props;
  return children({
    on: this.state.on,
    toggle: this.toggle,
  });
}

// App.js
<Toggle>
  {({ on, toggle }) => (
    <div>
      {on && <h3>She Me The Money</h3>}
      <button onClick={toggle}>Show / Hide</button>
    </div>
  )}
</Toggle>
```

---

#### 22:50 ~ Fragment Fortuitism

Fortuitism: believe in evolution by chance variation.

Fragments are basically generic components to solve the extraneous div situation.

```jsx
import React, { Component, Fragment } from 'react';
...
<Toggle>
  {({ on, toggle }) => (
    <Fragment>
      {on && <h3>She Me The Money</h3>}
      <button onClick={toggle}>Show / Hide</button>
    </Fragment>
  )}
</Toggle>
```

With newer versions of Babel, etc., the Fragments can be written like this:

```jsx
<Toggle>
  {({ on, toggle }) => (
    <>
      {on && <h3>She Me The Money</h3>}
      <button onClick={toggle}>Show / Hide</button>
    </>
  )}
</Toggle>
```

#### 23:06 ~ Penannular Portal

Penannular: in the form of an almost complete ring.

Ok I need to force myself to understand these concepts, as Scott goes over them very quickly and not too deeply. It's nice he doesn't spend too much time on them but I need to take time to understand.

So the "div" problem I mentioned is due to the fact that JSX has some rules about where it can be written into a file. Separating JSX from other JSX and from regular javascript code via a div works but adds on a bunch of extra divs that take up space.

Fragments were created to deal with that problem. They basically act like a generic component, which can be brought into the App like...well, like a component. This way, basically anything can be held inside of such a Fragment and arbitrarily passed around as if it were inside a component.

I'm not sure if they are related at all, but it seems to me like Portals take that even one step further. From what I've gathered thus far, which is nothing except the first few sentences of the Portal video, Portals allow a tunnel to be created through which something like a Fragment can be passed, resulting in arbitrary code being able to be run basically wherever. Let's learn some more!

Oh ya, I forgot that the example Scott is using to demonstrate a portal is a Modal. By inserting some code into the root of the application - possible by using a Portal - we can be sure that it will appear on top of everything else.

---- ∫ ----

Created a new component / file: `Portal.js`.

---

### 23:36 ~ Swappitty Floppitty Floop

Well...I'm not sure where I got the idea that we'd be building a blog application in Level 2 React, as we most definitely are not doing so. Maybe it was the GraphQL video or something.

Now that I know that, I'm looking around for another direction to take. Styled components would be a good one. Also, Modern CSS Layouts.

Or maybe the Pro Gatsby 2 would be dope coz I could learn more about a static site generator and if I want to use one.

---

### 00:42 ~ Swoopity Floppity Noopity Doop

#### Back 2 Bay6...1ce Again

Alright I have a plan now that the React one fell through...

I'm going back to the basics—keeping it pure Django. I'm going to use the HTML5UP templates as a base for the design of the pages, but I'm not going to use any front end framework to make it an SPA just yet.

Let's get going!

---

### 00:44 ~ No REST For the Weary

No more REST API for this GUY. At least not yet...I guess I got a little ahead of myself.

However, I'm going to make a copy of the setup I have now in case I want to take peeks at it later on. Crazy... the `frontend` directory is 253mb...constitutes probably 75% of the project's size. I'm only going to copy the django directories.

Copied over the `sojourn` and `fineyedesign` directories into `./docs/archive/` and appended `-api` to the end of their names.

---- ∫ ----

Changes be made...to the URLConfs:

> fineyedesign/urls.py

```python
urlpatterns = [path("admin/", admin.site.urls), path("", include("sojourn.urls"))]
```

> sojourn/urls.py

```python
urlpatterns = [
    path("", RepListView.as_view(), name="rep-list"),
    path("<int:pk>/", RepDetailView.as_view(), name="rep-detail"),
]
```

---- ∫ ----

Changes be made...to the views:

> sojourn/views.py

```python
from django.views.generic import ListView, DetailView
from .models import Rep

class RepListView(ListView):
    model = Rep
    template_name = "home.html"

class RepDetailView(DetailView):
    model = Rep
    template_name = "sojourn.html"
```

Started up the ol' server and...she runs! Let's see if actually works. It errored out the first time, but ended up being a simple issue of the name of the urlpattern. I changed the ListView URL back to `name="home"` and she's purring along just fine! Crazy how easy it is to switch back and forth. I guess once the site is more complex it takes a bit more than that...but for me, now, that was cake! Or ice cream. I like ice cream more.

---

### 01:06 ~ Customized Aquarelle

Aquarelle: watercolour painting.

The most important part to have up and running right now is the DetailView. As there will only be one article up tomorrow, I could literally have only that.

Currently porting over the template to create the new `base.html` and `home.html`. Having some issues with the static loading but it's getting there.

Oh man...I think it was just an extra space inside the href, like `href="... %} "`. Fixed it and about to see if that was really it...I guess not.

I was getting a 304 error, which I realized is different from a 404...so [I looked it up](https://httpstatuses.com/304). Apparently it happens when the client supposedly has a "valid representation" of the asset, and the server basically tells the client to use that cached version instead of sending an entirely new one. Interesting.

#### KB+-+FYI ~ HTTP 304 Response = Client has a cache of the asset  

And now it works! Aw yeaauuhhhh and it looks really good.

#### 02:00 ~ Template Arpenteur

Arpenteur: land surveyor.

I see now that receiving the 304 error is fine in this instance, because the assets worked correctly when they were cached.

    ...
    [12/Jun/2019 02:00:18] "GET /static/webfonts/fa-brands-400.woff2 HTTP/1.1" 304 0
    [12/Jun/2019 02:00:18] "GET /static/assets/favicon-lt.png HTTP/1.1" 200 5707

I successfully added a loop that brings in the Rep title and body. Not how it will be laid out in its final form but it's cool.

```html
<ul class="features">
  {% for rep in object_list %}
  <li>
    <span class="icon major style5 fa-gem"></span>
    <h3>{{ rep.title }}</h3>
    <p>{{ rep.body }}</p>
  </li>
  {% endfor %}
</ul>
```

This is more like how it will be on the home page—a section for each Rep with nav items for each. Super rad, and so simple!

I definitely got caught up in making this more complex than it needed to be. But here I am and I need to get some sleep tonight.  

```html
<div id="main">
  {% for rep in object_list %}
  <section id="{{ rep.title }}" class="main">
    <div class="spotlight">
      <div class="content">
        <header class="major">
          <h2>{{ rep.title }}</h2>
        </header>
        <p>{{ rep.body }}</p>
        <ul class="actions">
          <li><a href="#" class="button">{{ rep.motif }}</a></li>
        </ul>
      </div>
      <span class="image"><img src="{% static '/assets/images/measure.jpg' %}" alt="Measure Twice" /></span>
    </div>
  </section>
  {% endfor %}
</div>
{% endblock body %}
```

#### LVL2-FYI ~ Image resizer  

#### LVL1-FYI ~ Use unsplash images for color themes  

---

### 02:22 ~ Malabuano

Downloaded a bunch of dope pictures to use directly, as inspiration, or as the basis for new colors / styles.

I'm glad I decided to go this route, even though if I had started this last night I could be basically done by now (probably). It feels good to make this kind of progress.

Buenos nacheesimos, amigos!
