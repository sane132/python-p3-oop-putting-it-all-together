class Book:
    def __init__(self, title=None, page_count=None):
        self.title = title
        self._page_count = None  # use private attr to control validation
        if page_count is not None:
            self.page_count = page_count  # will trigger setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
