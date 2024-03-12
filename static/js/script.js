document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('sentiment-form');
    var resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        var inputText = document.getElementById('input-text').value;

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'text=' + encodeURIComponent(inputText)
        })
        .then(response => response.text())
        .then(data => {
            resultDiv.innerText = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
