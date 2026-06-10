import pytest

from Pages.SearchPage import SearchPage
from Utilities import excelReader


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_validproduct(self):
        validsearch = excelReader.get_data("ExcelFiles/SearchData.xlsx","Search")
        search_term = validsearch[0]
        search = SearchPage(self.driver)
        search.search_product(search_term)
        assert search.is_product_displayed("HP LP3065")
        print("Done")
    def test_invalidproduct(self):
        invalidsearch = excelReader.get_data("ExcelFiles/SearchData.xlsx","Search")
        search_term = invalidsearch[1]
        search = SearchPage(self.driver)
        search.search_product(search_term)
        expected = "There is no product that matches the search criteria."
        actual = search.get_no_product_message()
        assert actual == expected
        print("Done")