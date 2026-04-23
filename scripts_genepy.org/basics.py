# def testfunction(a,b):
#     return a+b
# print(testfunction(2,3))


# def is_dog(animal):
#     if animal == "dog":
#         return "is a dog!"
#     else: 
#         return "is another type of animal!"
# print(is_dog("dog"))


# def looping(array):
#     new = [888]
#     for a in array:            
#         new = new + [a]
#     return new
# print(looping([1,2,4]))


# def looping_if(array):
#     new = []
#     for a in array:            
#         if type(a) == float:
#             new = new + [a]
#     return new
# print(looping_if([1,2.9,4]))


# json_log = {
#     "name": "dnt",
#     "age": 888,
#     "country": "DE",
#     "status": "ERROR"
# }
# def log_parser(json):
#     return json["status"]
# print(log_parser(json_log))


json_log = [{
    "name": "dnt",
    "age": 888,
    "country": "DE",
    "status": "ERROR"
},{
    "name": "do0",
    "age": 555,
    "country": "DE",
    "status": "GOOD"
},{
    "name": "text",
    "age": 999,
    "country": "DE",
    "status": "ERROR"
}]
def log_filter(json):
    return json["status"]
print(log_filter(json_log))


# next challenge "classes"
#  class cat: 