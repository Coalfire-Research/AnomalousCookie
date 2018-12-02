# AnomalousCookie.py
+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+<BR>
|A|n|o|m|a|l|o|u|s| |C|o|o|k|i|e| - v1.0<BR>
+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+<BR>
Auto fuzz cookies to detect weaknesses (leading to additional vulnerabilities) and create screenshots.
<BR><BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALL/PRE-REQS:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
1. Install python:<BR>
apt-get install python

2. Install pip!<BR>
apt-get install python-pip
pip install --upgrade pip

3. Install needed Python libs:<BR>
pip install selenium<BR>

4. Install Geckodriver!<BR>
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz<BR>

- tar zxvf geckodriver-v0.18.0-linux64.tar.gz<BR>
- chmod 655 geckodriver<BR>
- cp geckodriver /usr/bin/geckodriver<BR>

<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALLING:<br>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>

GIT CLONE the 'AnomalousCookie' script/framework:<BR>
git clone https://github.com/LostRabbitLabs/AnomalousCookie<BR>

<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
HOW TO USE:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>

Usage:<BR>
./AnomalousCookie-v1.py -h  // HELP!!<BR>
./AnomalousCookie-v1.py -1 "https://www.example.com" output // Append fuzz data before existing cookie payload data.<BR>
./AnomalousCookie-v1.py -2 "https://www.example.com" output // Overwrite existing cookie payload data.<BR>
./AnomalousCookie-v1.py -3 "https://www.example.com" output // Append fuzz data after existing cookie payload data.<BR>

<BR>
Enable proxy by modifying the setting below:<BR>
proxy = "yes"<BR><BR>
Screenshots will be saved in the 'output' directory. Enjoy!<BR><BR>

-theLostRabbit
<BR><BR>

