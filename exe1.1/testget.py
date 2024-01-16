import pytest

@pytest.mark.parametrize(
    "dining_spot, expected_menu",
    [
        ('Default Diner', []),
        ("Static Sushi", [{"name": "Salmon Sashimi", "description": "Salmon (6 pieces)", "price": 5.99}]),
        ("Permanent Pizza", [
            {"name": "Pepperoni Pizza", "description": "A pizza with pepperoni on it", "price": 7.50},
            {"name": "Pineapple Pizza", "description": "A demon coming straight from hell", "price": 666}
        ])
    ]
)
def test_retrieve_menu(dining_spot, expected_menu, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    menu = dining_guide.list_menu(dining_spot)
    assert menu == expected_menu
