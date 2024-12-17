function addFormData(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Collect form data from the input fields
    const formData = {
        birth_state: document.getElementById("birth_state").value,
        phone: document.getElementById("phone").value,
        last_name: document.getElementById("last_name").value,
        first_name: document.getElementById("first_name").value,
        middle_name: document.getElementById("middle_name").value,
        address: document.getElementById("address").value,
        gender: document.getElementById("gender").value,
        zip_code: document.getElementById("zip_code").value,
        dob: document.getElementById("dob").value,
        weight: document.getElementById("weight").value,
        insurance_company: document.getElementById("insurance_company").value,
        ssn: document.getElementById("ssn").value,
        beneficiary_details: document.getElementById("beneficiary_details").value,
        health_conditions: document.getElementById("health_conditions").value,
        doctor_name: document.getElementById("doctor_name").value,
        doctor_address: document.getElementById("doctor_address").value,
        bank_name: document.getElementById("bank_name").value,
        routing_no: document.getElementById("routing_no").value,
        account_no: document.getElementById("account_no").value,
        account_type: document.getElementById("account_type").value,
        initial_draft_date: document.getElementById("initial_draft_date").value,
        future_draft_date: document.getElementById("future_draft_date").value,
        email: document.getElementById("email").value,
        policy_number: document.getElementById("policy_number").value,
        submission_date: document.getElementById("submission_date").value,
        drivers_license: document.getElementById("drivers_license").value,
        underwritten_by: document.getElementById("underwritten_by").value,
        jornaya_lead_id: document.getElementById("jornaya_lead_id").value,
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
