import http.client


def get_current_weather(location: int) -> str:
  conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

  headers = {
      'X-RapidAPI-Key': "your_key_here",
      'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
  }

  try:
    conn.request("GET", f"/current.json?q={location}", headers=headers)
  except Exception as e:
    print(f"Error occurred during call: {e}")

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

  conn.close()

def get_astronomy(location: int) -> str:
  conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

  headers = {
      'X-RapidAPI-Key': "your_key_here",
      'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
  }

  try:
    conn.request("GET", f"/astronomy.json?q={location}", headers=headers)
  except Exception as e:
    print(f"Error occurred during call: {e}")

  res = conn.getresponse()
  data = res.read()

  print(data.decode("utf-8"))

  conn.close()

def main():
  location = input("Enter Zip Code: ")
  print("Current Weather:")
  get_current_weather(location)
  print("\nCurrent Astronomy:")
  get_astronomy(location)

if __name__ == "__main__":
  main()