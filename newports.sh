#!/bin/bash

# Path to the torrc file
TORRC_PATH="/etc/tor/torrc"
echo "CookieAuthentication 1"
echo "ControlPort 9051"

# Number of additional SOCKS ports to add
NUM_PORTS=5

# Start port number for SOCKS (ensure these ports are not already in use)
START_PORT=9052

# Check if the script is being run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# Backup the current torrc file
cp "$TORRC_PATH" "$TORRC_PATH.bak"

# Add additional SOCKS ports to torrc
for ((i=0; i<NUM_PORTS; i++)); do
    PORT=$((START_PORT + i))
    echo "Adding SOCKS port $PORT to $TORRC_PATH"
    echo "SocksPort $PORT" >> "$TORRC_PATH"
done

# Restart the Tor service to apply changes
systemctl restart tor

echo "Added $NUM_PORTS SOCKS ports starting from $START_PORT to $TORRC_PATH"
