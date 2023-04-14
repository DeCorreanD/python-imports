from appliances.kitchen import DishWasher, Refrigerator
from appliances.laundry.dryer import Dryer
from appliances.laundry.washer import Washer
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

tuna_can = CanOpener("Gold")
tuna_can.open_can()
 