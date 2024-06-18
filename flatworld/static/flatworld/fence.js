import {createPopup} from './flatworld.js';

document.addEventListener('DOMContentLoaded', function() {
    let generateFence = document.getElementById('generateFence'); 
    if (generateFence){
        generateFence.addEventListener('click', fence);
    }
    let seeNeighbors = this.getElementById('showTable');
    if(seeNeighbors){
        seeNeighbors.addEventListener('click', neighbors);
    }
});

function fence(){
    let url = new URL(window.location.href);
    let params = new URLSearchParams(url.search.slice(1));

    params.append('fence', '');

    url.search = params.toString();

    console.log("URL: ", url); // log the URL

    fetch(url)
    .then(response => response.json())
      .then(data => {
        console.log(data.cost);
        let h3 = document.createElement('h3');
        h3.innerHTML = "Koszt ogrodzenia: <span style='color:green;'>" + data.cost + "</span> zł";
        let h1 = document.querySelector('h1');
        h1.innerHTML = "Ogrodzenie zostało wygenerowane!";
        let div = document.createElement('div');
        div.appendChild(h3);
        document.querySelector('.page').appendChild(div);
        document.getElementById('generateFence').remove();
      })
}


function neighbors(){
    let windowPopup, overlay;
    ({ windowPopup, overlay } = createPopup("Lista sąsiadów"));
    windowPopup.style.zIndex = 1001;
    windowPopup.style.width = '100%'; 
    windowPopup.style.maxWidth = '50%';
    windowPopup.style.display = 'flex'; 
    windowPopup.style.justifyContent = 'center'; 
    windowPopup.style.alignItems = 'center'; 

    let table = document.getElementById('neighborsTable').cloneNode(true);

    table.style.display = 'table';

    windowPopup.appendChild(table);
    document.body.appendChild(overlay);

    document.body.appendChild(windowPopup);

    overlay.addEventListener('click', function() {
        document.body.removeChild(windowPopup);
        document.body.removeChild(overlay);
    });
}