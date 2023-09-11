import chardet

# Sample text with an unknown encoding
text = b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'

# Detect the encoding of the text
result = chardet.detect(text)

# Print the detected encoding
print("Detected encoding: {}".format(result['encoding']))