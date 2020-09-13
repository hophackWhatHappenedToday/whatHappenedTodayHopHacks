anychart.onDocumentReady(function () {
    var data = [
    {x: "COVID-19", value: 80},
    {x: "Coronavirus", value: 56},
    {x: "Brexit", value: 44},
    {x: "Premier League ", value: 40},
    {x: "Stevie Lee", value: 36},
];
	// create a chart and set the data
    var chart = anychart.tagCloud(data);

    // set the chart title
    chart.title("Word Cloud: What Happened?");

    // set the container id
    chart.container("container");

    // initiate drawing the chart
    chart.draw();

    chart.listen("pointClick", function(e){
        var url = "https://news.google.com/search?q=" + e.point.get("x");
        window.open(url, "_blank");
    });

    // create and configure a color scale.
    var customColorScale = anychart.scales.linearColor();;
    customColorScale.colors(["#7bd5f5", "#5e72eb", "#120c6e"]);

    // set the color scale as the color scale of the chart
    chart.colorScale(customColorScale);

    // add a color range
    chart.colorRange().enabled(true);

    chart.normal().fontFamily("Verdana");
});


/*
anychart.onDocumentReady(function () {
    // To work with the data adapter you need to reference the data adapter script file from AnyChart CDN
    // https://cdn.anychart.com/releases/8.7.1/js/anychart-data-adapter.min.js
    anychart.data.loadCsvFile("https://cdn.anychart.com/charts-data/data_csv.csv", function (data) {

    // create chart from loaded data
    var chart = anychart.bar(data);
    // set title
    chart.title("AnyChart from CSV File");
    // draw chart
    chart.container("container").draw();
 });
});
*/