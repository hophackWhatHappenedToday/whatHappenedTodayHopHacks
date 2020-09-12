anychart.onDocumentReady(function () {

    // create data
    var data = [
        {x: "COVID-19", value: 80, category: "Medicine"},
        {x: "Coronavirus", value: 56, category: "Medicine"},
        {x: "Brexit", value: 44, category: "Politics"},
        {x: "Premier League ", value: 40, category: "Sports"},
        {x: "Stevie Lee", value: 36, category: "People"},
    ];

    // create a chart and set the data
    var chart = anychart.tagCloud(data);

    // set the chart title
    chart.title("Tag Cloud Chart: Basic Sample");

    // set the container id
    chart.container("container");

    // initiate drawing the chart
    chart.draw();

    chart.listen("pointClick", function(e){
        var url = "http://www.google.com/search?q=" + e.point.get("x");
        window.open(url, "_blank");
    });

    // create and configure a color scale.
var customColorScale = anychart.scales.ordinalColor();
customColorScale.colors(["#68b0ab", "#8fc0a9", "#c8d5b9", "#Faf3dd"]);

// set the color scale as the color scale of the chart
chart.colorScale(customColorScale);

// add a color range
chart.colorRange().enabled(true);
});