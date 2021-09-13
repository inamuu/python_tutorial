
users = {
    "tanaka": "active",
    "suzuki": "inactive",
    "sato": "active"
}

def main():
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    return active_users

if __name__ == '__main__': main()
