from aiogram import Router,F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from keyboards.keyboard_shop import ShopAction,ShopCbData, build_update_keyboard, create_builder_shop, create_list_products,ProductionActions,ProductCbData, product_details_kb


router=Router()

@router.callback_query(ShopCbData.filter(F.action==ShopAction.address))
async def show_products(callback_query:CallbackQuery):
    print(callback_query.data)
    await callback_query.answer(text="Your address is still in progress",cache_time=40)
    

@router.callback_query(ShopCbData.filter(F.action==ShopAction.products))
async def send_products_list(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Available products",reply_markup=create_list_products())





@router.callback_query(ShopCbData.filter(F.action==ShopAction.root))
async def return_root(callback:CallbackQuery):
    await callback.message.answer("Your shop actions:",reply_markup=create_builder_shop())



@router.callback_query(ProductCbData.filter(F.action==ProductionActions.detail))
async def handle_product_details_buttons(call:CallbackQuery,callback_data:ProductCbData):
    await call.answer()
    message_text=markdown.text(
        markdown.hbold(f"Product №{callback_data.id}"),
        markdown.text(
            markdown.hbold("Price:"),
            callback_data.price
            ,
        ),
        markdown.text(
                markdown.hbold(f"Title: {callback_data.title}")
            ),
        sep="\n"
        
        
    )
    await call.message.edit_text(
        text=message_text,reply_markup=product_details_kb(callback_data)
    )

@router.callback_query(ProductCbData.filter(F.action==ProductionActions.detail))
async def handle_product_details_buttons(call:CallbackQuery,callback_data:ProductCbData):
    await call.answer()
    message_text=markdown.text(
        markdown.hbold(f"Product №{callback_data.id}"),
        markdown.text(
            markdown.hbold("Price:"),
            callback_data.price
            ,
        ),
        markdown.text(
                markdown.hbold(f"Title: {callback_data.title}")
            ),
        sep="\n"
        
        
    )
    await call.message.edit_text(
        text=message_text,reply_markup=product_details_kb(callback_data)
    )

@router.callback_query(ProductCbData.filter(F.action==ProductionActions.update))
async def handle_update_button(call:CallbackQuery,callback_data:ProductCbData):
    await call.message.edit_reply_markup(reply_markup=build_update_keyboard(callback_data))
    await call.answer()
    
    
    