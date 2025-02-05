import sqlite3; 

conn = sqlite3.connect('yt_video.db'); 

cursor = conn.cursor();


cursor.execute('''
CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY, 
               name TEXT NOT NULL,
               time TEXT NOT NULL
               ) 
''')

def list_videos():
  cursor.execute("""
  SELECT * FROM videos
  """)
  for row in cursor.fetchall():
    print(row)

def add_video(name , time):
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name , time))
  conn.commit()

def Update_video(id, name , time):
  cursor.execute("UPDATE videos SET name = ?, time = ?WHERE id = ?" , (name , time , id))
  conn.commit()

def delete_video(id):
  cursor.execute("DELETE FROM videos where id = ?",(id,))
  conn.commit();

def main ():
  while True:
    print("\n Youtube manger app with DB ")
    print("1. List Videos")
    print("2. Add Videos")
    print("3. Update Videos")
    print("4. Delete Videos")
    print("5. Exit App Videos")
    choice = input("Enter your working Choices : "); 

    if choice == '1':
      list_videos();
    elif choice == '2' :
      name =  input("Enter the Video name: ")
      time =input("Enter the Video time: ")
      add_video(name, time)
    elif choice == '3':
      video_id = input("Enter the Video ID: ")
      name =  input("Enter the Video name: ")
      time =input("Enter the Video time: ")
      Update_video(video_id, name, time);
    elif choice == '4':
      video_id = input("Enter the Video ID: ");
      delete_video(video_id);
    elif choice == '5':
      break
    elif choice == '4':
      video_id = input("Enter the Video ID: ");
      delete_video(video_id);
    else : 
      print("Invalid choices")
  conn.close()



if __name__ == "__main__":
  main();