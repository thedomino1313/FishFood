async function rotate() {
    document.getElementById("rotateLabel").textContent = "Rotating!"
    fetch('/rotate', {
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
}

async function clearRotate() {
    document.getElementById("rotateLabel").textContent = "Waiting for rotate command..."
}