class ConvertionError(Exception):
    """

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, convertable):
        self.convertable = convertable
        self.message = f'{convertable}, cant be converted using this approach!'
        super().__init__(self.message)


def convert_anything(anything):
    res = 0
    try:
        res = float(anything)
    except:
        print(f'{anything} failed to convert to float')
        raise ConvertionError(anything)

    return res


if __name__ == "__main__":

    a = 3
    b = [1, 0, 2, '222', 'K']
    c = {el: el for el in b}

    for elem in c.items():
        elem = elem[0]

        try:
            elem = convert_anything(elem)

            reslt = a / elem
            # # result1 = a + elem
            # reslt = 1 > elem

        except ConvertionError as err:
            print(type(err))
            print(err)
            continue

        except TypeError as err:
            print(type(err))
            print(err)
            continue

        except Exception as err:
            print(type(err))
            print(err)
            continue

        print(f"Result is: {reslt}")

