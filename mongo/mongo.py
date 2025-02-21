from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017'); 
# not a good idea to include id and password in this 

db = client['youtube']
video_collection = db['videos']; 

# print('jhcbkxzjn' ,video_collection);


def list_videos ():
  for video in video_collection.find({}):
    print(f"id : {video['_id']} , Name : {video['name']} and time : {video['time']} ")

def Add_videos (name, time):
  video_collection.insert_one({"name" : name,"time" : time}); 

def update_videos ( video_id, name , time):
  video_collection.update_one({'_id': video_id}
                              , {"$set" : {"name" : name, "time" : time}})
def delete_videos (id):
  video_collection.delete_one({"_id" : id})


def main():
  while True: 
    print('\n Youtube Manger App '); 
    print('1. List All videos '); 
    print('2. Add  videos '); 
    print('3. Update videos '); 
    print('4. Delete  videos '); 
    print('5. Exit App '); 
    choice = input('Enter your Choice : '); 

    if choice == '1':
      list_videos(); 
    elif choice == '2':
      name = input('Enter name of videos : ');
      time = input ('Enter the time of video : ')
      Add_videos(name , time); 
    elif choice == '3':
      video_id = input('Enter id of videos : ');
      name = input('Enter name of videos : ');
      time = input ('Enter the time of video : ');
      update_videos( video_id, name , time); 

    elif choice == '4':
      id = input('Enter id of videos : ');
      delete_videos(id)
    elif choice == '5':
      break; 
    else :
      print('In valid Choices');


if __name__ == "__main__":
  main();
