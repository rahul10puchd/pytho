import wolframalpha

input = raw_input("Q: ")
app_id = "W97Q7V-EKQWJALLX8"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer
