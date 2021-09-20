#
# twitterbot2
#
#   edoardottt
#   edoardoottavianelli.it
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# This file is intended to update the devel branch
# on the test machine to quickly test the new 
# functionalities/fixes.
# The database.db, config.yaml and twitterbot2.log files
# will be kept. 
#

cp database.db ..
cp config.yaml ..
cp twitterbot2.log ..
cd ..
rm -rf twitterbot2
git clone --single-branch --branch devel https://github.com/edoardottt/twitterbot2
cd twitterbot2
cp ../database.db .
cp ../config.yaml .
cp ../twitterbot2.log .
