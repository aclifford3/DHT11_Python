[![CircleCI](https://circleci.com/gh/aclifford3/slushie-weather-station-edge.svg?style=svg)](https://circleci.com/gh/aclifford3/slushie-weather-station-edge)

# Slushie Weather Station (Edge)

This repository contains code run by telemetry devices at the edge to collect weather data and publish that data to the cloud to be analyzed by consuming applications.

# Road Map

## Phase 1: Indoor temperature and humidity collection system and dashboard

Indoor temperature and humidity data will be retrieved by a Raspberry Pi connected to a DHT11 sensor.  This data will be published to DynamoDB using a GraphQL API (created by AWS AppSync).  Data will be accessible using GraphQL.  A single client-side dashboard application will display this data in the form of current temperatures and time series.

Current components
- Telemetry device, Raspberry Pi with conneted DHT11 sensor. 
- Database (DynamoDB), GraphQL API (Both created by AWS App Sync)
- Dashboarding application (Amazon S3-hosted React.js application)


## Developer Setup
1. Install any missing Python packages
2. Create config.py file with example contents:
```python
SLUSHIE_API_KEY = 'key'
DEVICE_ID = 'pi_living_room'
```

## Phase 2


# License

This project is licensed under the terms of the MIT license.
