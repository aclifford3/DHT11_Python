from graphqlclient import GraphQLClient
import datetime
import config

client = None


class SlushieClient:
    def __init__(self):
        self.client = GraphQLClient('https://rxmmnanjazc63nzfsn6q57nytu.appsync-api.us-east-2.amazonaws.com/graphql')
        self.client.inject_token(config.SLUSHIE_API_KEY, 'x-api-key')

    def update_weather_data(self, device_id, temperature, humidity):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')
        query = '''
        mutation updateWeatherData {{
            updateSlushieWeatherModel(input: {{deviceId: \"{device_id}\", temperature: \"{temperature}\", humidity: \"{humidity}\", datetime: \"{now}\"}}) {{
                deviceId
                temperature
                humidity
                datetime
            }}
        }}
        '''.format(device_id=device_id, temperature=temperature, humidity=humidity, datetime=now)
        print(query)
        result = self.client.execute(query)
        print(result)
        return result
