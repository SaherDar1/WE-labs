from .resources import AddUser, UpdateUser,SearchUser,TakeOrder,AddMenu,UpdateMenu,SearchPizza


def initialize_routes(api):
    api.add_resource(AddUser, '/api1')
    api.add_resource(UpdateUser, '/api2/<username>')
    api.add_resource(SearchUser, '/api3')

    api.add_resource(TakeOrder, '/api4')
    api.add_resource(AddMenu, '/api5')
    api.add_resource(UpdateMenu,'/api6/<pizzaName>')
    api.add_resource(SearchPizza, '/api7')