google.charts.load("current", {packages: ["timeline"]});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    var container = document.getElementById('timelines');
    var chart = new google.visualization.Timeline(container);
    var dataTable = new google.visualization.DataTable();

    dataTable.addColumn({type: 'string', id: 'Name'});
    dataTable.addColumn({type: 'date', id: 'Start'});
    dataTable.addColumn({type: 'date', id: 'End'});
    dataTable.addColumn({type: 'string', role: 'tooltip', id: 'link', 'p': {'html': true}});
    dataTable.addRows([
        ['Данилова Елизавета Ильинична', new Date(2023, 3, 25), new Date(2023, 4, 10), 'test'],
        ['Данилова Елизавета Ильинична', new Date(2023, 8, 1), new Date(2023, 8, 14), 'test'],
        ['Ефремов Глеб Максимович', new Date(2023, 6, 1), new Date(2023, 6, 14), 'test'],
        ['Ефремов Глеб Максимович', new Date(2023, 10, 15), new Date(2023, 10, 30), 'test'],
        ['Кузнецов Александр Викторович', new Date(2023, 2, 1), new Date(2023, 2, 7), 'test'],
        ['Кузнецов Александр Викторович', new Date(2023, 8, 10), new Date(2023, 8, 17), 'test'],
        ['Кузнецов Александр Викторович', new Date(2023, 5, 10), new Date(2023, 5, 24), 'test'],
        ['Смирнова Анастасия Владимировна', new Date(2023, 6, 1), new Date(2023, 6, 14), 'test'],
        ['Смирнова Анастасия Владимировна', new Date(2023, 10, 15), new Date(2023, 10, 30), 'test'],
    ]);
    // set a padding value to cover the height of title and axis values
    var paddingHeight = 40;
// set the height to be covered by the rows
    var rowHeight = dataTable.getNumberOfRows() * 50;
// set the total chart height
    var chartHeight = rowHeight + paddingHeight;

    var options = {
        allowHtml: true,
        height: chartHeight,
        hAxis: {
            minValue: new Date(2023, 0, 1),
            maxValue: new Date(2024, 0, 1),
        },
        tooltip: {
            isHtml: true,
            trigger: 'selection'
        },

    };

    function modalWindow() {
        var selection = chart.getSelection();
        if (selection.length > 0) {

            var start_vacation_date = dataTable.getValue(selection[0].row, 1);

            var start_day = start_vacation_date.getDate(),
                start_month = Number(start_vacation_date.getMonth() + 1),
                start_year = start_vacation_date.getFullYear();

            start_month = (start_month < 10 ? "0" : "") + start_month;
            start_day = (start_day < 10 ? "0" : "") + start_day;
            var start_to_calendar = start_year + "-" + start_month + "-" + start_day;

            var end_vacation_date = dataTable.getValue(selection[0].row, 2);

            var end_day = end_vacation_date.getDate(),
                end_month = Number(end_vacation_date.getMonth() + 1),
                end_year = end_vacation_date.getFullYear();

            end_month = (end_month < 10 ? "0" : "") + end_month;
            end_day = (end_day < 10 ? "0" : "") + end_day;
            var end_to_calendar = end_year + "-" + end_month + "-" + end_day;


        }
    }


    function drawTimelineChart() {
        chart.draw(dataTable, options);

    }

    drawTimelineChart();


}