
var URL = "https://data.nasdaq.com/api/v3/datasets/LBMA/GOLD?start_date=2023-03-28&end_date=2023-03-28&api_key=Gn9_Btq48px28EnUeziH";
fetch(URL)
    .then(resp => resp.json())
    .then(json => {
        data = json.dataset.data[0][1];
        date = json.dataset.data[0][0];
        document.querySelector('#price').textContent = "The price of gold as of " + date +" is $"+ data+ " per Troy Ounce";
    });