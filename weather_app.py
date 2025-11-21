import asyncio
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv

load_dotenv() #laduje plik .env (tam gdzie jest klucz)


#tool do pozyskiwania informacji pogodowych:
@function_tool
def get_weather_information(city:str) -> dict:
    """Returns weather information from given location"""
    return {"city":city, "temperature": 32, "temperature unit":"C", "humidity":60}

# Tworzymy agenta:
agent = Agent(
    name="Weather App", #nazwa agenta
    instructions=(
        "You are a weather app.\n"
        "Use tools to get weather information.\n"
        "Answer in 1-2 sentence with rhymes."
    ), #system prompt
    model="gpt-5-nano", #podajemy nazwę modelu który chcemy użyć
    tools=[get_weather_information], #podajemy toole ktore chcemy zeby agent uzyl
)

# Uruchamiamy agenta:
async def main():
    result = await Runner.run(agent, "Cracow") #uruchamianie agenta z gotowym user promptem (Krakow)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main()) #robimy asyncio ze wzgledu na async i await w funkcji main
