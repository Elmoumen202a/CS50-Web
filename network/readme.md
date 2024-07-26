# Social Network Project

Welcome to the Social Network project! This implementation uses Python, JavaScript, HTML, and CSS to create a fully functional social network. Below are the specifications and features you need to complete:

## Specifications

### New Post
- **Feature**: Users who are signed in should be able to write a new text-based post.
- **Details**: 
  - Users fill in text into a text area and then click a button to submit the post.
  - The “New Post” box can be at the top of the “All Posts” page or on a separate page.

### All Posts
- **Feature**: View all posts from all users with the most recent posts first.
- **Details**: 
  - Each post should include the username of the poster, the post content, the date and time of posting, and the number of “likes”.

### Profile Page
- **Feature**: Display user's profile page.
- **Details**: 
  - Shows the number of followers and followings.
  - Displays all posts by the user in reverse chronological order.
  - Provides a “Follow” or “Unfollow” button for other users’ profiles.

### Following
- **Feature**: View posts made by users that the current user follows.
- **Details**: 
  - Behaves like the “All Posts” page but only shows posts from followed users.
  - This page is only accessible to signed-in users.

### Pagination
- **Feature**: Display posts 10 per page.
- **Details**: 
  - Includes “Next” and “Previous” buttons for navigation through pages of posts.

### Edit Post
- **Feature**: Users can edit their own posts.
- **Details**: 
  - Clicking “Edit” replaces the post content with a textarea for editing.
  - Users can save the edited post without reloading the page.
  - Ensure users cannot edit other users’ posts.

### “Like” and “Unlike”
- **Feature**: Users can toggle “like” on any post.
- **Details**: 
  - Asynchronously update the like count using JavaScript and update the displayed like count without reloading the page.

## Technologies Used
- **Python**: Backend logic and server-side operations.
- **JavaScript**: Client-side interactivity and asynchronous operations.
- **HTML**: Structure and layout of web pages.
- **CSS**: Styling and design of web pages.

## How to Run
1. Clone the repository.
2. Set up the virtual environment and install the required packages.
3. Run the server.
4. Access the application through the provided local server URL.

## Contributing
We welcome contributions! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.
