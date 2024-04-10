const handleReview = (event) => {
    event.preventDefault();

    const customer = document.getElementById("customer").value;
    const product = document.getElementById("product").value;
    const ratings = document.getElementById("ratings").value;
    const review = document.getElementById("review").value;

    const info = {
        customer,
        product,
        ratings,
        review
    };

    console.log(info);

    fetch("https://final-project-api-hvbn.onrender.com/products/reviews/",
    {
        method:"POST",
        headers:{"content-type":"application/json"},
        body:JSON.stringify(info)
    })
    .then((res)=>res.json())
    .then((data)=>console.log('Review saved successfully',data));


    document.getElementById('customer').value = '';
    document.getElementById('product').value = '';
    document.getElementById('ratings').value = '';
    document.getElementById('review').value = '';
}
