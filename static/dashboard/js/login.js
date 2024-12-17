function login(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const data = {
        user_name: username,
        password: password
    };

    fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST", 
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            console.log(data)
            if (data.role === "agent") {
                localStorage.setItem("token", data.token);
                window.location.href = "/agentform";
            } else {
                alert("Unauthorized role");
            }
        } else {
            console.log(data)
            alert("Login failed. Please check your credentials.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
    });
    return false;
}
