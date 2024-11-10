#
# twitterbot2
#
#   edoardottt
#   edoardottt.com
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

if [ -f database.db ]
then 
    cp database.db ..
fi 

if [ -f config.yaml ]
then 
    cp config.yaml ..
fi 

if [ -f twitterbot2.log ]
then 
    cp twitterbot2.log ..
fi 

cd ..
rm -rf twitterbot2
git clone --single-branch --branch devel https://github.com/edoardottt/twitterbot2
cd twitterbot2

if [ -f ../database.db ]
then 
    cp ../database.db .
fi 

if [ -f ../config.yaml ]
then 
    cp ../config.yaml .
fi 

if [ -f ../twitterbot2.log ]
then 
    cp ../twitterbot2.log .
fi 
