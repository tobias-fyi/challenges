# 2019-06-04 | #100DaysofCode

    GOAL-06-04 ~ Learn more React + build more stuff + vibe with the Vibrarians  

## Day 093/100 | 155/365

- [2019-06-04 | #100DaysofCode](#2019-06-04--100daysofcode)
  - [Day 093/100 | 155/365](#day-093100--155365)
    - [09:43 -+- Fineyedesign.init](#0943----fineyedesigninit)
    - [09:51 ~ Demisang Debugging](#0951--demisang-debugging)
    - [10:15 ~ Heretofore Happenstance](#1015--heretofore-happenstance)
      - [CUE-153 : Write up solution to `cannot read property __ of undefined` error](#cue-153--write-up-solution-to-cannot-read-property-__-of-undefined-error)
    - [10:44 ~ Heuristic Gereticlitous](#1044--heuristic-gereticlitous)
    - [11:06 ~ Such Styled Components](#1106--such-styled-components)
      - [IDEA-153 : Phrontistery API with React](#idea-153--phrontistery-api-with-react)
      - [LVL2-vibrary : Fix description paragraph formatting](#lvl2-vibrary--fix-description-paragraph-formatting)
    - [12:11 ~ Point Breakers](#1211--point-breakers)
    - [14:41 ~ Holocryptic Honesty](#1441--holocryptic-honesty)

---- Tasks ----

    LVL2-vibrary : Fix description paragraph formatting  

---- Notes ----

    CUE--155 : Write up solution to `cannot read property __ of undefined` error  
    IDEA-155 : Phrontistery API with React  
    IDEA-155 : Jeopard Tresure Hunt (livestream event series)  

---- Resources ----

- [used object-fit](https://alligator.io/css/cropping-images-object-fit/)
- [browse around the popular plugins and such](https://reactjs.org/community/component-workbenches.html)
- [Taking it to *overdrive*](https://github.com/berzniz/react-overdrive), baby.

---- Selects ----

- Google Books API
  - [Docs for Volume.get](https://developers.google.com/books/docs/v1/reference/volumes/get)
- Wes Bos' [CSS Grid Course](https://cssgrid.io/)

---- Sojourn ----

### 09:43 -+- Fineyedesign.init

Back in the studio without any sleep but tons of inspiration and wonderment...I guess? Yes to wonderment but maybe could've picked a better word for it.

Anyways...

I had the thought a few minutes ago to try and fix the bug I was seeing by using the same API that I used for the BookList component. I will hopefully be able to use the match parameters to capture the ID and use that as an index to the List API call instead of utilizing a separate URL.

Not sure if it will work or if it's good practice (probably not—the latter at least) but I don't want to use any more time on aimless troubleshooting...oh yeuuuhhh. I need to bring out the scope and make due with the targets I have open to me.

I'm on it right now.

---

### 09:51 ~ Demisang Debugging

Well...I didn't get far before I realized that there would not be any way for the app to guarantee that the book ID that was clicked on is i........

More research and reading...

    Undefined’ is the property of the global object. If you don’t assign any value to a variable is of type ‘undefined’. A code also return the undefined value when the evaluated variable doesn’t have any assigned value.

---

### 10:15 ~ Heretofore Happenstance

Holy shit it worked! ... not anything I mentioned above, though it was something that I had thought about while writing the above line on inquiry. Basically, it came down to the assignment of `this.state` in the `componentDidMount()` method.

```javascript
this.setState({
  book,
});
```

Rather than simply passing in `book` to the `this.setState` method, I passed in `book.volumeInfo`, which is where the meat of the information is anyways.

```javascript
this.setState({
  book: book.volumeInfo,
});
```

That's the code that did it... literally two words that I spent hours and hours trying to figure out.

But hey at least it worked now and didn't take me another 3 hours to figure out.

Now the title is passed into the component correctly and displays on the page and everything!

And with only a few changes, I successfully accessed all the volume information that I'd previously commented out in order to not break the app.

Sweet!

The description is not rendering all correctly-formatted and everything, but that's not as important right now. I'm simply happy that I got all the pieces to work.

I'm making a git commit now, just for posterity (and security). I'm also thinking that I should write a blog post about this because I feel that it might trip some people up in the future just as it did to me.

#### CUE-153 : Write up solution to `cannot read property __ of undefined` error  

---

### 10:44 ~ Heuristic Gereticlitous

I was able to render the cover of the book using the same method that I used to fix the last issue. I was running into the same error and thought I might as well try it out. Long story short it worked. I simply added on another line to my setState method for the cover...

```jsx
this.setState({
  book: book.volumeInfo,
  cover: book.volumeInfo.imageLinks.small,
  backdrop: book.volumeInfo.imageLinks.medium,
});
// ==== then render the cover via this.state
render() {
  const { book } = this.state;
  return (
    <div>
      <img src={this.state.cover} alt={book.title} />
      <h1>{book.title}</h1>
      <h5>{book.publishedDate}</h5>
      <h3>{book.authors}</h3>
      <p>{book.description}</p>
    </div>
  );
}
```

Then I managed to figure out at least a workaround for the multiple state items dealio within the render and before the `return()`.

```jsx
render() {
  const { book } = this.state;
  const { cover } = this.state;
  const { backdrop } = this.state; // simplify ^^ into one variable?
  return (
    <div>
      <img src={backdrop} alt={book.title} />
      <img src={cover} alt={book.title} />
      ...
    ...
  ...
...
```

---

### 11:06 ~ Such Styled Components

I want to practice with React beyond what is in the tutorial and to strike out a bit on my own before starting the next series. I'm thinking about trying to throw together something that creates an API for Phrontistery.

#### IDEA-153 : Phrontistery API with React  

#### LVL2-vibrary : Fix description paragraph formatting  

---- ∫ ----

Time to install some styled component goodies! Have heard Scott talk about these on Syntax.fm a bunch so I'm very excite to get into them.

    ╭─ vibrary » tobiasfyi » ../vibrary/vibrary »  master ●                             19.06.02 ∫ 11:15:39
    ╰─ npm install styled-components
    > styled-components@4.2.1 postinstall /Users/Tobias/workshop/vibrary/vibrary/node_modules/styled-components
    > node ./scripts/postinstall.js || exit 0
    + styled-components@4.2.1
    added 12 packages from 10 contributors and audited 889596 packages in 16.652s
    found 0 vulnerabilities

This tutorial will only be going over the very basics of CSS Grid. However, Wes Bos has [a neat free course on the topic](https://cssgrid.io/) available for free, thanks to Firefox! I just signed up for it, so now I can add it to my list of things I may never get to! Woop woop!

This styled component will only be used in the BookList component - so might as well include it in that file.

Super simple. Basically it's just another mini-component that holds straight up css...

```jsx
...
  render() {
    return (
      <BookGrid>
        {this.state.books.map(book => <Book key={book.id} book={book} />)}
      </BookGrid>
    );
  }
}
...
const BookGrid = styled.div`
  display: grid;
  padding: 1rem;
  grid-template-columns: repeat(6, 1fr);
  grid-row-gap: 1rem;
`;
```

Then another styled component for `Book.js`...with some extra CSS that I added in to crop all the covers to the same size (while keeping their aspect ratio - [used object-fit](https://alligator.io/css/cropping-images-object-fit/))...

```jsx
const Book = ({ book }) => (
  <Link to={`/${book.id}`}>
    <Cover src={book.volumeInfo.imageLinks.thumbnail} alt={book.volumeInfo.title} />
  </Link>
);
...
const Cover = styled.img`
  width: 8rem;
  height 12rem;
  object-fit: cover;
  box-shadow: 0 0 35px #0D0D0D;
`;
```

Then I moved the body styling from `App.ccs`to `index.css`.

```javascript
export const Cover = styled.img`
  width: 8rem;
  height 12rem;
  object-fit: cover;
  box-shadow: 0 0 35px #0D0D0D;
`;
```

Instead of exporting the Cover styled component (like above / Scott did in the tutorial), I'm just going to create a new one for BookDetail. My reasoning goes that I have the crop set for the grid but do not want the same crops for the Detail page.

Set up another styled component `BookWrapper` to style the backdrop. That styled component wraps / replaces the div and takes in the image data / URL as a prop. To access the prop in the CSS, gotta use an arrow function, yo!

> vibrary/src/BookDetail.js

```javascript
const Cover = styled.img`
  box-shadow: 0 0 35px #0D0D0D;
`;

const BookWrapper = styled.div`
  position: relative;
  padding-top: 50vh;
  background: url(${props => props.backdrop}) no-repeat;
  background-size: cover;
`;
```

The backdrop doesn't look spectacular—it's rendering all kinds of pixelized—but it works as expected.

---

### 12:11 ~ Point Breakers

Taking a break now to eat and vape.

---

### 14:41 ~ Holocryptic Honesty

Getting into some extra packages for animatinos and such. Definitely want to [browse around the popular](https://reactjs.org/community/component-workbenches.html) plugins / packages for React to see what other goodies I can scrounge up...

    ╭─ vibrary » tobiasfyi » ../vibrary/vibrary »  master ●                             19.06.02 ∫ 14:51:12
    ╰─ npm install react-overdrive
    + react-overdrive@0.0.10
    added 1 package from 1 contributor and audited 889597 packages in 15.291s
    found 0 vulnerabilities

[Taking it to *overdrive*](https://github.com/berzniz/react-overdrive), baby.

```jsx
import Overdrive from 'react-overdrive';
...
<Overdrive id={book.id}>
  <Cover src={book.volumeInfo.imageLinks.thumbnail} alt={book.volumeInfo.title} />
</Overdrive>
```

The animations were't working for me. Saw a warning in the js saying that no declarative file was found for react-overdrive. Tried installing again with the `--save` flag.

    Could not find a declaration file for module 'react-overdrive'. '/Users/Tobias/workshop/vibrary/vibrary/node_modules/react-overdrive/lib/Overdrive.min.js' implicitly has an 'any' type.
      Try `npm install @types/react-overdrive` if it exists or add a new declaration (.d.ts) file containing `declare module 'react-overdrive';`ts(7016)

    ╭─ vibrary » tobiasfyi » ../vibrary/vibrary »  master ●                             19.06.02 ∫ 15:04:27
    ╰─ npm install @types/react-overdrive
    npm ERR! code E404
    npm ERR! 404 Not Found - GET https://registry.npmjs.org/@types%2freact-overdrive - Not found
    npm ERR! 404  '@types/react-overdrive@latest' is not in the npm registry.
    npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
    npm ERR! 404 Note that you can also install from a
    npm ERR! 404 tarball, folder, http url, or git url.
    npm ERR! A complete log of this run can be found in:
    npm ERR!     /Users/Tobias/.npm/_logs/2019-06-02T21_07_42_213Z-debug.log

...hmm...I guess I'll do some searching around to see what the dealio is. I'm not sure I want to go through that whole thing with declaring the types for the package. It doesn't seem like it's a fatal error. I'm not sure if that's the reason that the animations aren't working or not.

Nope, I don't think it is the reason. I logged the `book.id` that gets passed into the render / return via this.state and it came back with this:

    index.js:1375 Warning: Failed prop type: Invalid prop `id` of type `object` supplied to `e`, expected `string`.
        in e (at BookDetail.js:41)

I think it's that same damn thing again. The object is empty when the `return()` method renders the component—the correct data is logged afterwards...ok I think I figured it out. I had to set the id state object—or whatever it is—to an empty string because that's what the function is expecting.

Ok well the animation is mostly working for the first half—it works on the way to the detail page, but doesn't seem to be doing so when going back to the list. I'm gnot going to dwell on this anymore...I at least got part of it working.

I ended up setting the id state parameter above the fetch because I figured that would work around the undefined error. I guess it worked?

```javascript
async componentDidMount() {
  try {
    const bookId = this.props.match.params.id;
    this.setState({
      id: this.props.match.params.id,
    });
```

I also feel like it could be partly due to the cropping I did to the image an didn't reuse the styled component - I created a new, identical one.

Ok...well I'm happy about a ton of things. Time to bring that happiness elsewhere.

Hasta happiness, amigas!
