import http.client


def get_current_weather(location: int) -> str:
  conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

  headers = {
      'X-RapidAPI-Key': "c9918a8ceamsh71bb6a68f0c1a2cp1fbbcbjsnda7ba6738dea",
      'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
  }

  conn.request("GET", f"/current.json?q={location}", headers=headers)

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

def get_astronomy(location: int) -> str:
  conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

  headers = {
      'X-RapidAPI-Key': "c9918a8ceamsh71bb6a68f0c1a2cp1fbbcbjsnda7ba6738dea",
      'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
  }

  conn.request("GET", f"/astronomy.json?q={location}", headers=headers)

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

def main():
  location = input("Enter Zip Code: ")
  print("Current Weather:")
  get_current_weather(location)
  print("\nCurrent Astronomy:")
  get_astronomy(location)

if __name__ == "__main__":
  main()