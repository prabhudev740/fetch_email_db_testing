import sqlite3
from emails import store_in_dbase, fetch_emails

email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
store_in_dbase(email_list)

class TestEmails:
    # def __init__(self) -> None:
    #     print('connected')
    
    def test_email_count(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        expected_count = len(email_list)
        c.execute('SELECT COUNT(*) FROM emails')
        actual_count = c.fetchone()[0]
        assert actual_count == expected_count
        conn.close()

    def test_email_sender(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        for i, email_dict in enumerate(email_list):
            expected_sender = email_dict['sender']
            c.execute(f'SELECT sender FROM emails WHERE rowid={i+1}')
            actual_sender = c.fetchone()[0]
            assert actual_sender == expected_sender
        conn.close()

    def test_email_receiver(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        for i, email_dict in enumerate(email_list):
            expected_receiver = email_dict['receiver']
            c.execute(f'SELECT receiver FROM emails WHERE rowid={i+1}')
            actual_receiver = c.fetchone()[0]
            assert actual_receiver == expected_receiver
        conn.close()

    def test_email_subject(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        for i, email_dict in enumerate(email_list):
            expected_subject = email_dict['subject']
            c.execute(f'SELECT subject FROM emails WHERE rowid={i+1}')
            actual_subject = c.fetchone()[0]
            assert actual_subject == expected_subject
        conn.close()

    def test_email_date(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        for i, email_dict in enumerate(email_list):
            expected_date = email_dict['date']
            c.execute(f'SELECT date FROM emails WHERE rowid={i+1}')
            actual_date = c.fetchone()[0]
            assert actual_date == expected_date
        conn.close()

    def test_email_body(self):
        conn = sqlite3.connect('emails.sql')
        c = conn.cursor()
        # c.execute('DROP TABLE IF EXISTS emails')
        email_list = fetch_emails("Prabhuprasad Panda", "01-Jan-2022")
        store_in_dbase(email_list)
        conn.commit()

        for i, email_dict in enumerate(email_list):
            expected_body = email_dict['body']
            c.execute(f'SELECT body FROM emails WHERE rowid={i+1}')
            actual_body = c.fetchone()[0]
            assert actual_body == expected_body
        conn.close()