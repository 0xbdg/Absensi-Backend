const sidebar = document.getElementById('sidebar');
const menuButton = document.getElementById('menu-button');

menuButton.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full');
});