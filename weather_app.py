from agents import Agent, Runner
from dotenv import load_dotenv

load_dotenv() #laduje plik .env (tam gdzie jest klucz)

# Tworzymy agenta:
agent = Agent(
    name="Weather App", #nazwa agenta
    instructions="You are a weather app", #system prompt
    model="gpt-5-nano", #podajemy nazwę modelu który chcemy użyć
)

# Uruchamiamy agenta:
def main():
    Runner.run(agent, "Kraków") #uruchamianie agenta z gotowym user promptem (Krakow)



if __name__ == "__main__":
    main()