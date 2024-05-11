from start_project_tests.models.pages.account_page import AccountPage
from start_project_tests.models.pages.content_page import ContentPage
from start_project_tests.models.pages.cookie_popup import CookiePopup
from start_project_tests.models.pages.favorites_page import FavoritesPage
from start_project_tests.models.pages.header import Header
from start_project_tests.models.pages.main_page import MainPage
from start_project_tests.models.pages.registration_popup import RegistrationPopup
from start_project_tests.models.pages.search_page import SearchPage
from start_project_tests.models.pages.series_page import SeriesPage
from start_project_tests.models.pages.signin_page import SigninPage
from start_project_tests.models.pages.signup_page import SignupPage


class PageFactory:

    def __init__(self):
        self.account_page = AccountPage()
        self.cookie_popup = CookiePopup()
        self.signup_page = SignupPage()
        self.signin_page = SigninPage()
        self.header = Header()
        self.search_page = SearchPage()
        self.main_page = MainPage()
        self.content_page = ContentPage()
        self.registration_popup = RegistrationPopup()
        self.favorites_page = FavoritesPage()
        self.series_page = SeriesPage()


pages = PageFactory()
