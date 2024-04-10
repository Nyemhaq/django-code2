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
    console.log(product.id);
    
    const parentElement = document.getElementById("wishlist");
    if (!parentElement) {
      console.error("Parent element 'wishlist' not found.");
      return;
    }
  
    const div = document.createElement("div");
    div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
    div.innerHTML = `
      <div class="men-card">
        <img src="${product.image}" class="card-img-top" alt="...">
        <div class="card-body">
          <h6 class="card-title my-2">${product.name}</h6>
          <p class="card-text">TK ${product.price}.00</p>
          <a href="product-details.html?productID=${product.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
        </div>
      </div>
    `;
    parentElement.appendChild(div);
    alert("Product added to Wishlist Successfully!")
  };
  
getparams();
  