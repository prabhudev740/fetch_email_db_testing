import email
import imaplib
import sqlite3

uname = 'practice740@gmail.com'
with open('password.txt') as f:
    passwd = f.read()

def fetch_emails(email_name=None, time_duration=None):
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(uname, passwd)
    mail.select('inbox')

    if email_name and time_duration:
        _, data = mail.search(None, f'(FROM "{email_name}")', f'(SINCE "{time_duration}")')
    elif email_name:
        _, data = mail.search(None, f'(FROM "{email_name}")')
    elif time_duration:
        _, data = mail.search(None, f'(SINCE "{time_duration}")')


    emails = data[0].split()
    
    email_list = []
    for num in emails:
        _, data = mail.fetch(num, '(RFC822)')
        # print(data)
        msg = email.message_from_bytes(data[0][1])
        # print(msg['From'])
        email_dict = {
            'sender': msg['From'],
            'receiver': msg['To'],
            'subject': msg['Subject'],
            'date': msg['Date'],
            'body': msg.get_payload(),
        }
        email_list.append(email_dict)

        print(msg.get_payload())
    
    mail.close()
    mail.logout()
    
    return email_list

# fetch_emails("Prabhuprasad Panda", "01-Jan-2022")


def store_in_dbase(email_list):
    conn = sqlite3.connect('emails.sql')
    curs = conn.cursor()
    curs.execute('DROP TABLE IF EXISTS emails')
    curs.execute('''CREATE TABLE IF NOT EXISTS emails( 
                    sender CHAR, 
                    receiver CHAR, 
                    subject CHAR, 
                    date CHAR, body CHAR)
                    ''')

    for email_dict in email_list:
        curs.execute('INSERT INTO emails VALUES (?, ?, ?, ?, ?)',
                  (str(email_dict['sender']), 
                  str(email_dict['receiver']), 
                  str(email_dict['subject']), 
                  str(email_dict['date']), 
                  str(email_dict['body'])))

    conn.commit()
    conn.close()

# email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
# # email_list = fetch_emails("01-Jan-2022")
# store_in_dbase(email_list)

