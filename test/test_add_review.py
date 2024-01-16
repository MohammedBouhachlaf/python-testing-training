from restaurant_reviews import RestaurantReviews

def test_add_valid_review():
    rr = RestaurantReviews()
    result = rr.add_review("Cafe Mocha", "Great coffee and pastries.", 4)
    assert result == "Review added for Cafe Mocha."
    # assert rr.get_review("Cafe Mocha") == {'review_text': "Great coffee and pastries.", 'rating': 4}

def test_add_invalid_rating_above_5():
    rr = RestaurantReviews()
    result = rr.add_review("Cafe Mocha", "Good ambiance.", 6)
    assert result == "Invalid rating. It must be between 1 and 5."

def test_add_invalid_rating_below_1():
    rr = RestaurantReviews()
    result = rr.add_review("Cafe Mocha", "Good ambiance.", 0)
    assert result == "Invalid rating. It must be between 1 and 5."