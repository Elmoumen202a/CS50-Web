function getCookie(name) {
    const x = `; ${document.cookie}`;
    const y = x.split(`; ${name}=`);
    if (y.length == 2) return y.pop().split(';').shift();
}

function submitHandler(id) {
    const textareaValue = document.getElementById(`textarea_${id}`).value;
    const modal = document.getElementById(`editModal${id}`);
    const editButton = document.getElementById(`editButton_${id}`);
    const contentElement = document.getElementById(`content_${id}`);

    fetch(`/edit/${id}`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ 
            content: textareaValue 
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(error => { throw new Error(error.message) });
        }
        return response.json();
    })
    .then(result => {
        if (result.status === 'success') {
            contentElement.innerHTML = result.content;

            // Hide the edit button
            if (editButton) {
                editButton.style.display = 'none';
            }

            // Hide the modal using Bootstrap's modal methods
            $(modal).modal('hide');

            // Remove modal backdrops
            const modalsBackdrops = document.getElementsByClassName('modal-backdrop');
            while (modalsBackdrops.length > 0) {
                document.body.removeChild(modalsBackdrops[0]);
            }
        } else {
            alert(`Error: ${result.message}`);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while updating the post');
    });
}

// create a new function likeHandler
function likeHandler(id, likes_by_user) {
   const btn = document.getElementById(`${id}`);

   btn.classList.remove('fa-thumbs-up')
   btn.classList.remove('fa-thumbs-down')
    
    if (likes_by_user.indexOf(id) >= 0) {
        var liked = true;
    } else {
        var liked = false;
    }

    if (liked === true) {
        fetch(`/remove_liked/${id}`)
        .then(response => response.json)
        .then(result => {
            btn.classList.add('fa-thumbs-up');
        })
    }
    else {
        fetch(`/add_liked/${id}`)
        .then(response => response.json)
        .then(result => {
            btn.classList.add('fa-thumbs-down');
        })
    }
    liked = !liked

}
