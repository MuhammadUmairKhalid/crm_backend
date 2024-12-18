function addFormData(event) {
    event.preventDefault();
    // Prevent the default form submission
    const last_name = document.getElementById("last_name").value;
    const first_name = document.getElementById("first_name").value;
    const middle_name = document.getElementById("middle_name").value;
    const name = `${first_name} ${middle_name} ${last_name}`;

    // Collect form data from the input fields
    const formData = {
        birth_state: document.getElementById("birth_state").value,
        phone_number: document.getElementById("phone_number").value,
        name: name,
        gender: document.getElementById("gender").value,
        address: document.getElementById("address").value,
        city : document.getElementById("city").value,
        zip_code :  document.getElementById("zip_code").value,
        dob: document.getElementById("dob").value,
        age: document.getElementById("age").value,
        height: document.getElementById("height").value,
        weight: document.getElementById("weight").value,
        insurance_company: document.getElementById("insurance_company").value,
        type_of_coverage: document.getElementById("type_of_coverage").value,
        coverage_amount: document.getElementById("coverage_amount").value,
        monthly_premium: document.getElementById("monthly_premium").value,
        social_security_number: document.getElementById("social_security_number").value,
        tobacco: document.getElementById("tobacco").value,
        beneficary: document.getElementById("beneficary").value,
        health_condition: document.getElementById("health_condition").value,
        medication: document.getElementById("medication").value,
        doctors_name: document.getElementById("doctors_name").value,
        doctors_address: document.getElementById("doctors_address").value,
        bank_name: document.getElementById("bank_name").value,
        account_type: document.getElementById("account_type").value,
        routing_number: document.getElementById("routing_number").value,
        account_number: document.getElementById("account_number").value,
        initial_draft_date: document.getElementById("initial_draft_date").value,
        future_draft_date: document.getElementById("future_draft_date").value,
        email: document.getElementById("email").value,
    };

    // Send the form data to the API
    fetch("/api/formdata/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Token " + localStorage.getItem("token"), // Token stored in localStorage
        },

        body: { form: formData }, // Send data under "form" key
    })
    .then((response) => response.json()) // Parse the JSON response
    .then((data) => {    
        console.log(data);
        if (data.status === "success") {
            alert("Form submitted successfully!");
            window.location.href = "/agentform"; // Redirect to the agent form page
        } else {
            console.error("Error:", data.errors);
            alert("Form submission failed. Please check your input.");
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred while submitting the form.");
    });
}
