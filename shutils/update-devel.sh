cp database.db ..
cp config.yaml ..
cd ..
rm -rf twitterbot2
git clone --single-branch -branch devel https://github.com/edoardottt/twitterbot2
cd twitterbot2
cp ../database.db .
cp ../config.yaml .