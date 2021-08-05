import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
train = []
data = json.loads(open('nfL6.json','r').read())
for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answer'])
    if k>1024:
        break

chatbot = ChatBot('Yahoo')
trainer = ListTrainer(chatbot)
trainer.train(train)

while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)
