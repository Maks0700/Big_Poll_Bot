from enum import Enum
from random import randint
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,KeyboardButtonPollType,InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButtonRequestUser,KeyboardButtonRequestChat
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

# keyboard=ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Test")],resize_keyboard=True
# ])



class Button_Text:
    HELLO="Hello"
    WHATS_NEXT="What is next"
    BYE="Bye"
    
    
class RandomNumaction(Enum):
    dice="dice"
    modal="modal"    
    

class RandomNumCbData(CallbackData,prefix="random_num"):
    action:RandomNumaction




    
def create_keyboard():
    button_hello=KeyboardButton(text=Button_Text.HELLO)
    button_help=KeyboardButton(text=Button_Text.WHATS_NEXT)
    button_bye=KeyboardButton(text=Button_Text.BYE)
    buttons_rows=[button_hello,button_help,button_bye]
    
    markup=ReplyKeyboardMarkup(keyboard=[buttons_rows],resize_keyboard=True)
    return markup


def code_command():
    test_rows=[
        "1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"
    ]
    # rows_total=[KeyboardButton(text=num)for num in test_rows]
    # keyboard_total=ReplyKeyboardMarkup(keyboard=[rows_total],resize_keyboard=True)
    # return keyboard_total
    builder=ReplyKeyboardBuilder()
    for item in test_rows:
        builder.add(KeyboardButton(text=item))
    builder.adjust(3)
    return builder.as_markup(resize_keyboard=True)


def get_actions_keyboard()->ReplyKeyboardMarkup:
    builder=ReplyKeyboardBuilder()
    builder.button(text="Send Location",request_location=True)
    builder.button(text="Send my phone",request_contact=True)
    builder.button(text="Send Poll",request_poll=KeyboardButtonPollType())
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
    

def inline_keyboard_create()->InlineKeyboardBuilder:
    tg_channel_btn=InlineKeyboardButton(text="Channel",url="https://huggingface.co/chat/")
    git_hub=InlineKeyboardButton(text="GitHub",url="https://github.com/?ysclid=m5jxgakpfz946087865")
    
    btn_random_num=InlineKeyboardButton(text="🎲 Random num",callback_data=RandomNumCbData(action=RandomNumaction.dice).pack())
    btn_random_number=InlineKeyboardButton(text="😛 Randdom number",callback_data=RandomNumCbData(action=RandomNumaction.modal).pack())
    
    
    rows=[tg_channel_btn]
    
    keyboard=InlineKeyboardMarkup(inline_keyboard=[rows,[git_hub],[btn_random_num],[btn_random_number]])
    return keyboard

def action_keyboard(button:str="Random number"):
    builder=InlineKeyboardBuilder()
    
    builder.button(
        text=button,callback_data="random_edited_text")
    builder.add()
    
    
    return builder.as_markup()

def create_request():
    builder=ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Выбрать премиум-пользователя",request_user=KeyboardButtonRequestUser(request_id=1)),
        KeyboardButton(text="Выбрать супергруппу с форумами",request_chat=KeyboardButtonRequestChat(request_id=2,chat_is_channel=False,chat_is_forum=True))
    )
    builder.as_markup()
    return builder


def create_increase_decrease_buttons():
    builder=InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="+1",callback_data="num_incr"),
        InlineKeyboardButton(text="-1",callback_data="num_decr")
        
    )
    builder.button(text="Подтвердить",callback_data="num_confirm")
    
    
    
    return builder.as_markup()

random_num_updated_cb_data="random_num_updated_cb_data"


class FixedRandomNumCbData(CallbackData,prefix="fixed_random"):
    number:int
    



def build_actions_kb(
    random_number_button_text="Random number"
)->InlineKeyboardMarkup:
    builder=InlineKeyboardBuilder()
    cb_data_1=FixedRandomNumCbData(number=randint(1,20))
    builder.button(text=random_number_button_text,
                   callback_data=cb_data_1.pack())
    
    builder.button(
        text=f"Fixed random number {cb_data_1.number}",
        callback_data=cb_data_1.pack()
    )
    builder.button(
        text=f"Random number: [HIDDEN]",
        callback_data=FixedRandomNumCbData(number=randint(1,20)).pack()
        
        
        )
    builder.adjust(1)
    return builder.as_markup()


def known_sport_to_kb_common():
    builder = ReplyKeyboardBuilder()
    