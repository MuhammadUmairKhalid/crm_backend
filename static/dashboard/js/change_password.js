document.getElementById("signInForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent the default form submission

    // Collect input values
    const oldPassword = document.getElementById("currentPassword").value; // Old password
    const newPassword1 = document.getElementById("newPassword1").value; // New password
    const newPassword2 = document.getElementById("newPassword2").value; // Confirm new password

    // Validate the new passwords match
    if (newPassword1 !== newPassword2) {
        alert("New passwords do not match.");
        return;
    }

    // Prepare the payload
    const payload = {
        old_password: oldPassword,
        new_password: newPassword1,
    };

    try {
        const response = await fetch("/api/update_password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${localStorage.getItem("token")}` // Replace with actual token retrieval logic
            },
            body: JSON.stringify(payload),
        });

        // Handle the response
        if (response.ok) {
            const data = await response.json();
            alert(data.message || "Password updated successfully.");
        } else {
            const errorData = await response.json();
            alert(
                errorData.old_password?.[0] || 
                errorData.new_password?.[0] || 
                errorData.detail || 
                "Failed to update password."
            );
        }
    } catch (error) {
        console.error("Error during password update:", error);
        alert("An error occurred while updating the password. Please try again later.");
    }
});
