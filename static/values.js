//
// twitterbot2
//
//   edoardottt
//   edoardoottavianelli.it
//   https://github.com/edoardottt/twitterbot2
//
//   This repository is under GPL - 3 License.
//
// This file controls the charts and all the data
// visualization on frontend.
//

const COLORS = [
    '#4dc9f6',
    '#f67019',
    '#f53794',
    '#537bc4',
    '#acc236',
    '#166a8f',
    '#00a950',
    '#58595b',
    '#8549ba'
];

function color(index) {
    return COLORS[index % COLORS.length];
}


const CHART_COLORS = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)',
    grey: 'rgb(255, 255, 255)',
    black: 'rgb(0, 0, 0)'
};

const NAMED_COLORS = [
    CHART_COLORS.red,
    CHART_COLORS.orange,
    CHART_COLORS.yellow,
    CHART_COLORS.green,
    CHART_COLORS.blue,
    CHART_COLORS.purple,
    CHART_COLORS.grey,
    CHART_COLORS.white,
    CHART_COLORS.black,
];

function namedColor(index) {
    return NAMED_COLORS[index % NAMED_COLORS.length];
}

var values = JSON.parse(document.getElementById("lineChart").dataset.values);

var dates = [];
var tweets = [];
var likes = [];
var retweets = [];
var followers = [];

for (var i = 0; i < values.length; i++) {
    var obj = values[i];
    var date = obj["1"];
    dates.push(date);
    var tweet = obj["2"];
    tweets.push(tweet);
    var like = obj["3"];
    likes.push(like);
    var retweet = obj["4"];
    retweets.push(retweet);
    var follower = obj["5"];
    followers.push(follower);
}

/*
console.log("dates: ");
console.log(dates);
console.log("tweets: ");
console.log(tweets);
console.log("likes: ");
console.log(likes);
console.log("retweets: ");
console.log(retweets);
console.log("followers: ");
console.log(followers);
*/

var ctx = document.getElementById('lineChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: dates,
        datasets: [
            {
                label: 'Tweets',
                data: tweets,
                borderColor: CHART_COLORS.red,
            },
            {
                label: 'Likes',
                data: likes,
                borderColor: CHART_COLORS.blue,
            },
            {
                label: 'Retweets',
                data: retweets,
                borderColor: CHART_COLORS.yellow,
            },
            {
                label: 'Followers',
                data: followers,
                borderColor: CHART_COLORS.green,
            }
        ]
    },
    plugins: {
        title: {
            display: true,
            text: 'Statistics over time'
        }
    },
    responsive: true,
    scaleShowVerticalLines: false,
});
