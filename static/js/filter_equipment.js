// Helper function to extract Django's CSRF token from cookies
function getCsrfToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, 10) === ('csrftoken=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
}

// Target the checkboxes directly rather than the list item containers
const equipmentCheckboxes = document.querySelectorAll(".equipment-list input[type='checkbox']");

equipmentCheckboxes.forEach((checkbox) => {
    // Using 'change' is safer than 'click' for checkboxes inside labels
    checkbox.addEventListener("change", (event) => {
        const targetCheckbox = event.target;

        // Pull the ID from the checkbox (Assumes you added value or data-id to the HTML element)
        const equipmentId = targetCheckbox.value;
        const isChecked = targetCheckbox.checked;

        // Configuration payload to send to your Django view
        const targetUrl = "/filter-equipment/"; // <-- Swap this with your actual template/URL route
        const payload = {
            equipment_id: equipmentId,
            active: isChecked
        };

        // Fire off the asynchronous POST request
        fetch(targetUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCsrfToken() // Keeps Django security happy
            },
            body: JSON.stringify(payload)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response encountered an error.");
                }
                return response.json();
            })
            .then(data => {
                console.log("Server Response Success:", data);

                // OPTIONAL: Do frontend updates here based on your view's response
                // e.g., if (data.status === 'success') { ... }
            })
            .catch(error => {
                console.error("Fetch Operation Failed:", error);

                // Revert the checkbox visual state if the database update failed
                targetCheckbox.checked = !isChecked;
                alert("Could not update equipment visibility. Retrying...");
            });
    });
});