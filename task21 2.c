def format_function(num, char):
    return "{0:{1}^10}".format(num, char)

result = format_function(145, 'o')
print("Formatted String:", result)
print("Representation used:", type(result).__name__)
