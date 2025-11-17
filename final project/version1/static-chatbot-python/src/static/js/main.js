document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('query-form');
    const input = document.getElementById('query-input');
    const responseDiv = document.getElementById('response');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const query = input.value;

        fetch('/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: query })
        })
        .then(response => response.json())
        .then(data => {
            responseDiv.innerHTML = data.commands.join('<br>');
        })
        .catch(error => {
            console.error('Error:', error);
            responseDiv.innerHTML = 'An error occurred. Please try again.';
        });
    });
});