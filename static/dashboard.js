//
// twitterbot2
//
//   edoardottt
//   edoardoottavianelli.it
//   https://github.com/edoardottt/twitterbot2
//
//   This repository is under GPL-3 License.
//
// This file refresh the website every 60 seconds.
//

function updateValues() {
    location.reload(true);
}
// every 60 seconds
setInterval(updateValues, 60000);
