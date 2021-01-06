from assertpy import assert_that


class SortAssert:
    def __init__(self, response, object_name):
        self.response = response
        self.object_name = object_name

    def checkOrderOfElements(self):
        assert_that([o.element_order for o in list(self.response.context[self.object_name])]).is_sorted()