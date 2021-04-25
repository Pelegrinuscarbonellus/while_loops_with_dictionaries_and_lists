swimming_pool_with_users = ['santpedor', 'manresa', 'solsona', 'vic']
swimming_pool_without_users = []

while swimming_pool_with_users:

    new_swim_users = swimming_pool_with_users.pop()

    print(f"verified users: {new_swim_users.title()}")

    print(swimming_pool_with_users)