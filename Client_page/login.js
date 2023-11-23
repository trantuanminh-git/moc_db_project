function submitForm() {

    event.preventDefault();
    // Get the entered username and password
    var username = document.getElementById('exampleInputEmail').value;
    var password = document.getElementById('exampleInputPassword').value;

    // Check if username or password fields are empty
    if (username.trim() === '' || password.trim() === '') {
        alert('Please enter both username and password');
    } else {
        // Create a JSON object with the entered data
        var loginData = {
            username: username,
            password: password
            // You can add more data if needed
        };

        fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(loginData),
          })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              alert('Login successful');
            } else {
              alert('Login failed');
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
    }
}