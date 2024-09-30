#!/usr/bin/with-contenv bashio

CONFIG_PATH=/data/options.json

# Get configuration values
INTERVAL=$(bashio::config 'update_interval')
LOCATION=$(bashio::config 'location')

# Run the Python script
python3 /meteo_lt_api.py "$INTERVAL" "$LOCATION"
