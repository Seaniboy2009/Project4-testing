document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM loaded");
    let menu_button = document.getElementById("menu-toggle");

    menu_button.addEventListener("click", () => {
        console.log("menu button clicked")
    });
})
