"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["mint"] = 3
# Add new key-value pair

ice_cream["vanilla"] += 10
# Modify key value

ice_cream["vanilla"] = 28
# Reassign key value

total_orders: int = 0
for flavor in ice_cream:
    # Loops through keys (flavors)
    print(flavor)
    total_orders += ice_cream[flavor]

print(ice_cream)
