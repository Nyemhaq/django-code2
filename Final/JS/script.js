const loadmen = () => {
    fetch("https://final-project-api-hvbn.onrender.com/products/list/")
        .then((res)=>res.json())
        // .then((data)=> console.log(data))
        .then((data)=> displaymen(data))
        .catch((err)=>console.log(err));
};

const displaymen = (men) => {
  let itemsInRow = 0; 
  men.forEach((man, index) => {
    console.log(man.id)
    if (man.category == 1 || man.category == 2 || man.category == 4 || man.category == 7) {
      if (itemsInRow === 0) {
        const parent = document.getElementById("men-container");
        const row = document.createElement("div");
        row.classList.add("row");
        parent.appendChild(row);
      }
      const parentRow = document.querySelector("#men-container .row:last-child");
      const div = document.createElement("div");
      div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
      div.innerHTML = `
        <div class="men-card">
          <img src="${man.image}" class="card-img-top" alt="...">
          <div class="card-body">
            <h6 class="card-title my-2">${man.name}</h6>
            <p class="card-text">TK ${man.price}.00</p>
            <a href="product-details.html?productID=${man.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
          </div>
        </div>
      `;
      parentRow.appendChild(div);

      itemsInRow++;
      if (itemsInRow === 3 || index === men.length - 1) {
        itemsInRow = 0;
      }
    }
  });
};




const loadpanjabi = () => {
    fetch("https://final-project-api-hvbn.onrender.com/products/list/")
        .then((res)=>res.json())
        // .then((data)=> console.log(data))
        .then((data)=> displaypanjabi(data))
        .catch((err)=>console.log(err));
};

const displaypanjabi = (men) => {
  let itemsInRow = 0; 
  men.forEach((man, index) => {
    console.log(man.id)
    if (man.category == 1) {
      if (itemsInRow === 0) {
        const parent = document.getElementById("men-container");
        const row = document.createElement("div");
        row.classList.add("row");
        parent.appendChild(row);
      }
      const parentRow = document.querySelector("#men-container .row:last-child");
      const div = document.createElement("div");
      div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
      div.innerHTML = `
        <div class="men-card">
          <img src="${man.image}" class="card-img-top" alt="...">
          <div class="card-body">
            <h6 class="card-title my-2">${man.name}</h6>
            <p class="card-text">TK ${man.price}.00</p>
            <a href="product-details.html?productID=${man.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
          </div>
        </div>
      `;
      parentRow.appendChild(div);

      itemsInRow++;
      if (itemsInRow === 3 || index === men.length - 1) {
        itemsInRow = 0;
      }
    }
  });
};


const loadshirt = () => {
  fetch("https://final-project-api-hvbn.onrender.com/products/list/")
      .then((res)=>res.json())
      // .then((data)=> console.log(data))
      .then((data)=> displayshirt(data))
      .catch((err)=>console.log(err));
};

const displayshirt = (men) => {
let itemsInRow = 0; 

men.forEach((man, index) => {
  if (man.category == 2) {
    if (itemsInRow === 0) {
      const parent = document.getElementById("shirt-container");
      const row = document.createElement("div");
      row.classList.add("row");
      parent.appendChild(row);
    }
    const parentRow = document.querySelector("#shirt-container .row:last-child");
    const div = document.createElement("div");
    div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
    div.innerHTML = `
      <div class="men-card">
        <img src="${man.image}" class="card-img-top" alt="...">
        <div class="card-body">
          <h6 class="card-title my-2">${man.name}</h6>
          <p class="card-text">TK ${man.price}.00</p>
          <a href="./product-details.html?productID=${man.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
        </div>
      </div>
    `;
    parentRow.appendChild(div);

    itemsInRow++;
    if (itemsInRow === 3 || index === men.length - 1) {
      itemsInRow = 0;
    }
  }
});
};


const loadtshirt = () => {
  fetch("https://final-project-api-hvbn.onrender.com/products/list/")
      .then((res)=>res.json())
      // .then((data)=> console.log(data))
      .then((data)=> displaytshirt(data))
      .catch((err)=>console.log(err));
};

const displaytshirt = (men) => {
let itemsInRow = 0; 

men.forEach((man, index) => {
  if (man.category == 4) {
    if (itemsInRow === 0) {
      const parent = document.getElementById("t-shirt-container");
      const row = document.createElement("div");
      row.classList.add("row");
      parent.appendChild(row);
    }
    const parentRow = document.querySelector("#t-shirt-container .row:last-child");
    const div = document.createElement("div");
    div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
    div.innerHTML = `
      <div class="men-card">
        <img src="${man.image}" class="card-img-top" alt="...">
        <div class="card-body">
          <h6 class="card-title my-2">${man.name}</h6>
          <p class="card-text">TK ${man.price}.00</p>
          <a href="./product-details.html?productID=${man.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
        </div>
      </div>
    `;
    parentRow.appendChild(div);

    itemsInRow++;
    if (itemsInRow === 3 || index === men.length - 1) {
      itemsInRow = 0;
    }
  }
});
};

const loadjeans = () => {
  fetch("https://final-project-api-hvbn.onrender.com/products/list/")
      .then((res)=>res.json())
      // .then((data)=> console.log(data))
      .then((data)=> displayjeans(data))
      .catch((err)=>console.log(err));
};

const displayjeans = (men) => {
let itemsInRow = 0; 

men.forEach((man, index) => {
  if (man.category == 7) {
    if (itemsInRow === 0) {
      const parent = document.getElementById("jeans-container");
      const row = document.createElement("div");
      row.classList.add("row");
      parent.appendChild(row);
    }
    const parentRow = document.querySelector("#jeans-container .row:last-child");
    const div = document.createElement("div");
    div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
    div.innerHTML = `
      <div class="men-card">
        <img src="${man.image}" class="card-img-top" alt="...">
        <div class="card-body">
          <h6 class="card-title my-2">${man.name}</h6>
          <p class="card-text">TK ${man.price}.00</p>
          <a href="./product-details.html?productID=${man.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
        </div>
      </div>
    `;
    parentRow.appendChild(div);

    itemsInRow++;
    if (itemsInRow === 3 || index === men.length - 1) {
      itemsInRow = 0;
    }
  }
});
};




const loadwoman = () => {
  fetch("https://final-project-api-hvbn.onrender.com/products/list/")
    .then((res) => res.json())
    .then((data) => displaywoman(data))
    .catch((err) => console.log(err));
};

const displaywoman = (women) => {
  let itemsInRow = 0;

  women.forEach((woman, index) => {
    if (woman.category == 3) {
      console.log(woman);
      if (itemsInRow === 0) {
        const parent = document.getElementById("woman-container")
        const row = document.createElement("div");
        row.classList.add("row");
        parent.appendChild(row);
        
      }
      const parentRow = document.querySelector("#woman-container .row:last-child");
      const div = document.createElement("div");
      div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
      div.innerHTML = `
          <div class="men-card">
            <img src="${woman.image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-title my-2">${woman.name}</h6>
              <p class="card-text">TK ${woman.price}.00</p>
              <a href="./product-details.html?productID=${woman.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
            </div>
          </div>
        `;
        parentRow.appendChild(div);

        itemsInRow++;
        if (itemsInRow === 3 || index === women.length - 1) {
          itemsInRow = 0;
        }
    }
  });
};




const loadboy = () => {
  fetch("https://final-project-api-hvbn.onrender.com/products/list/")
    .then((res) => res.json())
    .then((data) => displayboy(data))
    .catch((err) => console.log(err));
};

const displayboy = (boys) => {
  let itemsInRow = 0;

  boys.forEach((boy, index) => {
    if (boy.category == 5) {
      console.log(boy);
      if (itemsInRow === 0) {
        const parent = document.getElementById("boy-container")
        const row = document.createElement("div");
        row.classList.add("row");
        parent.appendChild(row);
        
      }
      const parentRow = document.querySelector("#boy-container .row:last-child");
      const div = document.createElement("div");
      div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
      div.innerHTML = `
          <div class="men-card">
            <img src="${boy.image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-title my-2">${boy.name}</h6>
              <p class="card-text">TK ${boy.price}.00</p>
              <a href="./product-details.html?productID=${boy.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
            </div>
          </div>
        `;
        parentRow.appendChild(div);

        itemsInRow++;
        if (itemsInRow === 3 || index === boy.length - 1) {
          itemsInRow = 0;
        }
    }
  });
};
  

  const loadgirl = () => {
    fetch("https://final-project-api-hvbn.onrender.com/products/list/")
        .then((res)=>res.json())
        // .then((data)=> console.log(data))
        .then((data)=> displaygirl(data))
        .catch((err)=>console.log(err));
  };
  
  const displaygirl = (girls) => {
    let itemsInRow = 0; 
    
    girls.forEach((girl, index) => {
      if (girl.category == 6) {
        if (itemsInRow === 0) {
          const parent = document.getElementById("girl-container");
          const row = document.createElement("div");
          row.classList.add("row");
          parent.appendChild(row);
        }
        const parentRow = document.querySelector("#girl-container .row:last-child");
        const div = document.createElement("div");
        div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
        div.innerHTML = `
          <div class="men-card">
            <img src="${girl.image}" class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-title my-2">${girl.name}</h6>
              <p class="card-text">TK ${girl.price}.00</p>
              <a href="./product-details.html?productID=${girl.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
            </div>
          </div>
        `;
        parentRow.appendChild(div);
    
        itemsInRow++;
        if (itemsInRow === 3 || index === girl.length - 1) {
          itemsInRow = 0;
        }
      }
    });
    };


    const loadeid = () => {
      fetch("https://final-project-api-hvbn.onrender.com/products/list/")
          .then((res)=>res.json())
          // .then((data)=> console.log(data))
          .then((data)=> displayeid(data))
          .catch((err)=>console.log(err));
    };
    
    const displayeid = (eids) => {
      let itemsInRow = 0; 
      
      eids.forEach((eid, index) => {
          if (itemsInRow === 0) {
            const parent = document.getElementById("eid-container");
            const row = document.createElement("div");
            row.classList.add("row");
            parent.appendChild(row);
          }
          const parentRow = document.querySelector("#eid-container .row:last-child");
          const div = document.createElement("div");
          div.classList.add("col-lg-4", "col-md-6", "col-sm-12");
          div.innerHTML = `
            <div class="men-card">
              <img src="${eid.image}" class="card-img-top" alt="...">
              <div class="card-body">
                <h6 class="card-title my-2">${eid.name}</h6>
                <p class="card-text">TK ${eid.price}.00</p>
                <a href="./product-details.html?productID=${eid.id}" target="_blank" class="btn btn-outline-warning" style="color:black">Details</a>
              </div>
            </div>
          `;
          parentRow.appendChild(div);
      
          itemsInRow++;
          if (itemsInRow === 3 || index === eid.length - 1) {
            itemsInRow = 0;
          }
      });
      };


loadeid()
loadgirl()
loadboy()
loadwoman()
loadjeans()
loadtshirt()
loadpanjabi()
loadshirt()

