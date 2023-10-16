import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write an email for resignation\n"
    },
    {
      "role": "assistant",
      "content": "Subject: Resignation Letter\n\nDear [Supervisor's Name],\n\nI hope this email finds you well. I wanted to begin by expressing my heartfelt gratitude for the valuable experiences and growth opportunities that I have had during my tenure at [Company Name]. It has been a pleasure working with you and the entire team.\n\nAfter careful consideration, I have made the difficult decision to resign from my position as [Your Position] at [Company Name], effective [last working day, typically two weeks from the date of resignation]. This decision has not been easy, as I have thoroughly enjoyed being a part of this organization and have built strong professional relationships along the way.\n\nI have accepted another career opportunity that aligns more closely with my long-term goals and aspirations. While I am excited about this new venture and the challenges it brings, I am also sad to leave behind the remarkable team, supportive work environment, and the positive company culture that I have experienced at [Company Name].\n\nI am committed to making this transition as seamless as possible. I am more than willing to assist in the training and handover of my responsibilities and provide any necessary support during my remaining time at [Company Name]. Additionally, I will ensure that all outstanding projects and tasks are completed or appropriately delegated before my departure. I"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)