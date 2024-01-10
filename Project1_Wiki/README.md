# Wiki Encyclopedia Project

## Overview

This project is the implementation of a Wiki encyclopedia, following the specifications outlined below.

### Project Requirements

Your website must meet the following requirements:

1. **Entry Page:** Visiting `/wiki/TITLE`, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry. The view should get the content of the encyclopedia entry by calling the appropriate util function. If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found. If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.

2. **Index Page:** Update `index.html` such that, instead of merely listing the names of all pages in the encyclopedia, users can click on any entry name to be taken directly to that entry page.

3. **Search:** Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry. If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page. If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. Clicking on any of the entry names on the search results page should take the user to that entry’s page.

4. **New Page:** Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry. Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page. Users should be able to click a button to save their new page. When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message. Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

5. **Edit Page:** On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea. The textarea should be pre-populated with the existing Markdown content of the page. The user should be able to click a button to save the changes made to the entry. Once the entry is saved, the user should be redirected back to that entry’s page.

6. **Random Page:** Clicking “Random Page” in the sidebar should take the user to a random encyclopedia entry.

7. **Markdown to HTML Conversion:** On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the `python-markdown2` package to perform this conversion, installable via `pip3 install markdown2`.

### Demo

Watch a demo of the project on [YouTube](https://youtu.be/5IDqcg65iBM).

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/Elmoumen202a/CS50-Web.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

Visit `http://localhost:5000` in your web browser to interact with the Wiki encyclopedia.

## Contributors

- [Youssouf Elmoumen](https://github.com/Elmoumen202a)
- [CS50-Web](https://github.com/Elmoumen202a/CS50-Web)
- ...

## License

This project is licensed under the [MIT License](LICENSE).


Happy coding! 🚀
