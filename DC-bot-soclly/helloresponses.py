import sqlite3

def hello_database():
    conn = sqlite3.connect('hello-responses.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS greetings_table (
                        id INTEGER PRIMARY KEY,
                        response_text TEXT
                    )''')

    additional_responses = [
        "Hi there! What's up?",
        "Hello!",
        "Hi! Nice to see you.",
        "Hello😊!",
        "Hi!👋",
        "Hello!👋",
        "Hi there! How's your day?",
        "Hello! What's going on?",
        "Hi! How are you doing?",
        "Hello! Need any assistance?",
        "Hi there! Good to meet you.",
        "Hey brother! what's up?",
        "Hi! How's everything going?",
        "Hello! What can I do for you?",
        "Hi! Nice to have you here.💜"
    ]

    for response in additional_responses:
        cursor.execute("INSERT INTO greetings_table (response_text) VALUES (?)", (response, ))

    conn.commit()
    conn.close()