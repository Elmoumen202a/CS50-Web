# eBay-like E-Commerce Auction Site

This Django-based project implements an eBay-like e-commerce auction site with features such as creating listings, placing bids, adding listings to a watchlist, and commenting on listings. The following sections provide an overview of the project structure, features, and instructions for running the application.

## Auction Site Implementation

**Models**
The application includes the following models, in addition to the default Django User model:

- ***User:*** Default Django User model.
- ***Listing:** *Represents auction listings with fields such as title, description, starting bid, image URL, category, and status.
- ***Bid:*** Stores information about bids, including the bidder, amount, and the associated listing.
- ***Comment:*** Captures comments made on auction listings, containing the user, content, and the linked listing.

Feel free to customize these models based on your specific project requirements.

**Create Listing**
Users can create new auction listings through a dedicated page. They can specify a title, text-based description, starting bid, and optionally provide a URL for an image and/or select a category (e.g., Fashion, Toys, Electronics, Home, etc.).

**Active Listings Page**
The default route of the web application allows users to view all currently active auction listings. For each active listing, the page displays (at minimum) the title, description, current price, and a photo if available.
**Listing Page**
Clicking on a listing takes users to a page specific to that listing, where they can view all details about the listing, including the current price.
- If the user is signed in, they can add the item to their "Watchlist." If the item is already on the watchlist, the user can remove it.
- Signed-in users can bid on the item. The bid must be at least as large as the starting bid and greater than any other bids placed (if any). If the bid doesn't meet these criteria, an error is presented.
- If the user created the listing and is signed in, they have the ability to "close" the auction from this page. Closing the auction makes the highest bidder the winner and the listing no longer active.
- If a signed-in user is on a closed listing page and has won the auction, the page indicates so.
**Comments**
Users who are signed in can add comments to the listing page. The listing page displays all comments made on the listing.
**Watchlist**
Signed-in users can visit a Watchlist page, displaying all listings they have added. Clicking on any of those listings takes the user to that listing’s page.
**Categories**
Users can visit a page displaying a list of all listing categories. Clicking on the name of any category takes the user to a page displaying all active listings in that category.
**Django Admin Interface**
Via the Django admin interface, a site administrator can view, add, edit, and delete any listings, comments, and bids made on the site. This provides a convenient way to manage the content and activities within the auction site.

Feel free to explore and customize the implementation based on your specific needs and preferences.

## Getting Started

 **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/e-commerce-auction-site.git
   cd e-commerce-auction-site
