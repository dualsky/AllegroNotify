from rinse.message import SoapMessage
from soap.request import SoapNoAuthRequest


class GetItemListRequset(SoapNoAuthRequest):
    def __init__(self, key, country, title,
                 offer_type="buyNow", price_max=0, price_min=0):
        super().__init__(key, country)
        self._title = title
        self._type = offer_type
        self._price_max = price_max
        self._price_min = price_min

    def _create_message(self, url):
        msg = SoapMessage()
        s = msg.elementmaker("s", url)

        init_body = s.DoGetItemsListRequest(
            s.webapiKey(self._key),
            s.countryId(self._country),
            s.filterOptions(
                s.item(
                    s.filterId("search"),
                    s.filterValueId(
                        s.item(self._title)
                    )
                )
            ),
            s.sortOptions(
                s.sortType("price")
            ),
            s.resultScope("3")
        )
        # [2]nd child is s.filterOptions
        filter_body = init_body.getchildren()[2]

        # Offer type xml
        if self._type != "both":
            offer_body = s.item(
                s.filterId("offerType"),
                s.filterValueId(
                    s.item(self._type.name)
                )
            )
            filter_body.insert(0, offer_body)

        # Price xml
        if self._price_max > 0 or self_.price_min > 0:
            price_body = s.item(
                s.filterId("price"),
                s.filterValueRange()
            )
            range_body = price_body.getchildren()[1]
            if self._price_max > 0:
                range_body.insert(0, s.rangeValueMax(
                    "{0:.2f}".format(round(self._price_max, 2))))
            if self._price_min > 0:
                range_body.insert(0, s.rangeValueMin(
                    "{0:.2f}".format(round(self._price_min, 2))))
            filter_body.insert(0, price_body)

        msg.body = init_body
        return msg
