anychart.onDocumentReady(function () {

    // create data


    // create a chart and set the data
    var chart = anychart.tagCloud(rawData);

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