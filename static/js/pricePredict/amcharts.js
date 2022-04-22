am5.ready(function () {

    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");


    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([
        am5themes_Animated.new(root)
    ]);

    root.dateFormatter.setAll({
        dateFormat: "yyyy",
        dateFields: ["valueX"]
    });

    let data = price_data;
    let dt_len = data.length;

    let data2 = [
        data[dt_len - 1],
        {
            "date": next_date,
            "value": next_price,
            "bullet": true
        }]
    console.log(data2)

    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(am5xy.XYChart.new(root, {
        focusable: true,
        panX: true,
        panY: true,
        wheelX: "panX",
        wheelY: "zoomX",
        pinchZoomX: true,
        height: 450,
        padding: 20,
    }));

    var easing = am5.ease.linear;

    // Create axes
    // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var xAxis = chart.xAxes.push(am5xy.DateAxis.new(root, {
        maxDeviation: 0.1,
        groupData: false,
        baseInterval: {
            timeUnit: "day",
            count: 1
        },
        renderer: am5xy.AxisRendererX.new(root, {

        }),
        tooltip: am5.Tooltip.new(root, {})
    }));

    var yAxis = chart.yAxes.push(am5xy.ValueAxis.new(root, {
        maxDeviation: 0.2,
        renderer: am5xy.AxisRendererY.new(root, {})
    }));


    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    var series1 = chart.series.push(am5xy.LineSeries.new(root, {
        minBulletDistance: 10,
        xAxis: xAxis,
        yAxis: yAxis,
        valueYField: "value",
        valueXField: "date",
        tooltip: am5.Tooltip.new(root, {
            pointerOrientation: "horizontal",
            labelText: "{valueY}"
        })
    }));

    series1.fills.template.setAll({
        fillOpacity: 0.2,
        visible: true
    });

    series1.strokes.template.setAll({
        strokeWidth: 2
    });


    // Set up data processor to parse string dates
    // https://www.amcharts.com/docs/v5/concepts/data/#Pre_processing_data
    series1.data.processor = am5.DataProcessor.new(root, {
        dateFormat: "yyyy-MM-dd",
        dateFields: ["date"]
    });

    //series2
    var series2 = chart.series.push(am5xy.LineSeries.new(root, {
        xAxis: xAxis,
        yAxis: yAxis,
        stroke: root.interfaceColors.get("negative"),
        fill: root.interfaceColors.get("negative"),
        valueYField: "value",
        valueXField: "date",
        tooltip: am5.Tooltip.new(root, {
            pointerOrientation: "horizontal",
            labelText: "{valueY}"
        })
    }));

    series2.fills.template.setAll({
        fillOpacity: 0.2,
        visible: true
    });

    series2.strokes.template.setAll({
        strokeWidth: 2
    });


    // Set up data processor to parse string dates
    // https://www.amcharts.com/docs/v5/concepts/data/#Pre_processing_data
    series2.data.processor = am5.DataProcessor.new(root, {
        dateFormat: "yyyy-MM-dd",
        dateFields: ["date"]
    });

    //setAll


    // series1.bullets.push(function () {
    //     var circle = am5.Circle.new(root, {
    //         radius: 4,
    //         fill: root.interfaceColors.get("background"),
    //         stroke: series1.get("fill"),
    //         strokeWidth: 2
    //     })

    //     return am5.Bullet.new(root, {
    //         sprite: circle
    //     })
    // });

    // series2.bullets.push(function () {
    //     var circle = am5.Circle.new(root, {
    //         radius: 4,
    //         fill: root.interfaceColors.get("background"),
    //         stroke: series2.get("fill"),
    //         strokeWidth: 2
    //     })

    //     return am5.Bullet.new(root, {
    //         sprite: circle
    //     })
    // });

    series2.bullets.push(function (root, series1, dataItem) {
        if (dataItem.dataContext.bullet) {
            var container = am5.Container.new(root, {});
            var circle0 = container.children.push(am5.Circle.new(root, {
                radius: 5,
                fill: am5.color(0xff0000)
            }));
            var circle1 = container.children.push(am5.Circle.new(root, {
                radius: 5,
                fill: am5.color(0xff0000)
            }));

            circle1.animate({
                key: "radius",
                to: 20,
                duration: 1000,
                easing: am5.ease.out(am5.ease.cubic),
                loops: Infinity
            });
            circle1.animate({
                key: "opacity",
                to: 0,
                from: 1,
                duration: 1000,
                easing: am5.ease.out(am5.ease.cubic),
                loops: Infinity
            });

            return am5.Bullet.new(root, {
                sprite: container
            })
        }
    })

    series1.data.setAll(data);
    series2.data.setAll(data2);

    var legend = chart.children.push(am5.Legend.new(root, {
        nameField: "name",
        fillField: "color",
        strokeField: "color",
        y: am5.percent(105),
        x: am5.percent(40),
    }));

    legend.data.setAll([{
        name: "정가",
        color: root.interfaceColors.get("primaryButton"),
    }, {
        name: "예측가",
        color: root.interfaceColors.get("negative"),
    }]);

    // Add cursor
    // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
        xAxis: xAxis,
        behavior: "none"
    }));
    cursor.lineY.set("visible", false);

    // add scrollbar
    chart.set("scrollbarX", am5.Scrollbar.new(root, {
        orientation: "horizontal"
    }));


    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    chart.appear(1000, 100);

}); // end am5.ready()