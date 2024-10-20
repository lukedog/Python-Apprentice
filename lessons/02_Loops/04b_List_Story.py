"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', '.', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

story = [] 

# Create a story using the words in the list
story.append(words[0])
story.append(words[2])
story.append(words[7])
story.append(words[9])
story.append(words[7])
story.append(words[1])
story.append(words[5])
story.append(words[6])
story.append(words[7])
story.append(words[13])
story.append(words[11])
story.append(words[19])
story.append(words[15])
story.append(words[10])
story.append(words[17])
story.append(words[18])
story.append(words[11])
# Display the story to the user
print(' '.join(story))