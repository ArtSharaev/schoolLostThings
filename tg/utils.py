from aiogram.utils.helper import Helper, HelperMode, ListItem


class States(Helper):
    mode = HelperMode.snake_case

    STATE1_GET_BUILDING = ListItem()
    STATE2_GET_ROOM = ListItem()


if __name__ == '__main__':
    print(f'States list: {States.all()}')