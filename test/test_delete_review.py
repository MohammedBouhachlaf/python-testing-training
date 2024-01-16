import pytest
from restaurant_reviews import RestaurantReviews

def test_delete_existing():
    rr= RestaurantReviews()
    rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
    result = rr.delete_review("Pasta Palace")
    assert (result == "Review deleted for Pasta Palace.")
    # Ajout d'une partie "fonctionnelle" à  notre test : 
    # On test aussi les implications de la suppression d'un review
    result2 = rr.get_review("Pasta Palace") 
    assert(result2 == "Review not found.")

# Vérification du cas de "non fonctionnement" avec exception
def test_delete_non_existing():
    rr = RestaurantReviews()
    with pytest.raises(ValueError) as e:
        rr.delete_review('Unkown Restaurant')
    assert str(e.value) == "Review not found to delete." 