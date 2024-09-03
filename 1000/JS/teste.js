const inputName = document.querySelector("#name")

inputName.addEventListener("keypress", function(e){
    const keyCode = (e.keyCode ? e.keyCode : e.wich);

    if(keyCode > 47 && keyCode < 58){
        e.preventDefault();
    }
});


document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var confirmationMessage = document.getElementById('confirmationMessage');
    confirmationMessage.style.display = 'block';

    setTimeout(function() {
        window.location.href = 'index.html';
    }, 2000);
});