

class Item:
    def __init__(self, tree, ns):
        self._tree = tree
        self._id = tree.find("ns1:itemId", ns).text
        self._title = tree.find("ns1:itemTitle", ns).text
        self._time_left = tree.find("ns1:timeToEnd", ns).text
        self._type = tree.find(".//ns1:priceType", ns).text
        self._price = tree.find(".//ns1:priceValue", ns).text
        self._damaged = None
        self._categories = []
        self._url = "http://allegro.pl/show_item.php?item={}".format(self._id)

    def __str__(self):
        return '''Item Info:
        id: {}, title: {},
        time_left: {}, type: {}, price: {},
        damaged: {}, categories: {},
        link: {}'''.format(
            self._id, self._title, self._time_left,
            self._type, self._price, self._damaged,
            self._categories, self._url)
