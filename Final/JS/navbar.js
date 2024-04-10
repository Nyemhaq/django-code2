fetch('navbar.html')
    .then(response => response.text())
    .then(navbarHtml => {
        document.getElementById('navbar').innerHTML = navbarHtml;
    });