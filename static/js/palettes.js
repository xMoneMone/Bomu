const colors = document.getElementsByClassName("color")

function colourAssignment(colour) {
    colour.style.backgroundColor = colour.title
}

Array.from(colors).forEach(colourAssignment);
