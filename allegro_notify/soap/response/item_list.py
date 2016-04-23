from soap.response import SoapResponse


__all__ = ["ItemListResponse"]


class ItemListResponse(SoapResponse, list):
    def __init__(self, response):
        list.__init__(self)
        SoapResponse.__init__(self, response)
        self._tree = self._body.find("ns1:doGetItemsListResponse", self._ns)
        self._items_count = self._tree.find("ns1:itemsCount", self._ns).text
        if self._items_count != "0":
          tree_items = self._tree.find("ns1:itemsList", self._ns)
          for tree_item in tree_items.findall("ns1:item", self._ns):
              self.append(Item(tree_item, self._ns))


class Item:
    def __init__(self, tree, ns):
        self._tree = tree
        self._id = tree.find("ns1:itemId", ns).text
        self._title = tree.find("ns1:itemTitle", ns).text
        self._time_left = tree.find("ns1:timeToEnd", ns).text
        self._type = tree.find(".//ns1:priceType", ns).text
        self._price = tree.find(".//ns1:priceValue", ns).text
        self._url = "http://allegro.pl/show_item.php?item={}".format(self._id)

    def __str__(self):
        return '''Item Info:
        id: {}, title: {},
        time_left: {}, type: {}, price: {},
        link: {}'''.format(
            self._id, self._title, self._time_left,
            self._type, self._price, self._url)
