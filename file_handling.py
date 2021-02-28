f = open('meeting.jpg', 'rb')

f1 = open('meeting_copy.jpg', 'wb')

for i in f:
    f1.write(i)