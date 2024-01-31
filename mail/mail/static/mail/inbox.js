document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // submit
  document.querySelector("#compose-form").addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-detail').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

// // view email ,show details of email
function view_email(id) {
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(emails => {
      // Print emails
      console.log(emails);

      // hide the mailbox and show emails-detail
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#emails-detail').style.display = 'block';

      // show in HTML
      document.querySelector('#emails-detail').innerHTML = `
        <ul class="list-group list-group-flush">
          <li class="list-group-item"><strong>From:</strong>${emails.sender}</li>
          <li class="list-group-item"><strong>To:</strong>${emails.recipients}</li>
          <li class="list-group-item"><strong>Subject:</strong>${emails.subject}</li>
          <li class="list-group-item"><strong>Timestamp:</strong>${emails.timestamp}</li>
          <li class="list-group-item">${emails.body}</li>
        </ul>
      `;

      // change to read
      if (!emails.read) {
        fetch(`/emails/${emails.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            read: true
          })
        })
          .then(response => response.json())
          .then(result => {
            console.log(result);
            // Change color after marking as read
            document.querySelector('#emails-view div[data-id="' + id + '"]').style.backgroundColor = 'gray';
          })
          .catch(error => {
            console.error('Error marking email as read:', error);
          });
      }
      //// Archive/Unarchive
      const element_arch = document.createElement('button');
      element_arch.innerHTML = emails.archived ? "Unarchive" : "Archive" ;
      element_arch.className = emails.archived ? "btn btn-success" : "btn btn-warning" ;
      element_arch.addEventListener('click', function() {
        fetch(`/emails/${emails.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !emails.archived // will be always the #
          })
        })
        .then( () => {load_mailbox('archived')})// 
      });
      document.querySelector('#emails-detail').append(element_arch);
      // Add space
      const space = document.createElement('span');
      space.innerHTML = '&nbsp;';
      document.querySelector('#emails-detail').append(space);
      // // reply
      const element_reply = document.createElement('button');
      element_reply.innerHTML = "Reply" ;
      element_reply.className =  "btn btn-primary" ;
      element_reply.addEventListener('click', function() {
        compose_email();

          //  composition fields
          document.querySelector('#compose-recipients').value = emails.sender;
          let subject=emails.subject;
          if(subject.split(' ',1)[0] !="Re:"){ subject="Re: "+emails.subject;}
          document.querySelector('#compose-subject').value = subject;
          document.querySelector('#compose-body').value = `On ${emails.timestamp} ${emails.sender} wrote: ${emails.body} 
          --------------------------------------------------------------------
          `;

      });
      document.querySelector('#emails-detail').append(element_reply);

    });
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-detail').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // // have the emails and user for the mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // // loop through each email / create a div for each
    emails.forEach(singleEmail => {
      
      console.log(singleEmail);
      // // div for each  email
      const newEmail = document.createElement('div');
      newEmail.classList.add("list-group-item"); // Add the base class first
      newEmail.innerHTML = `
        <h5>Sender: ${singleEmail.sender}</h5>
        <h3>Subject: ${singleEmail.subject}</h3>
        <p>${singleEmail.timestamp}</p>
      `;
      
      // Check read status and set background color accordingly
      if (singleEmail.read) {
        newEmail.style.backgroundColor = 'gray'; // for read emails
        newEmail.style.border = '1px solid black';
      } else {
        newEmail.style.backgroundColor = 'white'; // for unread emails
        newEmail.style.border = '1px solid black';
      }

      // click event to view email
      newEmail.addEventListener('click', function () {
        view_email(singleEmail.id)
      });
      document.querySelector('#emails-view').append(newEmail);

    });

});
}


function send_email(event){ 
  event.preventDefault();
  // // save fields
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value ;
  // // send data , to backend
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      // //
      load_mailbox('sent');
  });

}

