from exercice.classes.Diningmanager import DiningSpotNotFound, MenuItemNotFound
import pytest

@pytest.mark.parametrize("dining_spot, menu_item, expected_result", [
    ("Static Sushi", "Salmon Sashimi", "Salmon Sashimi removed from Static Sushi's menu"),
    ("Permanent Pizza", "Pineapple Pizza", "Pineapple Pizza removed from Permanent Pizza's menu")
])
def test_successful_menu_item_removal(dining_spot, menu_item, expected_result, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    result = dining_guide.remove_menu_item(dining_spot, menu_item)
    assert result == expected_result

@pytest.mark.parametrize("dining_spot, menu_item, expected_error_message", [
    ("Static Sushi", "Salmon Sushi", "Static Sushi does not have Salmon Sushi on the menu"),
    ("Missing Milkshake", "Mega Mystery", "Missing Milkshake does not exist")
])
def test_failed_menu_item_removal(dining_spot, menu_item, expected_error_message, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    with pytest.raises((MenuItemNotFound, DiningSpotNotFound)) as exc_info:
        dining_guide.remove_menu_item(dining_spot, menu_item)
    assert str(exc_info.value) == expected_error_message
