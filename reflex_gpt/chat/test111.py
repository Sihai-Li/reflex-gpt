from decouple import config

api_key = config("OPENAI_API_KEY", default=None)
print(f"Loaded API Key: {api_key}")