function submitForm() {
    // Get form values
    var username = document.getElementById("exampleFirstName").value;
    var email = document.getElementById("exampleInputEmail").value;
    var password = document.getElementById("exampleInputPassword").value;
    var repeatPassword = document.getElementById("exampleRepeatPassword").value;

    // Check if password and repeat password match
    if (password !== repeatPassword) {
        alert("Password and Repeat Password do not match. Please try again.");
        document.getElementById("exampleInputPassword").value = "";
        document.getElementById("exampleRepeatPassword").value = "";
        return;
    }

    // Create JSON object
    var userObject = {
        username: username,
        email: email,
        password: password,
        repeatPassword: repeatPassword
    };

    // Log JSON object to console 
    console.log(JSON.stringify(userObject));

    // Redirect to the login page after successful registration
    window.location.href = "login.html";
    
}
