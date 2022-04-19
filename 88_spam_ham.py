from typing import SupportsIndex


message = input("Enter your message here:")
badtxt = 'fuck'

if badtxt in message:
   message = message.replace(f'{badtxt}','####')
   print("This censor words should not be used in email.")


print(message)