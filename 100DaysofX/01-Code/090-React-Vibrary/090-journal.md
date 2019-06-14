# 2019-06-01 | #100DaysofCode

    GOAL-06-01 ~ workon Vibrary  

## Day 090/100 | 152/365

- [2019-06-01 | #100DaysofCode](#2019-06-01--100daysofcode)
  - [Day 090/100 | 152/365](#day-090100--152365)
  - [Razzmatazz React](#razzmatazz-react)
    - [18:42 ~ Back to React](#1842--back-to-react)
    - [00:17 ~ Back For Some Bits](#0017--back-for-some-bits)
      - [00:52 ~ APIs R Funambulistic](#0052--apis-r-funambulistic)
      - [01:04 ~ Ol' Faithful Functionalism](#0104--ol-faithful-functionalism)

---- Sojourn ----

## Razzmatazz React

### 18:42 ~ Back to React

Starting up the vibrary once again to get some learning in before heading out to drop off Kels at the airport and see my friend play a show.

Damn now that I'm utilizing all three screens with different active things, my computer is chugging—fan has been going on and off for a while now.

Starting off at the beginning of the video that I left off on—I left off about halfway through but started from the beginning just in case I missed anything. Here's the code I have so far for the asynchronous fetch request:

```javascript
class App extends React.Component {

    async componentDidMount() {
        try {
            const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=mainCategory:fiction&key=N0tY0Ur4P1k3Y!');
            const books = await res.json();
            console.log(books);
        } catch (e) {
            console.log(e)
        }
    }
```

Updated settings.json to give markdown files a tab size of 2. Also, I downscaled the big display to hopefully help my computer not run its fan all the time. We'll see if it helps at all...it didn't seem to.

So I'm going to try to make due with only the HUGE display and see how the performance is. It was perfectly fine up to this point. I also turned off and unplugged my audio interface. Seeing how low I can get my CPU, or if none of this really makes a difference then I'll try something else.

SAweeeet! I managed to replace the dummy titles that display in the component with real titles pulled from the API. I received a warning because the default prop is not set up correctly (as the book information, such as title, is one level down).

    Warning: Failed prop type: The prop `book.title` is marked as required in `Book`, but its value is `undefined`.
        in Book (at App.js:32)
        in App (at src/index.js:7)

I will have to figure that out when I return.

---

### 00:17 ~ Back For Some Bits

Seeing as it's already past midnight and I'm just getting back to the station, I probably will only be doing a bit o' work before calling it

I'm thinking that in order to address the warning above, I'll need to add an extra layer to the default prop declaration (if that's even the right term for it). Here is what the Book component looks like now:

```jsx
export default class Book extends React.Component {
    static propTypes = {
        book: PropTypes.shape({
            title: PropTypes.string.isRequired,
        }),
    }

    render() {
    return (
        <div>
            <h3>{this.props.book.volumeInfo.title}</h3>
        </div>
    );
    }
}
```

By "extra layer" I mean the title prop should be inside another object/prop called volumeInfo.

```javascript
static propTypes = {
    book: PropTypes.shape({
        volumeInfo: PropTypes.shape({
            title: PropTypes.string.isRequired,
        }),
    }),
}
```

No idea if I'm even thinking about this correctly. I might try it out and if it doesn't work take a quick look through the documentation.

Well, even before I opened up the dev console in firefox, I can see that the data still came in from the API. That means it still worked. Whether or not there is another warning...that's another thing entirely because apparently the warning isn't a fatal one—aka it wasn't an error.

Wow there is not error in the console! Sweet. *I am now the master of APIs*.

Damn the fan on my laptop got cranking within a few minutes of starting, and I'm seeing some lag in the big display...I wonder if my computer's graphics card just doesn't like doing 4k @ 50hz

I'm going to see if I can get more than 10 books from the API at once. Here's the fetch call:

```javascript
const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=mainCategory:fiction&key=N0tY0Ur4P1k3Y!');
// The fetch below is something I wrote the other night to search for Iain Banks novels.
// I don't think it worked. I'll try again later
// const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=inauthor=banks&prettyPrint=true&key=N0tY0Ur4P1k3Y!')
```

Going to add another piece to the url query...

```javascript
const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=mainCategory:fiction&prettyPrint=true&key=N0tY0Ur4P1k3Y!');
```

Actually...I'm going to try out the new author query with the `Iain` part added.

```javascript
const res = await fetch('https://www.googleapis.com/books/v1/volumes?q=inauthor=iain+banks&prettyPrint=true&key=N0tY0Ur4P1k3Y!')
```

Man my computer is *really* chugging away with that fan. Not sure if I like that it's doing that. Maybe I should've bought a new HDMI cable as well, as this didn't happen at all with the old HDMI cable. I could still use that one if I need to, but I might buy another one to test out the performance with a state-of-the-art HDMI.

#### 00:52 ~ APIs R Funambulistic

...I saved the `App.js` before I started writing that last paragraph and didn't look at the results until now. It worked! Now I'm seeing a list of only Iain Banks novels. Awesome!

Ok the time stamp above is when my computer shut its fan off—temperature read 120˚. Let's see how long it stays there / how long it takes to go back up to fan-temp.

Holy shit...it was steady around 125˚ for a minute...then shot back up to 180˚ within 3 minutes.

It's 00:55 now and the gauge reads 187˚...and...yet I can hear the fan starting to ramp itself up...interesting, because the computer itself does not feel particularly hot.

----ƒ----

I also had another idea to try out tomorrow—I can test things out using the HDMI that my roommate uses with his Apple TV. He has (I think) the latest model that runs 4k, so the HDMI cable that came with it should be one of the real nice / capacitive ones.

I really don't want to keep listening to my fan. I'm going to swap out the displayport for the my girlfriend's HDMI and see how it does.

#### 01:04 ~ Ol' Faithful Functionalism

Ok now I can definitely feel the lag—and I can tell that the colors are not nearly as good via HDMI. Interesting. My computer was at 121˚ at the timestamp above. Let's see what it does.

4 minutes later and we're back up to 170˚...I'm starting to think that it's actually Firefox that's causing the high temperature. Not Firefox in general, but it seems to be whenever I start playing the tutorial, which is an embedded youtube video in the leveluptuts site.

If that is indeed the cause, I might just download the tutorial video files and see if playing them from the filesystem helps. I was hoping that I could download each video individually, but it seems the only way is to get the entire series. It's not bad though—zipped it comes out to 1.2 gigs.

There we are...fan is ramping up again / temp is back up to mid 180s. However, I'm not as surprised this time because I'm downloading a large file.

...ugh I don't want to have to try Chrome again. But I might just to test it out. The videos are done downloading so I'm going to wait on that. Temp is back down to 160˚.

I think it's about that time...

Hasta luego, amigo!
