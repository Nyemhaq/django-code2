// // const getparams = () =>
// // {
// //   const param = new URLSearchParams(window.location.search).get("man.id")
// //   console.log(param);
// //   fetch(`https://final-project-api-hvbn.onrender.com/products/list/${param}`)
// //   .then((res)=>res.json)
// //   // .then((data)=>console.log(data))
// //   .then((data)=>displaydetails(data))
// // };
// // const displaydetails = (product) =>{
// // const parent = document.getElementById("details-container");
// // const div = document.createElement("div");
// // div.innerHTML = `
// // <div class="col-6 col-lg-6 col-md-6 col-sm-12 my-3" >
// // <img src=${product.image} alt="">
// // </div>
// // <div class="col-6 col-lg-6 col-md-6 col-sm-12">
// // <h3>${product.name}</h3>
// // <h5>TK. ${product.Price}.00</h5>
// // <div class="d-flex">
// //     <button class="btn btn-outline-warning"  style="color:black">XXL</button>
// //     <button class="btn btn-outline-warning mx-2"  style="color:black">XL</button>
// //     <button class="btn btn-outline-warning"  style="color:black">L</button>
// //     <button class="btn btn-outline-warning mx-2" style="color:black">M</button>
// //     <button class="btn btn-outline-warning" style="color:black">S</button>
// // </div>
// // <h5 class="my-2">COLOR : WHITE</h5>
// // <h5>Quantity : 6</h5>
// // <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime nemo sed porro dolorem animi possimus totam, quis enim, officiis inventore reiciendis dolore voluptatum numquam itaque cupiditate, repellat soluta eius natus? Amet veritatis blanditiis debitis ipsa repellat molestiae? Id laboriosam necessitatibus provident sed corrupti recusandae esse quos eveniet eligendi? Sed, nisi debitis. Laudantium ea temporibus libero praesentium, vel incidunt ipsum impedit.</p>
// // <a class="btn btn-outline-warning px-5" href="./wishlist.html" target="_blank" style="align-items: center;font-family:Bebas Neue, sans-serif;
// // font-weight: 100;color:black">ADD TO WISHLIST</a>
// // <Button class="btn btn-warning" style="align-items: center;font-family:Bebas Neue, sans-serif;
// // font-weight: 100;">BUY NOW</Button>
// // <br>
// // <a class="btn btn-outline-warning my-2" href="./reviews.html" target="_blank" style="align-items: center;font-family:Bebas Neue, sans-serif;
// // font-weight: 100;color:black;padding-left:20%;padding-right:20%">Review</a>
// // </div>
// // </div>
// // </div>

// // `
// // parent.appendChild(div)

// // }



// // const getparams = () => {
// //   const param = new URLSearchParams(window.location.search).get("man.id");
// //   console.log(param);
// //   fetch(`https://final-project-api-hvbn.onrender.com/products/list/${param}`)
// //     .then((res) => res.json())
// //     // .then((data) => console.log(data));
// //     .then((data) => displaydetails(data));
// // };


const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("man.id");
    if (param) {
      console.log(param);
      fetch(`https://final-project-api-hvbn.onrender.com/products/${param}`)
        .then((res) => res.json())
        .then((data) => displaydetails(data))
        .catch((error) => console.error("Error fetching product:", error));
    } else {
      console.error("Parameter 'man.id' not found in the URL.");
    }
  };
  
  
  const displaydetails = (product) => {
    const parent = document.getElementById("details-container");
    const div = document.createElement("div");
    div.innerHTML = `
      <div class="col-6 col-lg-6 col-md-6 col-sm-12 my-3">
        <img src="${product.image}" alt="">
      </div>
      <div class="col-6 col-lg-6 col-md-6 col-sm-12">
        <h3>${product.name}</h3>
        <h5>TK. ${product.Price}.00</h5>
        <div class="d-flex">
          <button class="btn btn-outline-warning" style="color:black">XXL</button>
          <button class="btn btn-outline-warning mx-2" style="color:black">XL</button>
          <button class="btn btn-outline-warning" style="color:black">L</button>
          <button class="btn btn-outline-warning mx-2" style="color:black">M</button>
          <button class="btn btn-outline-warning" style="color:black">S</button>
        </div>
        <h5 class="my-2">COLOR : WHITE</h5>
        <h5>Quantity : 6</h5>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime nemo sed porro dolorem animi possimus totam, quis enim, officiis inventore reiciendis dolore voluptatum numquam itaque cupiditate, repellat soluta eius natus? Amet veritatis blanditiis debitis ipsa repellat molestiae? Id laboriosam necessitatibus provident sed corrupti recusandae esse quos eveniet eligendi? Sed, nisi debitis. Laudantium ea temporibus libero praesentium, vel incidunt ipsum impedit.</p>
        <a class="btn btn-outline-warning px-5" href="./wishlist.html" target="_blank" style="align-items: center;font-family:Bebas Neue, sans-serif;font-weight: 100;color:black">ADD TO WISHLIST</a>
        <button class="btn btn-warning" style="align-items: center;font-family:Bebas Neue, sans-serif;font-weight: 100;">BUY NOW</button>
        <br>
        <a class="btn btn-outline-warning my-2" href="./reviews.html" target="_blank" style="align-items: center;font-family:Bebas Neue, sans-serif;font-weight: 100;color:black;padding-left:20%;padding-right:20%">Review</a>
      </div>
    `;
    parent.appendChild(div);
  };
  
  getparams();
  
  
// //   getparams();