const handlesignup = (event) => {
    event.preventDefault();
    
    const username = getvalue("username")
    const first_name = getvalue("first_name")
    const last_name = getvalue("last_name")
    const email = getvalue("email")
    const password = getvalue("password")
    const confirm_password = getvalue("confirm_password")
    const info =  {
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
    }
    if (password===confirm_password)
    {
        document.getElementById("error").innerText=""
        if(/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(password))
        {
            console.log(info)
            fetch("https://final-project-api-hvbn.onrender.com/customers/register/",
            {
                method:"POST",
                headers:{"content-type":"application/json"},
                body:JSON.stringify(info)
            })
            .then((res)=>res.json())
            .then((data)=>console.log(data));
        }
        else
        {
            document.getElementById("error").innerText="Password must contain minimum eight characters, at least one letter, one number and one special character"
        }
    }
    else
    {
        alert("Password doesn't match")
        document.getElementById("error").innerText="Password doesn't match"
    }
};


const handlelogin = (event) => {
    event.preventDefault()
    const username = getvalue("username");
    const password = getvalue("password");
    console.log(username,password)
    fetch("https://final-project-api-hvbn.onrender.com/customers/login/",
    {
        method:"POST",
        headers:{"content-type":"application/json"},
        body:JSON.stringify({username,password}),
    })
    .then((res)=>res.json())
    .then((data)=> {
        console.log(data);
        if (data.token && data.user_id){
            localStorage.setItem("token",data.token);
            localStorage.setItem("user_id",data.user_id);
            window.location.href="index.html"
        }
       else
       {
         alert("Wrong Username or Password")
       }
    })
}


const getvalue = (id) => {
    const value = document.getElementById(id).value;
    return value;
};