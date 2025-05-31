
    document.getElementById('save-button').addEventListener('click', function() {
        const workoutData = collectWorkoutData();
        
        // Here you can send the data to your server
        // For example using fetch:
        fetch('/user/save-workout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // For Django CSRF protection
            },
            body: JSON.stringify(workoutData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Workout saved successfully!');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Error saving workout');
        });
    });