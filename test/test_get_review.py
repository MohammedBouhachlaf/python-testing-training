from restaurant_reviews import RestaurantReviews

def test_get_existing_review():
    rr = RestaurantReviews()
    rr.add_review("Pasta Palace", "Delicious pasta dishes.", 5)
    result = rr.get_review("Pasta Palace")
    assert result == {'review_text': "Delicious pasta dishes.", 'rating': 5}

def test_get_non_existent_review():
    rr = RestaurantReviews()
    result = rr.get_review("Burger Bistro")
    assert result == "Review not found."