async function loadDashboard() {

    const userId = localStorage.getItem("user_id")

    const response = await fetch(`http://localhost:5000/dashboard/${userId}`)

    const data = await response.json()

    document.getElementById("jobs").innerHTML = data.matches

    document.getElementById("documents").innerHTML = data.documents

    document.getElementById("billing").innerHTML = "Active"
}

loadDashboard()