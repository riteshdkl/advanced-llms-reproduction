import ollama

# A short snippet with two common, deliberate weaknesses, for the model to catch:
# 1) the SQL query is built by gluing strings together (SQL-injection risk),
# 2) a password is hardcoded in the source.
code = '''
def login(user_id, password):
    query = "SELECT * FROM users WHERE id = " + user_id
    db.execute(query)
    SECRET = "hardcoded-admin-password"
'''

prompt = (
    "You are a careful code reviewer. List the security weaknesses in this "
    "Python code and how to fix each one:\n" + code
)

response = ollama.generate(model="llama3.2:1b", prompt=prompt)
print(response["response"])
