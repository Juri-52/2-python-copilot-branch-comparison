from inventory import Inventory
from product import Product
from storage import load_products


def test_product_info():
    product = Product(1, "ノート", "文房具", 250, 8)

    assert product.info() == "1 | ノート | 文房具 | 250円 | 在庫 8個"


def test_load_catalog():
    products = load_products()

    assert len(products) == 10
    assert products[0].name == "ノート"
    assert products[0].price == 250
    assert products[0].stock == 8
    assert products[-1].id == 10


def test_get_all_keeps_catalog_order():
    inventory = Inventory(load_products())
    products = inventory.get_all()

    assert products[0].id == 1
    assert products[-1].id == 10


def test_get_all_returns_separate_list():
    inventory = Inventory(load_products())

    displayed_products = inventory.get_all()
    displayed_products.pop()

    assert len(displayed_products) == 9
    assert len(inventory.get_all()) == 10


def test_empty_inventory():
    inventory = Inventory([])

    assert inventory.get_all() == []


def test_category_report():
    products = [
        Product(1, "ノート", "文房具", 250, 8),
        Product(2, "緑茶", "飲料", 150, 6),
        Product(3, "ティッシュ", "日用品", 200, 2),
    ]

    report = Inventory(products).get_category_report()

    assert list(report) == ["文房具", "飲料", "日用品", "全体"]
    assert report["文房具"] == {"count": 1, "stock": 8, "amount": 2000}
    assert report["飲料"] == {"count": 1, "stock": 6, "amount": 900}
    assert report["日用品"] == {"count": 1, "stock": 2, "amount": 400}
    assert report["全体"] == {"count": 3, "stock": 16, "amount": 3300}


def test_empty_category_report():
    report = Inventory([]).get_category_report()

    assert report == {
        "文房具": {"count": 0, "stock": 0, "amount": 0},
        "飲料": {"count": 0, "stock": 0, "amount": 0},
        "日用品": {"count": 0, "stock": 0, "amount": 0},
        "全体": {"count": 0, "stock": 0, "amount": 0},
    }
