async function fetchData() {
    const res = await fetch("https://api.chucknorris.io/jokes/random");
    const record = await res.json();
    document.getElementById("date").innerHTML = "N/A"; // No date field in API response
    document.getElementById("areaName").innerHTML = "N/A"; // No areaName field in API response
    document.getElementById("latestBy").innerHTML = "N/A"; // No latestBy field in API response
    document.getElementById("deathNew").innerHTML = record.value; // Joke text
}
fetchData();