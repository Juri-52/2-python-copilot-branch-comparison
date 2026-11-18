from inventory import Inventory
from storage import load_products


def show_products(products):
    if not products:
        print("該当する商品はありません。")
        return

    for product in products:
        print(product.info())


def show_category_report(inventory):
    report = inventory.get_category_report()
    has_products = report["全体"]["count"] > 0

    for category in Inventory.CATEGORIES:
        category_report = report[category]
        if has_products:
            print(
                f"{category}: {category_report['count']}種類 "
                f"{category_report['stock']}個 {category_report['amount']}円"
            )

    total = report["全体"]
    print(f"全体: {total['count']}種類 {total['stock']}個 {total['amount']}円")


def main():
    inventory = Inventory(load_products())

    while True:
        print("\n商品管理")
        print("1: 商品一覧")
        print("2: 分類別レポート")
        print("0: 終了")
        choice = input("選択: ").strip()

        if choice == "1":
            show_products(inventory.get_all())
        elif choice == "2":
            show_category_report(inventory)
        elif choice == "0":
            print("終了します。")
            break
        else:
            print("メニューの番号を入力してください。")


if __name__ == "__main__":
    main()
