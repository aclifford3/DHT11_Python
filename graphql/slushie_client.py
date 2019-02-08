from graphqlclient import GraphQLClient
import datetime

client = None


class SlushieClient:
    def __init__(self):
        self.client = GraphQLClient('https://rxmmnanjazc63nzfsn6q57nytu.appsync-api.us-east-2.amazonaws.com/graphql')
        # TODO: Environment variable, command line arg
        self.client.inject_token('', 'x-api-key')

    def update_weather_data(self, device_id, temperature, humidity, datetime):
        param = "deviceId: {device_id}, temperature: {temperature}, humidity: {humidity}, datetime: {datetime}"
        query = '''
        mutation updateWeatherData {
            updateSlushieWeatherModel(input: {}) {
                deviceId
                temperature
                humidity
                datetime
            }
        }
        '''
        print(query)
        result = self.client.execute(query)
        print(result)
        return result


client = SlushieClient()
client.update_weather_data("test", "10", "10", datetime.datetime.now())

