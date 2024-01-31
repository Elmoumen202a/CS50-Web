# Email Client Front-End Project

## Project Overview
This project involves designing the front-end for an email client that communicates with a back-end API to send and receive emails. The implementation is focused on the `inbox.js` file, where JavaScript, HTML, and CSS are used to create a single-page application with various features.

## Project Requirements

### Send Mail
- Implement the functionality to send an email when the user submits the email composition form.
- Use a POST request to `/emails` with values for recipients, subject, and body.
- After sending the email, load the user’s sent mailbox.

### Mailbox
- Load the appropriate mailbox (Inbox, Sent, Archive) when the user visits.
- Use a GET request to `/emails/<mailbox>` to request the emails for a specific mailbox.
- Display the mailbox name at the top of the page.
- Render each email in its own box, showing sender, subject, and timestamp.
- Unread emails should have a white background; read emails should have a gray background.

### View Email
- Show the content of an email when a user clicks on it.
- Use a GET request to `/emails/<email_id>` to request the email details.
- Display sender, recipients, subject, timestamp, and body.
- Mark the email as read when clicked.
- Update views to hide and show the right components when navigating.

### Archive and Unarchive
- Allow users to archive and unarchive received emails.
- Provide buttons in the Inbox and Archive views for archiving and unarchiving.
- Use a PUT request to `/emails/<email_id>` to mark an email as archived or unarchived.
- After archiving or unarchiving, load the user’s inbox.

### Reply
- Enable users to reply to an email.
- Show a "Reply" button when viewing an email.
- Clicking the "Reply" button should navigate to the email composition form.
- Prefill the recipient field with the original email sender.
- Prefill the subject line with "Re: original_subject" if not already prefixed with "Re:".
- Prefill the body with a template including the original sender, timestamp, and email content.

## Implementation Details
- All front-end logic and functionality should be contained within the `inbox.js` file.
- Ensure proper event listeners are added to handle user interactions.
- Utilize appropriate HTML structure and CSS styling for a seamless user experience.

## Hints
- Refer to the provided hint in the Hints section for guidance on adding event listeners to dynamically added HTML elements.

## Additional Notes
- This readme file provides an overview of the project and its requirements. Detailed implementation steps and code snippets can be found in the `inbox.js` file.

Feel free to reach out for any clarifications or further assistance during the development process. Good luck!
