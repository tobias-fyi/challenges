# The Culture

## A Project 0 Site for Harvardx - CS50w

## By Tobias Reaper | tobias-fyi

----

This is a site about The Culture, a fictional far-future utopian society created by the late, great Iain M. Banks, with a page dedicated to him as well. 

The Culture Series is by far my favorite science-fiction series that I've read thus far (many times over). I copied / pasted the text from the relevant articles on Wikipedia (links are included below), with minor edits here and there for clarity and formatting. This site only contains a fraction of the information found on Wikipedia and other sites. However, I did not want to spend a week on formatting alone.

I thought using information and facts from the series would give me some freedom to be creative with fulfilling the project requirements. 

The site is arranged as follows:

project0
├── index.html
├── themes.html
├── books.html
├── author.html
├── ships.html
├── css
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── main.css
│   └── main.scss
└── img

More detailed information about what is contained within the pages:

* Included in all pages
  * Bootstrap Navbar
    * Sticky top, dark theme, responsive w/ toggle button
    * Navigation links to other pages on site
    * Current page has Bootstrap's active link class (styled white)
  * Page Header
    * Utilized Bootstrap columns to set up a responsive title / subtitle
    * On smaller displays the subtitle collapses to underneath the title
    * Background color is assigned via SCSS variable $brand-color

* index.html (Home / The Culture)
  * [Source (Wikipedia)](https://en.wikipedia.org/wiki/The_Culture)
  * Bootstrap blockquote
  * Mostly paragraphs explaining The Culture
  * 1 instance of a class I created (.text-highlight) for important blocks of text
    * I styled this class using SCSS inheritance from %special-quote
    * I wanted to try making a block of text that seemed to pop out without "leaving" the main page container, so used @media queries to change the margins, padding, and size for different displays

* themes.html (Themes)
  * [Source (Wikipedia)](https://en.wikipedia.org/wiki/The_Culture_(series))
  * Two instances of .text-highlight
  * Paragraphs that give an overview of the main themes in the series

* books.html (Books)
  * [Source (Wikipedia)](https://en.wikipedia.org/wiki/The_Culture_(series))
  * Dark background styled via #books-body and SCSS variable $brand-dark
  * 10 instances of a Bootstrap card component, one for each book that features:
    * Image depicting the book cover
    * Number in series and title
    * Short description or synopsis
    * Bootstrap list-group with year published and approximate year on the fictional timeline
    * Custom responsive sizing via class .book-card 
    * Responsive layout that displays two cards per row on large displays and one card per row on small displays

* author.html (The Author)
  * [Source (Wikipedia)](https://en.wikipedia.org/wiki/Iain_Banks)
  * 1 instance of .text-highlight
  * 1 instance of another class I created (.dot-separator) to emulate the elipses separator found on Medium articles
  * A few headlines, one of which is styled using #id selector
  * Bibliography section
    * Unordered lists with links to specific books on books.html
    * Links are styled using SCSS variables and pseudo-classes

* ships.html (Ships)
  * 
