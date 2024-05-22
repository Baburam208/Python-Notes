# main.py

def main():

    #### Working with module ####
    print(f"Working with module")

    import mymodule

    print(mymodule.greet("KUcians"))


    print("="*30)

    #### Working with Package ####
    print(f"Working with Package")

    import mypackage

    print(mypackage.greet("new batch"))
    print(mypackage.display_numbers())
    print(mypackage.pick_vowels("KUcians"))

    print("="*30)

    print(f"Working with library")

    import mylibrary as mlib

    # Math utils
    print(mlib.square(3))
    print(mlib.divide(4, 2))

    try:
        print(mlib.divide(2, 0))
    except ValueError as e:
        print(e)     

    # string utils
    print(mlib.uppercase('kuaic'))
    print(mlib.is_palindrome('kuaic'))
    print(mlib.is_palindrome('acca'))

if __name__ == '__main__':
    main()