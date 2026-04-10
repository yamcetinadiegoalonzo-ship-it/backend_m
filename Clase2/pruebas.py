import requests
Base_URL="http://127.0.0.1:8000"

#def pet1():
 #   resp=requests.get(Base_URL+"/Pet1?edad=10")
  #  print(resp.text)

#pet1()
#def Pet2():
 #   resp=requests.get(Base_URL+"/pet_3",params={
  #      "edad":50,
   #     "estado":"Yucatán"
    #})
    #print(resp.text)
    #print(resp.json())

#Pet2()

#def Pet4():
 #   resp=requests.get(Base_URL+"/pet_4",params={
  #      "edad":500,
   #     "estado":"Yucatan",
 #       "estudiante":False
#    })
   # print(resp.text)
  #  print(resp.json())
   # print(resp.status_code)
 #   respServ=resp.status_code
 #   if respServ!=200:
 #       print("ERROR en la informacion")
  #  else:
   #     print(resp.json())

#Pet4()

# def body_1():
#     resp=requests.post(Base_URL+"/body_1",json={
#         "edad":10,
#         "nombre":"Maria"
#     })
#     print(resp.json())

# body_1()

# def body_1():
#     resp=requests.post(Base_URL+"/body_2",json={
#         "edad":10,
#         "nombre":"maria"
#     })
#     print(resp.json())

# body_1()

def body_3():
    resp=requests.post(Base_URL+"/body_3",json={
        "edad":10,
        "nombre":"maria"
    })
    print(resp.json())

body_3()
def alumno():
    resp = requests.get(Base_URL + "/alumno/2", params={
        "bienvenida": True
    })
    
    print(resp.text)
    print(resp.json())
    print(resp.status_code)

alumno()