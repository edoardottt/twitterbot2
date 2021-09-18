var values = JSON.parse(document.getElementById("myChart").dataset.values);

var dates = values.slice(0, n);
var tweets = values.slice(1, n);
var likes = values.slice(2, n);
var retweets = values.slice(3, n);
var followers = values.slice(4, n);

// NOT WORKING

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
        datasets: [
            {
                label: 'Tweets',
                data: tweets,
                borderColor: Utils.CHART_COLORS.red,
                backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
                yAxisID: 'y',
            },
            {
                label: 'Likes',
                data: likes,
                borderColor: Utils.CHART_COLORS.blue,
                backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
                yAxisID: 'y1',
            },
            {
                label: 'Retweets',
                data: retweets,
                borderColor: Utils.CHART_COLORS.yellow,
                backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
                yAxisID: 'y',
            },
            {
                label: 'Followers',
                data: followers,
                borderColor: Utils.CHART_COLORS.green,
                backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
                yAxisID: 'y1',
            }
        ]
    },
    plugins: {
        title: {
            display: true,
            text: 'Statistics over time'
        }
    },
    scales: {
        y: {
            type: 'linear',
            display: true,
            position: 'left',
        },
        y1: {
            type: 'linear',
            display: true,
            position: 'right',

            // grid line settings
            grid: {
                drawOnChartArea: false, // only want the grid lines for one axis to show up
            },
        },
    }
});