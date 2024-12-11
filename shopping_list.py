class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    """ 返回获得购物车的商品数量 """

    def get_item_count(self):
        return len(self.shopping_list)

    """ 返回购物车总价格 """

    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price
