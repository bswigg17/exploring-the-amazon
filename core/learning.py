# import numpy as np
# import pandas as pd


# def main():
#     bad_text = """
#             The payment process is a terrible process with lots of shortcommings.
#             Sometimes glitchy and does not work at some merchants causing to then use card.
#     """

#     good_text = """
#             I love the new payment process. So simple and easy to use.
#             This is fantastic and innovative!
#     """

#     blob = TextBlob(bad_text)

#     total = 0
#     count = 0
#     for sentence in blob.sentences:
#         total += sentence.sentiment[0]
#         count += 1

#     avg = total / count

#     print('Bad Sentiment' if avg < 0 else 'Good Sentiment')


# def future():
#     train = [
#         ('The Pid-Pad is broken.', 'PINPAD'),
#         ('Pid-Pad is down all the time.', 'PINPAD'),
#         ('The Pid-Pad installation is not good.', 'PINPAD'),
#         ('The POS crashed.', 'POS'),
#         ('Cannot login to POS.', 'POS'),
#         ('The POS is down.', 'POS'),
#     ]   
#     test = [
#         ('The Pin-Pad is having a hard time booting.', 'PINPAD'),
#         ('I hate the new Pin-Pad software.', 'PIDPAD'),
#         ("Pin-Pad is bad.", 'PINPAD'),
#         ("POS.", 'POS'),
#     ]
#     model = NaiveBayesClassifier(train)
#     res = model.classify('The Pin-Pad is down.')
#     res2 = model.classify('So hard to use the POS.')
#     print(res)
#     print(res2)
#     #print(res2)

# future()
