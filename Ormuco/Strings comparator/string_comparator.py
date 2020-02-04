from comparator import String_comparator


def test(strings: String_comparator):
    """
     This function is for testing all valid cases, it checks if passed arguments are valid as well
    Params:
    string_comparator: String_comparator object
    """
    try:
        strings.check_strings()
        return strings.compare()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    #With int numbers
    print("Case with int numbers")
    s1 = 123
    s2 = 12324312412
    obj = String_comparator(s1, s2)
    print(test(obj))

    print("Case with NoneType string")
    #with NoneType string
    s1 = None
    s2 = 12324312412
    obj = String_comparator(s1, s2)
    test(obj)

    print("Case with two strings")
    #with two strings
    s1 = "21312312312"
    s2 = "sadasdasdsads"
    obj = String_comparator(s1, s2)
    print(test(obj))

    print("Case with one string and an int or float number")
    #with one string and an int or float number
    s1 = "21312312312"
    s2 = 2131231293012903129039120390129302193012
    obj = String_comparator(s1, s2)
    print(test(obj))

    s1 = "21312312312"
    s2 = 2.3
    obj = String_comparator(s1, s2)
    print(test(obj))

    s1 = "HEY !!"
    s2 = 2.3
    obj = String_comparator(s1, s2)
    print(test(obj))

    print("Case with empty strings")
    #with empty strings
    s1 = ""
    s2 = -2.3
    obj = String_comparator(s1, s2)
    print(test(obj))

    s1 = ""
    s2 = ""
    obj = String_comparator(s1, s2)
    print(test(obj))

    print("Case with negative and positive int or float numbers")
    s1 = +2132132
    s2 = -2131234768
    obj = String_comparator(s1, s2)
    print(test(obj))

    s1 = +2.2321
    s2 = -90.4532
    obj = String_comparator(s1, s2)
    print(test(obj))

    s1 = -2.2321
    s2 = +90.4532
    obj = String_comparator(s1, s2)
    print(test(obj))


  