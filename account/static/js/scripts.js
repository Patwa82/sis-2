document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const password = document.querySelector('input[name="password1"]');
        const passwordConfirm = document.querySelector('input[name="password2"]');
        
        if (password.value !== passwordConfirm.value) {
            alert("Passwords do not match");
            event.preventDefault();
        }
    });
});
