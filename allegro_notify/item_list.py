from item import Item


class ItemList(list):
    def __init__(self, body, ns):
        list.__init__(self)
        self._tree = body.find("ns1:doGetItemsListResponse", ns)
        self._items_count = self._tree.find("ns1:itemsCount", ns).text
        tree_items = self._tree.find("ns1:itemsList", ns)
        for tree_item in tree_items.findall("ns1:item", ns):
            self.append(Item(tree_item, ns))
