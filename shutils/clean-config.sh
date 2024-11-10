#
# twitterbot2
#
#   edoardottt
#   edoardottt.com
#   https://github.com/edoardottt/twitterbot2
#
#   This repository is under GPL-3 License.
#
# When you execute this file the config.yaml 
# will be overwritten with the default content
# to prevent to commit and push secrets.
#

rm config.yaml
touch config.yaml
echo -n "api_key:
api_secret_key:
bearer_token:
access_token:
access_token_secret:" > config.yaml