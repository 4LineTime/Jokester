import database.database as db
import view


def main():
    db.connect_db()
    view.view_controller()

    



if __name__ == '__main__':
    main()