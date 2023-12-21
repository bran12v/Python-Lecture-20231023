"""
Get a dad joke, a new one preferable, every time it is requested

API - dad jokes

Google

Webpage

"""
import boto3
import requests

session = boto3.Session(profile_name="bvanek")

client = boto3.client('sns')

def get_joke():
    url = " https://www.icanhazdadjoke.com"
    response = requests.get(url, headers={"Accept": "application/json"})
    return response.json()["joke"] # This wasnt working previously but since I changed the headers, now it works

def main():
    # while True:
    #     option = input("Would you like a Dad Joke? (y or n)")
    #     if option == "y":
    #         num = input("How many?")
    #         try:
    #             for i in range(0, int(num)):
    #                 print(get_joke())
    #         except:
    #             print("That's not a number brother, try again")
    #     elif option == "n": 
    #         print("Woe, okay, I guess you hate fun or something")
    #         break
    #     else:
    #         print("Try again buddy")
    #         continue
    response = client.publish(
        TopicArn='arn:aws:sns:us-east-1:797918408294:bvanek-dadjokes',
        Message=f'{get_joke()}',
        Subject="Wonderful Daily Dad Jokes",
        # MessageAttributes={
        #     'string': {
        #         'DataType': '',
        #     }
        # },
    )
    print(response)

if __name__ == "__main__":
    main()