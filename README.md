# Slushie Weather Station (Edge)

This repository contains code run by telemetry devices at the edge to collect weather data and publish that data to the cloud to be analyzed by consuming applications.

# Road Map

## Phase 1: Indoor temperature and humidity collection system and dashboard

Indoor temperature and humidity data will be retrieved by a Raspberry Pi connected to a DHT11 sensor.  This data will be published to a cloud streaming service such as Amazon Kinesis.  Data will be accessible in a RESTful manner by fronting the streams with an API gateway.  A single client-side dashboard application will display this data in the form of current temperatures and time series.

Current components
- Telemetry device, Raspberry Pi with conneted DHT11 sensor. 
- Data stream (Amazon Kinesis)
- API gateway (Amazon API Gateway)
- Dashboarding application (Amazon S3-hosted React.js application)



# License

This project is licensed under the terms of the MIT license.
