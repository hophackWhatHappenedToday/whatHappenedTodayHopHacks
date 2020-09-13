var myInit = {
    method: 'GET',
    headers:{
        'Content-Type':'application/json'
    },
    mode: 'cors',
    cache:'default'
};

let myRequest = new Request("./data.json",myInit);
var data;
fetch(myRequest)
    .then(function(resp){
        return resp.json();
    })
    .then(function(a){
        console.log(a)
        data = a;
    });


function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[key]);
      cell.appendChild(text);
    }
  }
}

let table = document.getElementById('data');
let data = Object.keys(mountains[0]);
generateTableHead(table, data);
generateTable(table, mountains);