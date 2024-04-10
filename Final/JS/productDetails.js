const getparams = () =>
{
  const param = new URLSearchParams(window.location.search).get("productID")
  console.log(param);
  fetch(`https://final-project-api-hvbn.onrender.com/products/list/${param}/`)
  .then((res)=>res.json())
//   .then((data)=>console.log(data))
  .then((data)=>displayProductDetails(data))
};


const displayProductDetails = (product) => {
    const productDetailsContainer = document.getElementById("product-details");
    
    const productHTML = `
        <div class="product row d-flex mt-5">
          <div class="col-6 col-lg-6 col-md-6 col-sm-12">
            <img style="width:80%" src="${product.image}" alt="image">
          </div>
          <div class="col-6 col-lg-6 col-md-6 col-sm-12">
            <h2>${product.name}</h2>
            <h4>Price: TK ${product.price}.00</h4>
            <p>Description: ${product.details}</p>
            <button class="btn btn-warning" onclick="buyNow('${product.id}')">Buy Now</button>
            <a href="./wishlist.html?productID=${product.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Add to Wishlist</a>
            <a href="./reviews.html" class="btn btn-outline-success" style="color:black" >Reviews</a>
            </div>
        </div>
            `;
            
            productDetailsContainer.innerHTML = productHTML;
        };

        const buyNow = (productId) => {
          const successMessage = document.getElementById("success-message");
          successMessage.style.display = "block";
          successMessage.textContent = "Product Bought Successfully!";
        };
        

getparams()