from dataclasses import dataclass


@dataclass
class ContentMovie:
    alias: str
    uid: str
    cls: str
    for_kids: bool
    favs_title: str


@dataclass
class ContentSeries:
    alias: str
    uid: str
    cls: str
    for_kids: bool
    items_total: int
    favs_title: str


cheburashka = ContentMovie(
    alias='cheburashka',
    uid='fbe6a8e6-5dec-4a45-a54f-f309b96a5d4f',
    cls='Product.Movie',
    for_kids=True,
    favs_title='Чебурашка смотреть онлайн')

syostry = ContentSeries(
    alias='syostry',
    uid='c289d12e-71a2-4db4-b79c-7b13141a1f2e',
    cls='Product.Series',
    for_kids=False,
    items_total=3,
    favs_title='Сестры смотреть онлайн')
