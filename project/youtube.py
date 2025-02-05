# 1. List a favourite video
# 2. Add a Youtube video
# 3. Update a youtube video detail 
# 4. Delete a youtube video  
# 5. Exit the App
import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            content = file.read()
            if not content.strip():  # Check if file is empty
                print("File is empty. Returning an empty list.")
                return []
            videos = json.loads(content)
            return videos
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning an empty list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def save_data_helper(videos):
    try:
        with open('youtube.txt', 'w') as file:
            json.dump(videos, file)
      # this take only 2 values , kya karna hai kha karna hai 
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

def list_all_videos(videos):
    if not videos:
        print("No videos to display.")
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']} , duration : {video['time']}')

def add_videos(videos):
    try:
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos.append({'name': name, 'time': time})
        save_data_helper(videos)
    except Exception as e:
        print(f"An error occurred while adding the video: {e}")

def update_youtube_video(videos):
  #  pass
    if not videos:
        print("No videos to update.")
        return
    try:
        list_all_videos(videos)
        index = int(input("Enter the index of the video you want to update: ")) - 1
        if index < 0 or index >= len(videos):
            print("Invalid index.")
            return
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        videos[index] = {'name': name, 'time': time}
        save_data_helper(videos)
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while updating the video: {e}")

def delete_youtube_video(videos):
    
    if not videos:
        print("No videos to delete.")
        return
    try:
        list_all_videos(videos)
        index = int(input("Enter the index of the video you want to delete: ")) - 1
        if index < 0 or index >= len(videos):
            print("Invalid index.")
            return
        del videos[index]
        save_data_helper(videos)
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred while deleting the video: {e}")

def main():
    videos = load_data()

    while True:
        print('\nYouTube Manager | Choose an option:')
        print('1. List all videos')
        print('2. Add a YouTube video')
        print('3. Update a YouTube video detail')
        print('4. Delete a YouTube video')
        print('5. Exit the app')
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_youtube_video(videos)
            case '4':
                delete_youtube_video(videos)
            case '5':
                break
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    main()
