from shop import in_stock

stock = {"P001": 3, "P002": 0}

assert in_stock(stock, "P001")
assert not in_stock(stock, "P002")

print("Stock test passed")
def test_find_case_insensitive():
    assert [p.sku for p in find_by_name(products, "KEY")] == ["B2"]