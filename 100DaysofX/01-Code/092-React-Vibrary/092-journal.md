# 2019-06-03 | #100DaysofCode

    GOAL-06-03 ~ Learn more React + build more stuff + vibe with the Vibrarians  

## Day 092/100 | 154/365

- [2019-06-03 | #100DaysofCode](#2019-06-03--100daysofcode)
  - [Day 092/100 | 154/365](#day-092100--154365)
    - [12:12 -+- session.init](#1212----sessioninit)
    - [12:56 ~ Visual Identification](#1256--visual-identification)
    - [13:35 ~ New Componentizations](#1335--new-componentizations)
    - [13:47 ~ Links and Lability](#1347--links-and-lability)
    - [14:15 ~ Book Dactylogram](#1415--book-dactylogram)
    - [15:24 ~ Troubleshootin' Toby](#1524--troubleshootin-toby)
    - [16:40 ~ Actually, Though](#1640--actually-though)

---- Resources ----

- [JS async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [React Type Error StackOverflow Discussion](https://stackoverflow.com/questions/50862192/react-typeerror-cannot-read-property-props-of-undefined)

---- Selects ----

- [PythonBytes Ep 132](https://pythonbytes.fm/episodes/show/132/algorithms-as-objects)
  - [Algorithms as Objects](https://gieseanw.wordpress.com/2019/05/10/algorithms-as-objects/)
  - [The Missing Intro to Containerization](https://medium.com/faun/the-missing-introduction-to-containerization-de1fbb73efc5)
- [Khan Academy course on Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms)

---- Sojourn ----

### 12:12 -+- session.init

Firefox Developer Edition is still not doing too hot. I did a little more research and found that other people have had issue with Firefox and 4k displays. I guess I'll be using Chrome for a while longer.

---

### 12:56 ~ Visual Identification

Spent a little time re-exporting the logo plus a favicon to use for the app. Now I'm getting back into some tutorial bidnizz. I went back and forth a bit between using the yellow/gold or the red as the main brand color. I decided on the red because it shows up better on both light and dark backgrounds, whereas the gold doesn't show up as well on light backgrounds.

![SVG Markdown Test](vibrary-logo.png)

Crazy...the png version of vibrary-logo is 88k while the svg version is only 4.5k. That's so tiny!

---

### 13:35 ~ New Componentizations

Moved the entire App component to a new file. Spent a little time trying to figure out the destructuring warning I was getting from eslint, but ended up just ignoring it.

The ordering of the Routes is important. Though this is not a good solution, it is a solution to the fact that if path="/" is above, it sees that yes, that slash exists, and stops. It doesn't care whether there is a test after that or not. Moving the home route below test is a workaround solution...

```jsx
<Switch>
  <Route path="/test" component={Test} />
  <Route path="/" component={BookList} />
</Switch>
```

The far better solution to this is to specify that the path must be exactly what is defined.

```jsx
<Route exact path="/" component={BookList} />
```

Inserting the `exact` statement as it is above is equivalent to `exact = { true }`

---

### 13:47 ~ Links and Lability

```javascript
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Link,
} from 'react-router-dom';
```

Imported the Link functionality to accomplish the following:

```jsx
<Link to="/">
  <img src={logo} className="App-logo" alt="logo" />
</Link>
```

Then set a similar thing up in `Book.js` so that each book cover links to the test page. I'm assuming we'll be converting the test component into a detail page type of thing here soon. However, the next thing is to route the cover art link dynamically to the id of that movie.

```jsx
<Link to={`/${book.id}`}>
```

To capture that id from the App component, the route can take in an id path, with the Test component capturing it via the match...

```jsx
<Route path="/:id" component={Test} />
...
const Test = ({ match }) => (
  <h1>{match.params.id}</h1>
);
```

Now, the Test component outputs the id of the book to the h1 tag as specified. All we have to do now to get the book details is link up the id to be inserted into the url that gets the information about a specific book from the API. Here's an example of a fetch call + URL for a specific book (I knew I'd need this at a later time—that's why I saved it):

```javascript
const res = await fetch('https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC?key=d0nT3vEnTRy!t');
```

Which, when edited to work with the code, looks like...

```javascript
class BookDetail extends React.Component {
  state = {
    book: {},
  }

  async componentDidMount() {
    try {
      const res = await fetch(`https://www.googleapis.com/books/v1/volumes/${this.props.match.params.id}?key=d0nT3vEnTRy!t`);
      const book = await res.json();
      this.setState({
        book,
      });
    } catch (e) {
      console.log(e);
    }
  }
...
```

Just had the idea to also have a list that is returned via a query for `mainCetegory:science+fiction`.

```javascript
const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=mainCategory:science+fiction&prettyPrint=true&key=d0nT3vEnTRy!t');
```

I'll give that a whirl later on.

---

### 14:15 ~ Book Dactylogram

Dactylogram: fingerprint.

I haven't saved it yet, but here's the code I have for displaying the book details (the render method underneath the async + more code above)...

```jsx
render() {
  return (
    <div>
      <h1>{this.state.book.volumeInfo.title}</h1>
      <h5>{this.state.book.volumeInfo.publishedDate}</h5>
      <h3>{this.state.book.volumeInfo.authors[0]}</h3>
      <p>{this.state.book.volumeInfo.description}</p>
    </div>
  );
}
```

The moment of trooooooth!...nope got an error.

    TypeError: Cannot read property 'title' of undefined

It's saying that it can't access the book title. I could brute force it / workaround this error by simply reusing the code from the BookList app. I believe that the data returned by the API for the detail and for the list is exactly the same. However, I want to learn how to debug this bad boii so I'm going to get the detail to work how the tutorial sets it up...

Quick note: it might be cool to use sorting on the BookList query.

Anyways...according to the react devtools, I have the state and everything set up correctly...

    Props
      history: {…}
      location: {…}
      match: {…}
        isExact: true
        params: {…}
          id: "3_bJKlAOecEC"
        path: "/:id"
        url: "/3_bJKlAOecEC"

Looking at this, I can once again see that everything seems to be hooked up correctly...

```javascript
${this.props.match.params.id} // this correctly traverses the props to find the id
```

And also using the react devtools I can see that the way I accessed the title should be correct...

```jsx
<h1>{this.state.book.volumeInfo.title}</h1>
```

However, when I use that method of accessing the state, it throws the error I copied in above...not sure why...I'm going to look over the code in the folder I downloaded to see if there is anything I missed.

Ahaaaa! I think I found the problem...

```javascript
render() {
  const { movie } = this.state;
```

I never assigned it...but wait, this code is *after* this video—because he got it to work in the video without that extra bit in the render method...hmmm...I'm going to try it out anyways.

Before I do that...I'm going to try one more thing—logging the object to the console to see if there's anything wrong with what's being returned...I guess that really only accomplished the exact same thing as looking in the React devtools.

It all looks correct. I don't get what the issue is. I'm going to try only accessing one of the other items, such as the detail or author...nope, but I didn't think to go to the console to get more info about the error. So I made some progress at least.

So everything is connected up correctly...up until the render function. Something about the way the state is being assigned or accessed or...I'm not sure...

The reason I say that is I logged the exact same thing to the console in the async section of the component and it printed out fine.

```javascript
class BookDetail extends React.Component {
  ...
  async componentDidMount() {
    ...
    console.log(this.state.book.volumeInfo.title);
    ...
====
// from Chrome DevTools
// BookDetail.js:15 Consider Phlebas
```

I tried running it without the title, and even the damn error message said that the object had a key of `title`...***wut.***

    Invariant Violation: Objects are not valid as a React child (found: object with keys {title, authors, publisher, publishedDate, description, industryIdentifiers, readingModes, pageCount, printedPageCount, printType, categories, averageRating, ratingsCount, maturityRating, allowAnonLogging, contentVersion, panelizationSummary, imageLinks, language, previewLink, infoLink, canonicalVolumeLink}). If you meant to render a collection of children, use an array instead.

However, for some reason, the error message on the browser page says that the error is in the this.setState method...

      11 |   const book = await res.json();
    > 12 |   this.setState({
      13 | ^   book,
      14 |   });
      15 |

Ok I think I got some useful info. I logged the book object to the console inside of the render function and it came up with an empty array. However, I'd set the book state to be an empty array, just to see what it did. Setting that back now...

And the same thing happened, except with an object. Therefore, I know now that the state is not being set correctly. I have a few more ideas to try and work this thing out.

---

### 15:24 ~ Troubleshootin' Toby

I broke up the fetch and all that into multiple steps in order to be sure everything was connected. I then accessed the URL via direct link and downloaded that data as json. I saved it into `vibrary/assets/code`. Here's a snippet of it.

```json
{
  "kind": "books#volume",
  "id": "3_bJKlAOecEC",
  "etag": "FOiqpNwhG4M",
  "selfLink": "https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC",
  "volumeInfo": {
    "title": "Consider Phlebas",
    "authors": [
      "Iain M. Banks"
    ],
    "publisher": "Orbit",
    "publishedDate": "2009-12-01",
    "description": "\u003cb\u003eThe first book in Iain M. Banks's seminal science fiction series",
    "pageCount": 544,
    "printedPageCount": 437,
    "printType": "BOOK",
    "categories": [
      "Fiction / Science Fiction / Action & Adventure",
      "Fiction / Science Fiction / Space Opera",
      "Fiction / Science Fiction / Hard Science Fiction"
    ],
    "averageRating": 3.5,
    "ratingsCount": 103,
    ...
    },
    "imageLinks": {
      "smallThumbnail": ...
      ...
      "extraLarge": "http://books.google.com/books/content?id=3_bJKlAOecEC&printsec=frontcover&img=1&zoom=6&edge=curl&imgtk=AFLRE70Q2KD2_dRgXQd0cdi3hayZtLyH0nSqLrKCNXrBuKb6McKyemN9o9Zuhj9vNUTKEnoTwiCdSn57w6qWjjHFmObyvSAn8uC-D2z2ASWo8_K_hMbgjZ0WHpVSfXX59itbAFSnhmjm&source=gbs_api"
    },
    ...
  },
  ...
}
```

I wonder if I can access it by adding quotes or if it the "props" are converted to props (without the quotes) automatically...yep, it looks like that part is fine. Here's the eslint response to me trying to access it via brackets...

```javascript
console.log(this.state["volumeInfo"])
//["volumeInfo"] is better written in dot notation.eslint(dot-notation)
```

Next thing I tried is logging the book variable that is being assigned to the state, before it's assigned...

```javascript
const book = await res.json();
console.log(book);
```

It printed out the object correctly.

Ok...I'm about to set this aside for a while to go hang with friends and let thi marinate. I have one more thread of inquiry I want to pursue—the fact that when I console log the exact same object from outside the `return()` method, it works. But when I put it inside the return method, it causes the fatak error.

```javascript
console.log(this.state.book);
// {kind: "books#volume", id: "3_bJKlAOecEC", etag: "cfm/ikxWAy0", selfLink: "https://www.googleapis.com/books/v1/volumes/3_bJKlAOecEC", volumeInfo: {…}, …}
```

Ahaaaaa! Now we're getting somewhere...when I console log the title, it errors out.

```javascript
console.log(this.state.book.volumeInfo.title);
// BookDetail.js:25 | Uncaught TypeError: Cannot read property 'title' of undefined
```

So now the question becomes: what happens when I log the volumeInfo - without the title?...it works!

```javascript
console.log(this.state.book.volumeInfo);
//{title: "Consider Phlebas", authors: Array(1), publisher: "Orbit", publishedDate: "2009-12-01", description: "<b>The first book in Iain M. Banks's seminal scien…ly to find it, and with it their own destruction.", …}
```

Now I know there's something very strange with this level of the object. Not sure why it's not letting me access any of the children...but I'm here to find this the fukk out!

Hmm...that's really weird—the devtool console is also logging "undefined"...

    BookDetail.js:25 | undefined

This makes me wonder if it's a timing thing...i.e. it's trying to access the data before it's fetched. It seems like the `render()` method is being called first, then the async function, then the back to the render method.

That doesn't seem like it makes any sense, though maybe it does. I wonder if I could make it work with promises.

Ok I decided to add the linting rule back in to ignore the destructuring issue:

```json
"rules": {
    ...
    "react/destructuring-assignment": 0
}
```

Oh well...I tried reading up on the [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) and looking on [StackOverflow](https://stackoverflow.com/questions/50862192/react-typeerror-cannot-read-property-props-of-undefined), but I still can't figure it out. I guess I'll have to come back to it later.

Ok I'm seeing now that it's something to do with `this`. Depending on when / where it's called, it will change?

Ok that's it...I'm done for now...

---

### 16:40 ~ Actually, Though

I am actually done now...3+ hours later...

Gosh durnit. I'll see you when I return!

This trouble better be ready to be shot when I do...

Buenos troubleshootin', Amigos!
