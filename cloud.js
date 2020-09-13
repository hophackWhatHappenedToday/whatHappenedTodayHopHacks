var data = [
    {x: "Premier League ", value: 40, date: 100, sentiment: 50},
    {x: "COVID-19", value: 80, date: 100, sentiment: 50},
    {x: "Coronavirus", value: 56, date: 100, sentiment: 50},
    {x: "Brexit", value: 44, date: 100, sentiment: 50},
    {x: "Stevie Lee", value: 36, date: 100, sentiment: 50},
];

var chart = anychart.tagCloud(data);
chart.title("Word Cloud: What Happened?");
chart.container("container");
chart.draw();
chart.listen("pointClick", function(e){
    var url = "https://news.google.com/search?q=" + e.point.get("x");
    window.open(url, "_blank");
});
var customColorScale = anychart.scales.linearColor();;
customColorScale.colors(["#7bd5f5", "#5e72eb", "#120c6e"]);
chart.colorScale(customColorScale);
chart.colorRange().enabled(true);
chart.normal().fontFamily("Verdana");

//Random Changes

