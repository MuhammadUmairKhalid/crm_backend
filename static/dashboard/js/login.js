function login(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const data = {
        user_name: username,
        password: password
    };

    fetch("/api/login/", {
        method: "POST", 
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            localStorage.setItem("token", data.token);
            localStorage.setItem("name", data.username);
            console.log(data.role);  // Store the username
            localStorage.setItem("role", data.role);            // Store the role
        
            if (data.role === "agent") {
                window.location.href = "/agentform";
            }
            else if(data.role === "validator"){
                window.location.href = "/validate_form/";
            }
            else if(data.role === "admin"){
                window.location.href = "/admin";
            }
            else if(data.role === "superuser"){
                window.location.href = "/super_user/";
            }
            else {
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
    return false;
}

