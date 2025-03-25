from ProtectedDictInt import ProtectedDictInt


def debug_protected_dict():
    try:
        d = ProtectedDictInt()
        print("Adding key 1 with value 2")
        d[1] = 2
        print("Current dictionary:", d)

        print("Trying to add key 1 again (should raise PermissionError)")
        try:
            d[1] = 3
        except PermissionError:
            print("Caught expected PermissionError")

        print("Trying to access key 1:", d[1])
        print("Trying to access a non-existent key (should raise KeyError)")
        try:
            print(d[2])
        except KeyError:
            print("Caught expected KeyError")

        print("Adding a tuple (3, 'three') using + operator")
        d = d + (3, "three")
        print("Current dictionary:", d)

        print("Removing key 1 using - operator")
        d = d - 1
        print("Current dictionary:", d)

        print("Trying to remove non-existent key (should raise KeyError)")
        try:
            d = d - 10
        except KeyError:
            print("Caught expected KeyError")

        print("Checking if key 3 is in dictionary:", 3 in d)
        print("Checking length of dictionary:", len(d))

        print("Deleting key 3 using del operator")
        del d[3]
        print("Current dictionary:", d)

        print("Trying to delete non-existent key (should raise KeyError)")
        try:
            del d[3]
        except KeyError:
            print("Caught expected KeyError")

        print("Summing all keys using call method:", d())

    except ValueError as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    debug_protected_dict()
