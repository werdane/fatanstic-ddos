sudo apt update
sudo apt install tor
sudo apt install python3
sudo apt install python3-pip

pip3 install -r requirements.txt
chmod +x newports.sh
sudo ./newports.sh
echo "Setup finished; run the script: python3 main.py <url>"
