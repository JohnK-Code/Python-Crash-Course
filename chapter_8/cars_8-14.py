#### TRY IT YOURSELF - Chapter 8 - Cars
def car_info(make, model, **info):
    """Summarize the details of a car."""
    info['make'] = make.title()
    info['model'] = model.title()
    return info
car_spec = car_info('ford', 'fiesta', color='gray', tow_package=False)
print(car_spec)


#### Alternative version that creates its own 'dictionary' in the function and add the 'key-value' pairs to it
def car_info2(make, model, **info):
    """Summarize the details of a car."""
    car_dict = {
        'Make': make.title(),
        'Model': model.title()
    }
    for key, value in info.items():
        car_dict[key.title()] = value.title()
    return car_dict
car_spec2 = car_info2('honda', 'civic', color='blue', engine_size='1.4l')
print(car_spec2)