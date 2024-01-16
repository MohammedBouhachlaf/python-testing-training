from exercice.classes.Diningmanager import DiningSpotNotFound, MenuItemNotFound
import pytest

@pytest.mark.parametrize(
    "dining_spot, menu_item, item_details, item_cost, expected_result",
    [
        ("Static Sushi", "Salmon ", "RAW Salmon (6 pieces)", 5.99, "saumoau"),
        ("Permanent Pizza", "Pineapple Pizza", "If you buy one, we'll send your address to Mauro Rocco (you will die)", 9999999, "pizza")
    ]
)
def test_successful_menu_item_update(dining_spot, menu_item, item_details, item_cost, expected_result, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    result = dining_guide.modify_menu_item(dining_spot, menu_item, item_details, item_cost)
    assert result == expected_result

@pytest.mark.parametrize(
    "dining_spot, menu_item, item_details, item_cost, expected_error_message",
    [
        ("Static Sushi", "Salmon Sushi", "Salmon (4 pieces)", 5, "Static Sushi does not have Salmon Sushi on the menu"),
        ("Missing Milkshake", "Mega Mystery", "It's actually an escape game, you will get clues to find us", 25, "Missing Milkshake does not exist")
    ]
)
def test_failed_menu_item_update(dining_spot, menu_item, item_details, item_cost, expected_error_message, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    with pytest.raises((MenuItemNotFound, ValueError, DiningSpotNotFound)) as exc_info:
        dining_guide.modify_menu_item(dining_spot, menu_item, item_details, item_cost)
    assert str(exc_info.value) == expected_error_message
