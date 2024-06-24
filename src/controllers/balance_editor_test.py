from ..controllers.balance_editor import BalanceEditor

user_id = 1
new_balance = 1000.0


class MockBalanceRepository:

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        return (user_id, new_balance)

def test_balance_editor():
    balance_editor = BalanceEditor(MockBalanceRepository())
    response = balance_editor.edit(1, 1000.0)

    print(response)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new_balance"] == 1000.0
#   assert balance_editor.edit(1, 1000.0) == {
#     "type": "User",
#     "count": 1,
#     "new balance": 1000.0
#   }