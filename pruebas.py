import requests

url = "https://backend-m-1.onrender.com/tarea-0"

response = requests.get(url)

print("Código de estado:", response.status_code)

if response.status_code == 200:
    print("Respuesta:", response.json())
else:
    print("Error:", response.text)