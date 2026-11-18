class Inventory:
    CATEGORIES = ("文房具", "飲料", "日用品")

    def __init__(self, products):
        self.products = products

    def get_all(self):
        # 呼び出し側が一覧を並べ替えても元の順番を残す
        return self.products.copy()

    def get_category_report(self):
        report = {
            category: {"count": 0, "stock": 0, "amount": 0}
            for category in self.CATEGORIES
        }

        for product in self.products:
            category_report = report.get(product.category)
            if category_report is None:
                continue
            category_report["count"] += 1
            category_report["stock"] += product.stock
            category_report["amount"] += product.price * product.stock

        total = {
            "count": len(self.products),
            "stock": sum(product.stock for product in self.products),
            "amount": sum(product.price * product.stock for product in self.products),
        }
        report["全体"] = total
        return report
