import requests

response = requests.api.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(response.content)

#def main():
   # print("Hello from hello-cs188!")


#if __name__ == "__main__":
  #  main()
