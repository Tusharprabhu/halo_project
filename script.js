// Get the sidebar and the toggle button by their IDs
const sidebar = document.querySelector('.sidebar');
const toggleButton = document.getElementById('toggle-sidebar');

// Add a click event listener to the button
toggleButton.addEventListener('click', function() {
    // Toggle the 'sidebar-hidden' class on the sidebar to show/hide it
    sidebar.classList.toggle('sidebar-hidden');
});
