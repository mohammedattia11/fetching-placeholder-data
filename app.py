import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    return data

def print_message():
    data = fetch_data()
    print(f"Title: {data['title']}\nBody: {data['body']}")

if __name__ == "__main__":
    print("Fetching data from API...")
    print_message()