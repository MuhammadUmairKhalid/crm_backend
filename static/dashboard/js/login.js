function login() {
    // Get username and password from input fields
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Prepare the request payload
    const data = {
        username: username,
        password: password
    };

    // Send data to the API using fetch
    fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",  // HTTP method
        headers: {
            "Content-Type": "application/json",  // Set the content type to JSON
        },
        body: JSON.stringify(data),  // Convert data to JSON
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        // Check if the status is success
        if (data.status === "success") {
            // Check if the role is 'agent'
            if (data.role === "agent") {
                // Redirect to the agent's dashboard
                window.location.href = "/agentform"; // Adjust the URL to your agent dashboard
            } else {
                alert("Unauthorized role");
            }
        } else {
            alert("Login failed. Please check your credentials.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    });
}
