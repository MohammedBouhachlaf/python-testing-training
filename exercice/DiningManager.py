class DiningManager:
    def __init__(self):
        self.dining_spots = {}

    def fetch_dining_spot(self, name: str):
        if name not in self.dining_spots:
            raise DiningSpotNotFound(f'{name} does not exist')
        return self.dining_spots[name]

    def register_dining_spot(self, name: str):
        if name in self.dining_spots:
            raise DiningSpotAlreadyRegistered(f'{name} already exists')
        self.dining_spots[name] = {"menu": {}}
        return self

    def deregister_dining_spot(self, name: str):
        if name not in self.dining_spots:
            raise DiningSpotNotFound(f'{name} does not exist')
        del self.dining_spots[name]
        return self

    def append_menu_item(self, spot: str, item: str, details: str, cost: float):
        if cost < 0:
            raise ValueError('Cost must be positive')
        if spot not in self.dining_spots:
            raise DiningSpotNotFound(f'{spot} does not exist')
        if item in self.dining_spots[spot]['menu']:
            raise MenuItemAlreadyListed(f'{spot} already has {item} on the menu')
        self.dining_spots[spot]["menu"][item] = {"details": details, "cost": cost}
        return f"{item} added to {spot}'s menu" if spot[-1] != 's' else f"{item} added to {spot}' menu"

    def list_menu(self, spot: str):
        if spot not in self.dining_spots:
            raise DiningSpotNotFound(f'{spot} does not exist')
        menu = []
        for item_name, item_info in self.dining_spots[spot]["menu"].items():
            menu.append({"name": item_name, "details": item_info["details"], "cost": item_info["cost"]})
        return menu

    def modify_menu_item(self, spot: str, item: str, details: str, cost: float):
        if cost < 0:
            raise ValueError('Cost must be positive')
        if spot not in self.dining_spots:
            raise DiningSpotNotFound(f'{spot} does not exist')
        if item not in self.dining_spots[spot]['menu']:
            raise MenuItemNotFound(f'{spot} does not have {item} on the menu')
        self.dining_spots[spot]["menu"][item] = {"details": details, "cost": cost}
        return f"{item} updated on {spot}'s menu" if spot[-1] != 's' else f"{item}
    
    def remove_menu_item(self, spot: str, item: str):
    if spot not in self.dining_spots:
        raise DiningSpotNotFound(f'{spot} does not exist')
    if item not in self.dining_spots[spot]['menu']:
        raise MenuItemNotFound(f'{spot} does not have {item} on the menu')
    del self.dining_spots[spot]["menu"][item]
    return f"{item} removed from {spot}'s menu" if spot[-1] != 's' else f"{item} removed from {spot}' menu"

