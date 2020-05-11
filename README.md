# PPC_Automation (v. 1.3)
Simple but very useful script to automate multiple advertising campaigns based on JSON parameters (eCPM, Country). You will receive notifications about the status of advertising campaigns to Telegram, along with important values from the affiliate network.

# How to use?
Just setup your API keys (credentials.py) and IDs of campaign to run (campaigns_id.py). 
Then set up your cron on Ubuntu Server:

*/30 * * * * /usr/bin/env python3 ../path_to_script/main.py

Then enjoy profitable campaigns! 
(All logs writen to log file, to easy check where something go wrong)


# Which network i can use?
It depends on your preferences, any that can provide JSON statistic for offers and API for manage campaigns
