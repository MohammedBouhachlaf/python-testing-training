from exercice.classes.Diningmanager import MenuItemAlreadyListed
import pytest

@pytest.mark.parametrize(
    "dining_spot, menu_item, item_details, item_cost, expected_result",
    [
        ("Default Diner", "Data", "Couldn't find anything eatable that starts with 'D'", 1, "Data added to Default Diner's menu"),
        ("Default Diner", "Dust", "Maybe you could eat this, I wouldn't recommend", 0.01, "Dust added to Default Diner's menu")
    ]
)
def test_successful_menu_item_addition(dining_spot, menu_item, item_details, item_cost, expected_result, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    result = dining_guide.append_menu_item(dining_spot, menu_item, item_details, item_cost)
    assert result == expected_result

@pytest.mark.parametrize(
    "dining_spot, menu_item, item_details, item_cost, expected_error",
    [
        ("Static Sushi", "Salmon Sashimi", "Salmon (4 pieces)", 1.10, "Static Sushi already has Salmon Sashimi on the menu"),
        ("Default Diner", "Dust", "I'll pay you if you eat it, or just get a broom and clean the place idk", -100, "Cost must be positive"),
        ("Missing Milkshake", "Mega Mystery", "It's actually an escape game, you will get clues to find us", 25, "Missing Milkshake does not exist")
    ]
)
def test_failed_menu_item_addition(dining_spot, menu_item, item_details, item_cost, expected_error, dining_guide_fixture):
    dining_guide = dining_guide_fixture
    with pytest.raises((MenuItemAlreadyListed, ValueError, DiningSpotNotFound)) as exc_info:
        dining_guide.append_menu_item(dining_spot, menu_item, item_details, item_cost)
    assert str(exc_info.value) == expected_error
