import functions as f


def main():
    f.get_requirements()
    list_size = f.user_input()
    f.using_lists(list_size)


if __name__ == "__main__":
    main()