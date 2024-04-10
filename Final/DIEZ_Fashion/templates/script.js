const loadmen = () =>{
    fetch("https://fakestoreapi.com/products")
        .then((res)=>res.json())
        .then((data)=> console.log(data))
        // .then((data)=> displaymen(data))
        .catch((err)=>console.log(err));
};

loadmen()
// const displaymen = () => {
    
// };