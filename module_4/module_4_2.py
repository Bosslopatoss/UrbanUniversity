def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
#inner_function() - нельзя вызвать фунуцию 'inner_function()' вне функции 
#'test_function()', т.к она является локальной для функции 'test_function()' 
#и к ней нельзя обращаться из глобальной области видимости 
test_function()