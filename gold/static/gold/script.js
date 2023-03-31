
var URL = "https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD?limit=1&api_key=Gn9_Btq48px28EnUeziH";
fetch(URL)
    .then(resp => resp.json())
    .then(json => {
        data = json.dataset.data[0][1];
        date = json.dataset.data[0][0];
        document.querySelector('#price').textContent = "The price of gold as of " + date +" is $"+ data+ " per Troy Ounce";
    });

function calculate(){
    let input = document.querySelector('#numInput').value;
    let unit = document.querySelector('#unitSelection').value;
    if (Number.isNaN(Number(input)) || input<0){
        document.querySelector('#error').textContent = "Please provide a valid number!!!!";

    }
    else{
        url = "http://localhost:8000/unitconv/convert?from=" + unit + "&to=t_oz&value="+ input;
        fetch(url)
            .then(resp => resp.json())
            .then(json => {
                if (json.hasOwnProperty('error')) {
                    throw json.error;
                }
                else{
                    result = json.value * data;
                    let div = document.createElement('div');
                    div.setAttribute("class","stuff-box green");
                    div.setAttribute("id", "result");
                    div.setAttribute("type", "button");
                    div.setAttribute("onclick", "remove()");
                    document.querySelector('body').appendChild(div);
                    let now = new Date();
                    let p = document.createElement('p');
                    p.textContent = now;
                    let p1 = document.createElement('p');
                    p1.textContent = input+ " "+ unit+ " of gold is worth$" + result.toFixed(2);
                    div.appendChild(p);
                    div.appendChild(p1);
                }
            });
    }
}
function remove(){
    destroy = document.querySelector('#result');
    destroy.remove()
}