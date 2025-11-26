def price_discount(item_name, original_price, promo_code):
	if promo_code == "SAVE10":
		discounted_price = original_price - original_price * (10/100)
	elif promo_code == "HALFOFF":
		discounted_price = original_price - original_price * (50/100)
	else:
		discounted_price = original_price

	return discounted_price

print(price_discount('cup', 500, 'HALFOFF'))