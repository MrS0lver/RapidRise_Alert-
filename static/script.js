// Get modal elements
const modal = document.getElementById("register-modal");
const registerBtn = document.getElementById("register-btn");
const closeBtn = document.querySelector(".close");

// Show modal
registerBtn.addEventListener("click", () => {
    modal.style.display = "block";
});

// Close modal
closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

// Close modal when clicking outside
window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});
