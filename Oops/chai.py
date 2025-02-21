# print("Chai with Oops"); 

class CarBrand :
  total_car = 0;
  def __init__(self, brand,modal):
    self.__brand = brand
    self.modal = modal;
    CarBrand.total_car += 1

  def get_brand(self):
    return self.__brand + " !"
  
  def fuel_type(self):
    return "Petrol or diesel"
  
  def fullname(self):
    return (f"{self.__brand} {self.modal} ")
  
class Electric_car(CarBrand):
  def __init__(self,brand , modal, battery_size):
    super().__init__ (brand, modal);
    self.battery_size  = battery_size
  def fullInfo(self):
    return (f"name: {self.brand}, modal : {self.modal} , Size of battery : {self.battery_size} ")
  
  # def fuel_type(self):
    # return "Electric charge "
  


electic_car = Electric_car("tesla", "Modal S" , "4022mh")
# print(electic_car.get_brand());

safari = CarBrand("tata", "sarafi");
# print(safari.fuel_type());
# print(electic_car.fuel_type());

# print(electic_car.__brand);

# print(electic_car.fullInfo()); 
my_car = CarBrand("Toyota" , "Nexon");
# print(my_car.fullname());   



print(CarBrand.total_car)
