function $(elementId)
{
    return document.getElementById(elementId);
}

function $value(elementId)
{
    return $(elementId).value;
}

function addElementEvent(elementId, event, func)
{
    $(elementId).addEventListener(event, func);
}

function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function insertRowText(tbodyID, rowIndex, ...cells)
{
    var cellIndex = 0;
    var tableRef = $(tbodyID);
    if(rowIndex) //If rowIndex is valid
    {
        var newRow = tableRef.insertRow(rowIndex);
    }else{
        var newRow = tableRef.insertRow();
    }

    //Specific Functionality
    newRow.addEventListener("dblclick", function(){
        openEditWindow(this);
    });   

    for(i=0;i<cells.length;i++)
    {
        cellValue = cells[i];
        addRowText(newRow, cellValue, cellIndex);
        cellIndex++;
    }
}

function addRowText(newRow, cellValue, cellIndex)
{  
    var newCell = newRow.insertCell(cellIndex);
    var newText = document.createTextNode(cellValue);
    newCell.appendChild(newText);
}

function validateRequest(request){
    if(request.readyState == 4)
    {
        return request.status;
    }else{
        return 0;
    }
}

function showSpinner()
{
    $("loader").hidden = false;
    $("mainBody").classList.add("disabled");
}

function hideSpinner()
{
    $("loader").hidden = true;
    $("mainBody").classList.remove("disabled");
}

//Application

window.addEventListener("load", onLoad);
var httpRequest = new XMLHttpRequest();
var albumList;

function onLoad()
{
    addElementEvent("btnSearch", "click", searchArtist);
}

function searchArtist()
{
    artistName = $value("txtArtist");
    httpRequest.onreadystatechange = searchResponse;
    httpRequest.open("GET", "http://localhost:8000/api/v1/albums?artist=" + artistName);
    httpRequest.send();
}

function searchResponse()
{
    if(httpRequest.readyState == 4)
    {
        if(httpRequest.status == 200)
        {
            albumList = httpRequest.responseText;
            parseAndShowAlbums();
            hideSpinner();
        }else{
            if(httpRequest.status == 404)
            {
                alert("Error: Artist not found.")
            }else{
                alert("Error obtaining artist.");
            }            
            hideSpinner();
        }
    }else{
        showSpinner();
    }
}

function parseAndShowAlbums()
{
    clearCards();    
    albumJson = JSON.parse(albumList);
    for(var i=0;i<albumJson.Discography.length;i++){
        generateCard(albumJson.Discography[i].name, albumJson.Discography[i].released, albumJson.Discography[i].cover.url)
    }
}

function clearCards()
{
    $("albums").innerHTML = "";
}

function generateCard(artistName, releaseDate, imageUrl){
    cardGroup = document.createElement("div");
    cardGroup.className = "card-group";

    newCard = document.createElement("div");
    newCard.className = "card cardStyle";

    cardImg = document.createElement("img");
    cardImg.className = "card-img-top";
    cardImg.src = 'data:image/jpeg;base64,' + imageUrl;
    cardImg.alt = "Image not found in S3";
    newCard.appendChild(cardImg);

    cardBody = document.createElement("div");
    cardBody.className = "card-body";    

    cardTitle = document.createElement("h5");
    cardTitle.className = "card-title";
    cardTitle.innerHTML = artistName;
    cardBody.appendChild(cardTitle);

    cardText = document.createElement("p");
    cardText.className = "card-text";
    cardText.innerHTML = releaseDate;
    cardBody.appendChild(cardText);
    
    newRow = document.createElement("div");
    newRow.className = "row";

    newCard.appendChild(cardBody);
    cardGroup.appendChild(newCard);
    $("albums").appendChild(cardGroup);
    $("albums").appendChild(newRow);
}