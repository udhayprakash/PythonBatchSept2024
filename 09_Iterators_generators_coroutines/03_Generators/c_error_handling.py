def my_gen():
    try:
        yield "value" + 8
    except (ValueError, TypeError):
        yield "Handling Exception"
    finally:
        print("cleaning up")


x = my_gen()

next(x)

e = ValueError("some error")

print(x.throw(e))  # "Handling Exception"
print(x.close())  # Cleaning Up


# python -i 08_error_handling.py 