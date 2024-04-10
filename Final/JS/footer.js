fetch('footer.html')
    .then(response => response.text())
    .then(navbarHtml => {
        document.getElementById('footer').innerHTML = navbarHtml;
    });