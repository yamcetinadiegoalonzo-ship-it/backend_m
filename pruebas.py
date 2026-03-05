import requests

url = "https://tarea-0-py0u.onrender.com/tarea-0"

response = requests.get(url)

print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
