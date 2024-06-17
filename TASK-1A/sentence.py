subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

# Generate and print all possible sentences
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            print(sentence)