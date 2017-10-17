from pyBook.models import Book, User
import pyBook.utils.secrets as secrets

crypt_syn = "In 1942, Lawrence Pritchard Waterhouse, a young United States Navy code breaker and " \
            "mathematical genius, is assigned to the newly formed joint British and American Detachment " \
            "2702. This ultra-secret unit's role is to hide the fact that Allied intelligence has cracked " \
            "the German Enigma code."

crypt = Book('Cryptonomicon', '0380973464', '9780380973460', 'Neal', 'Stephenson', 5, 0, crypt_syn,
             'crypt0380973464.jpg', 'cryptonomicon')

stone_syn = "The most evil and powerful dark wizard in history, Lord Voldemort, murders James and Lily " \
            "Potter but mysteriously disappears after failing to kill their infant son, Harry. While the " \
            "wizarding world celebrates Voldemort's apparent downfall, Professor Dumbledore, Professor " \
            "McGonagall and half-giant Rubeus Hagrid place the one-year-old orphan in the care of his surly " \
            "and cold Muggle uncle and aunt, Vernon and Petunia Dursley and their spoilt and bullying " \
            "son, Dudley."

stone = Book('Harry Potter and the Philosopher\'s Stone', '0747532699', '9780747532699', 'J.K.', 'Rowling',
             4, 0, stone_syn, 'harry0747532699.jpg', 'harry')

chamber_syn = "In 1992, while the Dursley family—his uncle Vernon, aunt Petunia, and cousin Dudley—entertain " \
              "a potential client for Vernon’s drill-manufacturing company Grunnings, Harry Potter " \
              "reminisces upon the events of the previous year, including his enrolment in Hogwarts School " \
              "of Witchcraft and Wizardry and confrontation with Lord Voldemort (the Dark wizard whose reign " \
              "seemingly ended when he killed Harry’s parents and attempted but failed to kill Harry " \
              "himself), and laments the fact that the best friends he made at the institution have not " \
              "written to him, even for his birthday, on which the novel opens."

chamber = Book('Harry Potter and the Chamber of Secrets', '0747538492', '9780747538493', 'J.K.', 'Rowling',
               4, 0, chamber_syn, 'harry0747538492.jpg', 'harry')

quick_syn = "The first book is a series of flashbacks from 1713 to the earlier life of Daniel Waterhouse. " \
            "It begins as Enoch Root arrives in Boston in October 1713 to deliver a letter to Daniel " \
            "containing a summons from Princess Caroline. She wants Daniel to return to England and attempt " \
            "to repair the feud between Isaac Newton and Gottfried Leibniz. While following Daniel's decision " \
            "to return to England and board a Dutch ship (the Minerva) to cross the Atlantic, the book flashes" \
            " back to when Enoch and Daniel each first met Newton. During the flashbacks, the book refocuses " \
            "on Daniel's life between 1661 and 1673."

quick = Book('Quicksilver', '0380977427', '9780380977420', 'Neal', 'Stephenson', 4.5, 0, quick_syn,
             'quick0380977427.jpg', 'quicksilver')

ream_syn = "Reamde begins by introducing two members of the Forthrast family who reconnect at an annual " \
           "family reunion: Richard \"Dodge\" Forthrast, a middle-aged man who is the second of the three " \
           "Forthrast sons (John, Richard, and Jake), and Zula Forthrast, John's adopted Eritrean daughter, " \
           "Richard's niece."

ream = Book('Reamde', '0061977969', '9780061977961', 'Neal', 'Stephenson', 4.5, 0, ream_syn,
            'reamd0061977969.jpg', 'reamde')

conf_syn = "The beginning of The Confusion finds Jack Shaftoe awakened from a syphilitic blackout of nearly " \
           "three years. During this time he was a pirate galley slave. The other members of his bench, a" \
           " motley crew who call themselves \"The Cabal\" and who include men from Africa, the Far East and " \
           "Europe, create a plot to capture silver illegally shipped from Central America by a Spanish " \
           "Viceroy; they convince the Pasha of Algiers and their owner to sponsor this endeavor and " \
           "negotiate for their freedom and a cut in the profit."

conf = Book('The Confusion', '0060523867', '9780060523862', 'Neal', 'Stephenson', 4.5, 0, conf_syn,
            'confu0060523867.jpg', 'confusion')

strange_syn = "Meursault learns of his mother's death. At her funeral, he expresses none of the expected " \
              "emotions of grief.[4] When asked if he wishes to view the body, he says no, and, instead, " \
              "smokes and drinks coffee in front of the coffin. Rather than expressing his feelings, he " \
              "comments to the reader only about the attendees at the funeral."

strange = Book('The Stranger', '0679420266', '9780679420262', 'Albert', 'Camus', 0, 0, strange_syn,
               'stran0679420266.jpg', 'stranger')

color_syn = "The story begins in Ankh-Morpork, the biggest city on the Discworld. The main character is an " \
            "incompetent and cynical wizard named Rincewind, who is hired as a guide to the rich but naive " \
            "Twoflower, an insurance clerk from the Agatean Empire who has come to visit Ankh-Morpork. "

color = Book('The Colour of Magic', '0062225677', '9780062225672', 'Terry', 'Pratechett', 0, 0, color_syn,
             'color0062225677.jpg', 'colour')

system_syn = "Daniel Waterhouse returns to England from his \"Technologickal College\" project in Boston " \
             "in order to try to resolve the feud between Isaac Newton and Gottfried Leibniz over who " \
             "invented calculus. Someone attempts to assassinate him with an \"Infernal Device\" (a bomb), " \
             "and Waterhouse forms a club to find out who did it and prosecute them. It later turns out that" \
             " the bomb was intended for his friend Isaac Newton."

system = Book('The System of the World', '0060523875', '9780060523879', 'Neal', 'Stephenson', 4.5, 0,
              system_syn, 'syste0060523875.jpg', 'system of the World')
test_books = [crypt, stone, ream, strange, chamber, color, quick, conf, system]

guest_salt = secrets.generate_salt()

test_user = User("guest", "guest@fakeurl.com", 0, "Guest", "User", guest_salt, secrets.hash_password("guest", guest_salt), secrets.generate_salt(15) )
