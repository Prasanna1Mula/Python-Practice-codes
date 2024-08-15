import time

def get_hashtag_datahashtag_data():
    return["#Python"]

while True:
    hashtag_data = get_hashtag_data("#python")
    analyze_data(hashtag_data)
    time.sleep(300)