import requests

def fetch_Random_Quote_Api ():
  url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
  response = requests.get(url)
  data = response.json(); 
  # print(f"data of api {data}");
  if data["success"] and 'data' in data :
    user_data = data["data"]
    author = user_data["author"]
    qoute = user_data["content"]
    try:
      print(f"Author {author} \n Qoute {qoute}"); 
    except Exception as e:
      print(str(e))

  else :
    raise Exception ("Failed to fetch data ")

# fetch_Random_Quote_Api();

def fetch_jokes_api ():
  url = 'https://api.freeapi.app/api/v1/public/randomjokes'
  response = requests.get(url); 
  result = response.json(); 
  #print(result);
  if( result['statusCode'] ==  200):
    jokes =  result['data']['data']

    for joke in jokes :
      print(f'{joke['id']}, {joke['content']}'); 
  else : 
    print("failed to fetch jokes..."); 

# fetch_jokes_api();

def fetch_book_api ():
  url = "https://api.freeapi.app/api/v1/public/books";
  response = requests.get(url); 
  result = response.json();

  if(result['statusCode'] == 200) : 
    books = result['data']['data'];
    # print("books", books)
    for book in books :
      title = book['volumeInfo'].get('title', 'No title available')
      authors = book['volumeInfo'].get('authors', ['No author available'])
      author_names = ', '.join(authors)

    print(f"Book no {book['id']} \nTitle: {title} \nAuthor(s): {author_names}")
  else: 
    print("No Data fetch or problem in fetching!")


  
fetch_book_api();