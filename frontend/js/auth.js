async function signup() {

    const response = await fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            full_name: document.getElementById("fullname").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    })

    const data = await response.json()

    alert(data.message)
}


async function login() {

    const response = await fetch("http://localhost:5000/signin", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    })

    const data = await response.json()

    localStorage.setItem("user_id", data.user_id)

    window.location.href = "dashboard.html"
}