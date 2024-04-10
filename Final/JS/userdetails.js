const loadUserDetails = () => {
    const user_id = localStorage.getItem("user_id");
    console.log(user_id)
    fetch(`https://final-project-api-hvbn.onrender.com/customers/list/${user_id}`)
    .then((res)=>res.json())
    .then((data)=>console.log(data))
}

loadUserDetails()