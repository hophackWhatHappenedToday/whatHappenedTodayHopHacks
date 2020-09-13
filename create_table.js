var myArray = [
        {x: "Premier League ", value: 40},
	    {x: "COVID-19", value: 80},
	    {x: "Stevie Lee", value: 36},
        {x: "Coronavirus", value: 56},
        {x: "Brexit", value: 44},
	]

    //Implement a method to get myArray from Python
	buildTable(myArray)

	function buildTable(data){
		var table = document.getElementById('myTable')
		for (var i = 0; i < data.length; i++){
			var row = `<tr>
							<td>${data[i].x}</td>
							<td>${data[i].value}</td>
					  </tr>`
			table.innerHTML += row

		}
	}