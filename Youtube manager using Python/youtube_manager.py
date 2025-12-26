import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
        

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the video number to Update : "))
    if 1 <= index <= len(videos):
        name = input("Enter new video name:")
        time = input("Enter new video time: ")
        videos[index - 1] = {'name' : name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invlaid Inddex selected!")

def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    
    if 1<= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid Index Selected!")

def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option: ")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the application")
        user_choice = input("Enter your choice (1-5): ")
        # print(videos)

        match user_choice:
            case '1':
                list_videos(videos)
                
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)

            case '5':
                break

            case _:
                print("Invalid Choice! Please try again.")
        
if __name__ == "__main__":
    main()

