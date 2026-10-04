# Deliberately insecure sample, only for the security scanner to analyze.
# Do NOT run this file — it references things that don't exist.

def login(user_id, password):
    query = "SELECT * FROM users WHERE id = " + user_id   # SQL built from strings
    db.execute(query)

SECRET = "hardcoded-admin-password"   # a hardcoded secret