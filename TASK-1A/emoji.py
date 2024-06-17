import demoji

# Initialize the demoji module (downloads emoji data if not already present)
demoji.download_codes()

# Example text containing emojis
text_with_emojis = "I love playing 🎾 and 🏀!"

# Replace emojis with their text descriptions
text_with_descriptions = demoji.replace_with_desc(text_with_emojis)

print(text_with_descriptions)