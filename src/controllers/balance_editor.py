from typing import Dict
from src.models.interface.user_repository import UserRepositoryInterface

class BalanceEditor:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> Dict:
        self.__user_repository.edit_balance(user_id, new_balance)
        return {
            "type": "User",
            "count": 1,
            "new_balance": new_balance
        }