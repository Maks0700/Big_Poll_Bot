from aiogram.fsm.state import State,StatesGroup
from enum import Enum


class Survey(StatesGroup):#Состояния основные для опроса
    name=State()
    email=State()
    sport=State()
    news_letter=State()
    
class SportDetails(StatesGroup):#Состояния для спорта
    tennis=State()
    football=State()
    formula_one=State()


class KnownSports(str,Enum):#Перечисления для хранения известных видов спорта
    tennis="Tennis"
    football="Football"
    formula_one="Formula_one"
    
class KnownF1Tracks(str,Enum):#Создаем перечисления для трасс Формулы 1, как аргкумент для клавиатуры
    monako="Monaco"
    spa="Spa"
    suzuka="Suzuka"
    monza="Monza"
    
    