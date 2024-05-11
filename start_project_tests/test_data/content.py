from dataclasses import dataclass


@dataclass
class ContentMovie:
    alias: str
    uid: str
    cls: str
    for_kids: bool
    favs_title: str
    title: str


@dataclass
class ContentSeries:
    alias: str
    uid: str
    cls: str
    for_kids: bool
    items_total: int
    favs_title: str
    title: str


cheburashka = ContentMovie(
    alias='cheburashka',
    uid='fbe6a8e6-5dec-4a45-a54f-f309b96a5d4f',
    cls='Product.Movie',
    for_kids=True,
    favs_title='Чебурашка смотреть онлайн',
    title='Чебурашка')

lermontov = ContentMovie(
    alias='lermontov',
    uid='0ba973d6-125f-4d16-9d57-7118a59eec49',
    cls='Product.Movie',
    for_kids=False,
    favs_title='Лермонтов смотреть онлайн',
    title='Лермонтов')

syostry = ContentSeries(
    alias='syostry',
    uid='c289d12e-71a2-4db4-b79c-7b13141a1f2e',
    cls='Product.Series',
    for_kids=False,
    items_total=3,
    favs_title='Сестры смотреть онлайн',
    title='Сестры')

chyornaya_vesna = ContentSeries(
    alias='chyornaya-vesna',
    uid='d979664b-3654-4e61-945d-33f78215cd5d',
    cls='Product.Series',
    for_kids=False,
    items_total=1,
    favs_title='Черная весна смотреть онлайн',
    title='Черная весна')
