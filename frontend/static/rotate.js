window.onload = async function() {
    // Code to execute after the page has fully loaded
    await fetch('/stepper_diagnostic', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (!data.value) {
            location.href = "connection.html";
        }
    });
};

async function rotate() {
    document.getElementById("rotateButton").disabled = true;
    document.getElementById("clearRotateButton").disabled = true;
    document.getElementById("rotateLabel").textContent = "Rotating!";
    await fetch('/rotate', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.value) {
            console.log("yippee")
            document.getElementById("rotateLabel").textContent = "Rotated successfully!"
        } else {
            console.log("L + ratio")
            document.getElementById("rotateLabel").textContent = "Rotate failed :("
        }
    });
    document.getElementById("rotateButton").disabled = false;
    document.getElementById("clearRotateButton").disabled = false;
}

async function clearRotate() {
    document.getElementById("rotateLabel").textContent = "Waiting for rotate command...";
}