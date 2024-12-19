function addFormData(event) {
    event.preventDefault();
    // Prevent the default form submission
    const last_name = document.getElementById("last-name").value;
    const first_name = document.getElementById("first-name").value;
    const middle_name = document.getElementById("middle-name").value;
    const name = `${first_name} ${middle_name} ${last_name}`;

    // Collect form data from the input fields
    const formData = {
        birth_state: document.getElementById("birth-state").value,
        phone_number: document.getElementById("phone").value,
        name: name,
        gender: document.getElementById("gender").value,
        address: document.getElementById("address").value,
        city : document.getElementById("city-state").value,
        zip_code :  document.getElementById("zip-code").value,
        dob: document.getElementById("dob").value,
        age: document.getElementById("age").value,
        height: document.getElementById("height").value,
        weight: document.getElementById("weight").value,
        insurance_company: document.getElementById("insurance-company").value,
        type_of_coverage: document.getElementById("coverage-type").value,
        coverage_amount: document.getElementById("coverage-amount").value,
        monthly_premium: document.getElementById("monthly-premium").value,
        social_security_number: document.getElementById("ssn").value,
        tobacco: document.getElementById("tobacco").value,
        beneficary: document.getElementById("beneficiary-details").value,
        health_condition: document.getElementById("health-conditions").value,
        medication: document.getElementById("medications").value,
        doctors_name: document.getElementById("doctor-name").value,
        doctors_address: document.getElementById("doctor-address").value,
        bank_name: document.getElementById("bank-name").value,
        account_type: document.getElementById("account-type").value,
        routing_number: document.getElementById("routing-number").value,
        account_number: document.getElementById("account-number").value,
        initial_draft_date: document.getElementById("initial-draft-date").value,
        future_draft_date: document.getElementById("future-draft-date").value,
        email: document.getElementById("email").value,
    };

    // Send the form data to the API
    fetch("/api/formdata/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Token " + localStorage.getItem("token"),
        },

        body: JSON.stringify({ form: formData }),
    })
    .then((response) => response.json()) 
    .then((data) => {    
        if (data.status === "success") {
            alert("Form submitted successfully!");
            window.location.href = "/agentform"; // Redirect to the agent form page
        } else {
            console.error("Error:", data.errors);
            alert( data.errors,"Form submission failed. Please check your input.");
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        alert(data.errors,"An error occurred while submitting the form.");
    });
}
