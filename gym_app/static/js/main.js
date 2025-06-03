console.log('This is JS from your page!!')

window.addEventListener('message', function (event) {
    if (event.data.type === 'OAUTH_SUCCESS') {
        // Handle successful login
        console.log('Login successful!', event.data.token);
        // You might want to reload or redirect
        window.location.reload();
    }
});