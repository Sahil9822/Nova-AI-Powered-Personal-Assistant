import google.generativeai as genai
from config import apikey

genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
response = chat.send_message("I have 2 dogs in my house.", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)
response = chat.send_message("How many paws are in my house?", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)

print(chat.history)


'''
That
________________________________________________________________________________
's wonderful!  What breeds are they?  Do you have any fun
________________________________________________________________________________
 stories about them?

________________________________________________________________________________
If
________________________________________________________________________________
 you have two dogs, and each dog has four paws, then there are eight
________________________________________________________________________________
 paws in your house.

________________________________________________________________________________
[parts {
  text: "Hello"
}
role: "user"
, parts {
  text: "Great to meet you. What would you like to know?"
}
role: "model"
, parts {
  text: "I have 2 dogs in my house."
}
role: "user"
, parts {
  text: "That\'s wonderful!  What breeds are they?  Do you have any fun stories about them?\n"
}
role: "model"
, parts {
  text: "How many paws are in my house?"
}
role: "user"
, parts {
  text: "If you have two dogs, and each dog has four paws, then there are eight paws in your house.\n"
}
role: "model"
]
'''