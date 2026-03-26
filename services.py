from managers import UserRepository

repo = UserRepository()

def create_user(name: str, email: str):
    if not email:
        raise ValueError("Email is required")
    return repo.create(name=name, email=email)

def get_user(user_id: int):
    return repo.get_by_id(user_id)