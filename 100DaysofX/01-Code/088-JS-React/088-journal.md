# 2019-05-30 | #100DaysofCode

    GOAL-05-30 ~ Continue Learning React  

## Day 088/100 | 150/365

- [2019-05-30 | #100DaysofCode](#2019-05-30--100daysofcode)
  - [Day 088/100 | 150/365](#day-088100--150365)
    - [20:37 ~ Back to Bay6](#2037--back-to-bay6)
      - [20:40 ~ Props](#2040--props)
      - [20:47 ~ State of Denial](#2047--state-of-denial)
      - [22:26 ~ Visual Assets](#2226--visual-assets)
      - [22:45 ~ MoreStates](#2245--morestates)
      - [23:17 ~ Some Extras and Lifecycles](#2317--some-extras-and-lifecycles)
      - [CUE--088 ~ SVGO Library / vscode extension](#cue--088--svgo-library--vscode-extension)
      - [00:08 ~ Ref Not Thy Referee](#0008--ref-not-thy-referee)
      - [00:19 ~ More Inputs](#0019--more-inputs)
    - [00:57 ~ To The Build](#0057--to-the-build)
      - [01:19 ~ Default Props and Prop Types](#0119--default-props-and-prop-types)
      - [01:43 ~ PropTypes Golden Rülz](#0143--proptypes-golden-rülz)
    - [01:45 ~ Await Data Fetch](#0145--await-data-fetch)
      - [02:22 ~ Async and Await](#0222--async-and-await)
    - [03:17 ~ Nighty Night of Ni](#0317--nighty-night-of-ni)

---- Notes ----

    CUE--088 ~ SVGO Library / vscode extension  

---- Resources ----

- [GoodReads API](https://www.goodreads.com/api/index)
- ['Using the GoogleBooks API' docs](https://developers.google.com/books/docs/v1/using)

---- Sojourn ----

### 20:37 ~ Back to Bay6

#### 20:40 ~ Props

I already passed in `name` as a prop, though I don't think I realized that's what it was. However, it is more common to bring the prop out of the return (inside the component)...

```javascript
class Welcome extends React.Component {
    render() {
        const { name } = this.props;
        return (
            <h1>Welcome to the Vibrary, {name}</h1>
        )
    }
}
```

#### 20:47 ~ State of Denial

I'm going to leave in both types of components for now and see if I can make them work by me onesie. Well... I guess that didn't last long. I had to switch to using a class because of the state functionality.

```javascript
class App extends React.Component {

    state = {
    toggle: true
    }

    render() {
    return (
        <div className="App">
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <Welcome name="Mr. Reaper" />
        </header>
        <p>This should show and hide.</p>
        <button>Show / Hide</button>
        </div>
    );
    }
}
```

#### 22:26 ~ Visual Assets

Decided to swap out the react logo for one of my own design. Came up with something pretty neat. This also means that I am able to learn more about SVG.

Here's the working color pallette:

    #595854
    #F2A74B
    #BFBCBA
    #731D1D
    #0D0D0D

To start, the book mentions a tool called SVGO - a node package that optimizes SVGs.

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:31:56
    ╰─ npm install svgo
    npm WARN @typescript-eslint/eslint-plugin@1.6.0 requires a peer of typescript@* but none is installed. You must install peer dependencies yourself.
    ...
    npm WARN tsutils@3.12.0 requires a peer of typescript@>=2.8.0 || >= 3.2.0-dev || >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= 3.6.0-dev but none is installed. You must install peer dependencies yourself.

    + svgo@1.2.2
    updated 1 package and audited 889057 packages in 14.623s
    found 0 vulnerabilities

Looked it up and decided to install the typescript that the errors mention:

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:35:17
    ╰─ npm i -D typescript@~3.2.0-dev
    + typescript@3.2.4
    added 1 package from 1 contributor and audited 889058 packages in 15.768s
    found 0 vulnerabilities

For some reason it's not recognizing the command...

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:36:59
    ╰─ svgo vibrary-logo-04.svg vib-logo.min.svg
    zsh: command not found: svgo

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:37:02
    ╰─ npm install svgo
    + svgo@1.2.2
    updated 1 package and audited 889058 packages in 14.155s
    found 0 vulnerabilities

Tried installing it again. And again, globally.

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:37:58
    ╰─ npm install -g svgo
    /Users/Tobias/.nvm/versions/node/v12.3.1/bin/svgo -> /Users/Tobias/.nvm/versions/node/v12.3.1/lib/node_modules/svgo/bin/svgo
    + svgo@1.2.2
    added 49 packages from 83 contributors in 2.437s

Now it worked!

    ╭─ vibrary » tobiasfyi » ..rary/vibrary/src »  ma 19.05.30 ∫ 22:39:08
    ╰─ svgo vibrary-logo-04.svg

    vibrary-logo-04.svg:
    Done in 50 ms!
    4.482 KiB - 2.4% = 4.375 KiB

Hawt damn that looks fresh!

![vibrotationary](vibrotationary.gif)

Sweet.

#### 22:45 ~ MoreStates

Looked in the dev console to see that the state change triggers the re-render of the component.

#### 23:17 ~ Some Extras and Lifecycles

I installed the svgo extension for vscode. Nice to have!

#### CUE--088 ~ SVGO Library / vscode extension  

When the component is created: the constructor is called first, then the `componentWillMount()` method. The `render()` is the "mounting". Then after rendering is finished, `componentDidMount()`. Scott doesn't use the WillMount - and react docs say not to? - because of double something-or-other.

There are a bunch of other lifecycle methods for different phases of the component mounting and updating.

#### 00:08 ~ Ref Not Thy Referee

Managed to find a few more of the A Book Apart books.

Added an input and accessed the value of the input with a method similar to the state function.

```javascript
class App extends React.Component {

    submit = () => {
    console.log(this.text.value)
    }
    ...
        </header>
        <input type="text" ref={(input) => this.text = input} />
        <button onClick={this.submit}>Show Value</button>
        </div>
    );
    }
}
```

That logs the value of the input the console...obviously. The refs can really be assigned to any DOM element in order to assign it to a component.

#### 00:19 ~ More Inputs

Inputs: controlled vs uncontrolled.

```javascript
updateInput = () => {

}
```

The above syntax allows access to the `this` object.

```javascript
updateInput = (event) => {
    console.log(event.target.value);
        this.setState({
        input: event.target.value
    })
}
```

This fires off an event every time a character is entered, and because the setState sets the state to the new value, it adds onto the characters entered before. This gives *full* control over the input.

```jsx
<h3>{this.state.input}</h3>
<input type="text" onChange={this.updateInput} value={this.state.input} /> // controlled input
<input type="text" ref={(input) => this.text = input} /> // uncontrolled input
```

With the `<h3>` tag pulling in the input, it updates automatically with the text entered into the controlled input field.

---

### 00:57 ~ To The Build

Getting to the build part. Edited the css a little to make the header nice and minimal. Left the animation in coz it's neat. Time to iterate over some dataz...

```jsx
{books.map(book => (
    <div key={book.id}>
        {book.title}
    </div>
))}
```

Creating a new component for the books, this time in a separate file. Those damn tabs were pissing me off, so I looked up how to set the tab size per filetype...

```json
"[javascript]": {
    "editor.tabSize": 2
},
"[python]": {
    "editor.tabSize": 4
},
```

Ok back to the build! Iterating over the book titles using the component in `Book.js`.

```jsx
{books.map(book => <Book key={book.id} book={book} />)}
```

#### 01:19 ~ Default Props and Prop Types

Installing prop-types...

    ╭─ vibrary » tobiasfyi » ../vibrary/vibrary »  master ● ?                              19.05.30 ∫ 01:23:26
    ╰─ npm install prop-types
    + prop-types@15.7.2
    updated 1 package and audited 889063 packages in 30.432s
    found 0 vulnerabilities

...and imported into book component...

    import PropTypes from 'prop-types';

Now set up the prop types into which the component expects to be passed...just to make it easier if something isn't the correct type.

```javascript
import React from 'react';
import PropTypes from 'prop-types';

export default class Book extends React.Component {
static propTypes = {
    book: PropTypes.shape({
        title: PropTypes.string.isRequired
        desc: PropTypes.string.isRequired
    })
}
```

No desc was passed in, so...

    Warning: Failed prop type: The prop `book.desc` is marked as required in `Book`, but its value is `undefined`.
        in Book (at App.js:30)
        in App (at src/index.js:7)

Default props will be a sort of placeholder or "default"...doi...

```jsx
export default class Book extends React.Component {
    static propTypes = {
        book: PropTypes.shape({
            title: PropTypes.string.isRequired,
        }),
        desc: PropTypes.string
    }

    static defaultProps = {
        desc: 'Description not available'
    }

    render() {
        return (
        <div>
            <h3>{this.props.book.title}</h3>
            <p>{this.props.desc}</p>
        </div>
        );
    }
}
```

Now the page says description not available for each item because it's empty. Added in a description.

```jsx
{books.map(book => <Book key={book.id} book={book} desc={book.desc} />)}
```

#### 01:43 ~ PropTypes Golden Rülz

1. Have a proptype for every single prop used in component
2. Have either isRequired or defaultProp
   1. Helps a ton with debugging coz it raises something whenever something isn't as it should be

---

### 01:45 ~ Await Data Fetch

Await Data has a nice assonance to it.

Alrighty then, time to go grab my API key from [GoodReads](https://www.goodreads.com/api/index). This will be the last video of the night. Hopefully I can get something to work before then.

    Here is your developer key for using the Goodreads API. This key must be appended to every request using the form variable 'key'. (If you're using our write API, you'll need your secret too.)

    key: *******

Hmm...I'm not seeing the ability to grab an image. I looked around to see what other APIs might be able to do that. Found this tutorial on using Google Books API to grab the cover images, so if anything I can use that. Given that I only need to access the public database, I can use a simple API Key.

I created a new project on Google Console and obtained an API key...

    apiKey=*******

#### 02:22 ~ Async and Await

Added a `componentDidMount()` method to the App class in `App.js`. Simply by inserting "async" beforehand it will be run asynchronously. Also, it's good practice to have the fetch wrapper into a try / catch block (aw yeah, just spent some time on these bad boiz so I'm gold pony boii).

Here's the URL for Consider Phlebas:

    https://books.google.com/books?id=3_bJKlAOecEC&printsec=frontcover&dq=consider+phlebas&hl=en&sa=X&ved=0ahUKEwjR7-6o7MLiAhUHXa0KHTxeCisQ6AEIKjAA#v=onepage&q=consider%20phlebas&f=false

So the id is: `id=3_bJKlAOecEC`

Some more from the ['Using the API' docs](https://developers.google.com/books/docs/v1/using):

    Retrieving a specific volume - You can retrieve information for a specific volume by sending an HTTP GET request to the Volume resource URI:

            https://www.googleapis.com/books/v1/volumes/volumeId

    Replace the volumeId path parameter with the ID of the volume to retrieve. See the Google Books IDs section for more information on volume IDs.

    Request - Here is an example of a GET request that gets a single volume:

    GET https://www.googleapis.com/books/v1/volumes/zyTCAlFPjgYC?key=yourAPIKey

So for this book in particular...

    apiKey='n0ty0Ur4P!K3y'

    GET https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC?key=apiKey
    GET https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC?key=n0ty0uR4P!K3y

About to call it for the night, but I realized that I need to get a list of books. Starting with the example provided in the docs.

    GET https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=yourAPIKey

I found this:

    https://www.googleapis.com/books/v1/volumes?q=mainCategory:fiction&key=n0ty0uR4P!K3y'

Saving this one for later...

    const res = await fetch('https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC?key=n0ty0uR4P!K3y');

Ayyyyye using the one that filters by mainCategory:fiction I actually got a response!

Going to make another, cooler request...

    const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=inauthor=banks&prettyPrint=true&key=n0ty0uR4P!K3y')

Meh...I'll play around some more later.

```javascript
{…}
    items: (10) […]
        0: Object { kind: "books#volume", id: "wmy71stp17cC", etag: "k916buF03r0", … }
        1: Object { kind: "books#volume", id: "bDKIGmdnxsMC", etag: "uE45cg1x2pU", … }
        2: Object { kind: "books#volume", id: "ECvxEpH7VZYC", etag: "tPgqpflarz8", … }
        3: Object { kind: "books#volume", id: "Uog7rgEACAAJ", etag: "DiELdn3gDBU", … }
```

---

### 03:17 ~ Nighty Night of Ni

Here's a useful [Google Books API Overview Link](https://console.developers.google.com/apis/api/books.googleapis.com/overview?project=vibrary).

I'm actually going to leave it off there as it's already 03:17 and I'm definitely not at my sharpest right now.

At least I successfully got a response though! That's exciting.

Hasta responsivas, amigas!
