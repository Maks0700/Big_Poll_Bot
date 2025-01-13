from enum import IntEnum, auto
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData



class ShopAction(IntEnum):
    products=auto()
    address=auto()
    root=auto()





class ShopCbData(CallbackData,prefix="shop"):
    action:ShopAction



    

class ProductionActions(IntEnum):
    detail=auto()
    update=auto()
    delete=auto()
    
class ProductCbData(CallbackData,prefix="product"):
    id:int
    title:str
    price:float
    action:ProductionActions
    


def create_builder_shop()->InlineKeyboardBuilder:
    builder=InlineKeyboardBuilder()
    builder.button(text="Show the products",callback_data=ShopCbData(action=ShopAction.products).pack())
    builder.button(text="Show the address",callback_data=ShopCbData(action=ShopAction.address).pack())
    
      
    
    
    builder.adjust(1)
    return builder.as_markup()

def create_list_products()->InlineKeyboardBuilder:
    builder=InlineKeyboardBuilder()
    builder.button(
        text="Back to root",callback_data=ShopCbData(action=ShopAction.root)
    )
    for idx,(name,price) in enumerate([
        ("Laptop",1600),
        ("Tablet",2000),
        ("Desktop",9000)
    ],start=1):
        builder.button(text=name,callback_data=ProductCbData(id=idx,
                                                             title=name,
                                                             price=price,
                                                             action=ProductionActions.detail))
    builder.adjust(1)
    return builder.as_markup()


def product_details_kb(product_callback_data:ProductCbData)->InlineKeyboardBuilder:
    builder=InlineKeyboardBuilder()
    builder.button(
        text="Back to products",
        callback_data=ShopCbData(action=ShopAction.products).pack()
    )
    for label,action in [
        ("Update",ProductionActions.update),
        ("Delete",ProductionActions.delete)
    ]:
        builder.button(text=label,callback_data=ProductCbData(action=action,
            **product_callback_data.model_dump(include={"id","title","price"}),
        ))
    builder.adjust(1,2)
    return builder.as_markup()


def build_update_keyboard(product_callback:ProductCbData):
    builder=InlineKeyboardBuilder()
    builder.button(text=f"Back to {product_callback.title}",callback_data=ProductCbData(action=ProductionActions.detail,**product_callback.model_dump(
        include={"id","title","price"})).pack())
    builder.button(text="Update",callback_data="...")
    
    return builder.as_markup()

    