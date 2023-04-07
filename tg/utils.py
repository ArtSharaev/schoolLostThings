from aiogram.utils.helper import Helper, HelperMode, ListItem


class UserStates(Helper):
    mode = HelperMode.snake_case

    STATE1_GET_BUILDING = ListItem()
    STATE2_GET_ROOM = ListItem()
    STATE3_GET_PHOTO = ListItem()


class AdminStates(Helper):
    mode = HelperMode.snake_case

    ADMIN_GET_BUILDING = ListItem()
    ADMIN_GET_PHOTO_TO_DELETE = ListItem()


if __name__ == '__main__':
    print(f'UserStates list: {UserStates.all()}')
    print(f'AdminStates list: {AdminStates.all()}')
