window.onload = async function() {
    // Code to execute after the page has fully loaded
    await fetch('/stepper_diagnostic', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.value) {
            location.href = "rotate.html";
        }
    });
};


async function connect() {
    document.getElementById("connectLabel").textContent = "Attempting to connect...";
    await fetch('/connect', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.value) {
            document.getElementById("connectLabel").textContent = "Rotate time!";
            location.href = "rotate.html";
        } else {
            console.log("L + ratio")
            document.getElementById("connectLabel").textContent = "Uh oh! Couldn't connect to the Discovery Board.";
        }
    });
}