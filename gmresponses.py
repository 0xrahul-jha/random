import sqlite3


def gm_database():
  conn = sqlite3.connect('gm-responses.db')
  cursor = conn.cursor()

  cursor.execute('''CREATE TABLE IF NOT EXISTS responses_table (
                        id INTEGER PRIMARY KEY,
                        response_text TEXT
                      )''')

  additional_responses = [
   

     "Morning! ☀️"
    , "GM! 🌼"
    , "Good morning! 🌅"
    , "Rise! 🌤️"
    , "Up! ☕"
    , "Hey! 🌞"
    , "Hello! 🌅"
    ,"New day! 🌈"
    , "Greetings! 🌞"
    , "Good morning vibes! 🌺"
      
  ]

  for response in additional_responses:
    cursor.execute("INSERT INTO responses_table (response_text) VALUES (?)",
                   (response, ))

  conn.commit()
  conn.close()
    
