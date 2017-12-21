import requests
import click

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

@click.command()
@click.argument('location')
@click.option('--api_key','-a')
def main(location, api_key):
    weather = current_weather(location, api_key)
    print(f'The weather in {location} right now: {weather}.')

if __name__ == '__main__':
    main()

# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == '__main__':
#     hello()

# parser = argparse.ArgumentParser(description="Process some integers")
# parser.add_argument('integers', metavar='N', type=int, narg='+', help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default:find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))