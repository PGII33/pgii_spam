function toggleVisibility(id) {
    var hiddenText = document.getElementById(id);

    if (window.getComputedStyle(hiddenText).display === "none") {
        hiddenText.style.display = "block";
    } else {
        hiddenText.style.display = "none";
    }
}