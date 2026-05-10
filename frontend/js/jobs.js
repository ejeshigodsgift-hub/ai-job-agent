async function loadJobs() {

    const response = await fetch("http://localhost:5000/jobs/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            skill: "Python"
        })
    })

    const data = await response.json()

    document.getElementById("job-list").innerHTML = JSON.stringify(data)
}

loadJobs()