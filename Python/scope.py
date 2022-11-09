# Global scope
price = 100


def increment():
    # Local scope. Las variables no pueden leerse por un contexto exterior al actual
    price = price + 10
    print(price)


print(price)
increment()
