import         return None
    # Update last login
    now_str = datetime.now().isoformat()
    cursor.execute("UPDATE users SET last_login = ? WHERE user_id = ?", (now_str, user_dict['user_id']))
    conn.commit()
    conn.close()
    del user_dict['password_hash']
    user_dict['last_login'] = now_str
    return user_dict
def get_user_by_id(user_id):
    """Fetches user profile by user_id."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    d = dict(row)
    if 'password_hash' in d:
        del d['password_hash']
    return d
def get_user_by_username(username):
    """Fetches user profile by username."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username.strip().lower(),))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    d = dict(row)
    if 'password_hash' in d:
        del d['password_hash']
    return d