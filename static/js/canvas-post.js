let dataURI = window.sessionStorage.getItem('drawing');

function setDrawing(blob){
    let fileName = new Date().getTime() + '.png'
    let file = new File([blob], fileName,{type:"image/png", lastModified:new Date().getTime()}, 'utf-8');
    let container = new DataTransfer(); 
    container.items.add(file);
    document.querySelector('#id_drawing').files = container.files;
    console.log(document.querySelector('#id_drawing'))
}

if (dataURI) {
    fetch(dataURI)
    .then(res => res.blob())
    .then(blob => setDrawing(blob))

    let preview = document.getElementById('drawing_preview')
    preview.src = dataURI

    window.onbeforeunload = function(){
        window.sessionStorage.removeItem('drawing')
    }
}
else {
    document.getElementById('redirect').click()
}

