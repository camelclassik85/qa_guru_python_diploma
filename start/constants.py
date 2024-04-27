import string

'''Generator'''
email_length = 7
password_length = 7
generator_collection = string.ascii_letters + string.digits

'''URL'''
web_base_url = "https://start.ru"
web_signup_url = "/signup"
web_signin_url = "/signin"
web_account_url = "/account"
web_search_url = "/search"
web_favorites_url = "/favorites"
web_series_url = "/series"


class ApiUrl:
    base_api_url = 'https://api.start.ru'
    favorites_endpoint = '/profile/favorites'


'''Apikey'''
web_apikey = "a20b12b279f744f2b3c7b5c5400c4eb5"

'''Title'''
web_signup_page_title = "Регистрация на Start"
web_signin_page_title = "Вход в аккаунт Start"
web_search_title = "Поиск"
web_main_page_title = ("Онлайн-кинотеатр START — смотреть легальные фильмы,"
                       " сериалы, мультфильмы онлайн. "
                       "Интернет кинотеатр с хорошим качеством видео")
web_favorites_title = "Избранное"
web_series_page_title = "Сериалы - смотреть онлайн"


class Search:
    search_with_one_element_result = "лермонтов"
    search_multiple_element_result_per = "пер"
    search_multiple_element_result_nov = "нов"
    search_no_results = "перdjdjdjjdjdj"
    search_recommendation_title_text = "Ничего не нашлось"
    search_recommendation_desc_text = "Попробуйте изменить запрос"


class WebDriverDefaults:
    default_browser_name = "chrome"
    default_browser_version = "120"
    default_context = "web_selenoid"


TIMEOUT = 10.0
