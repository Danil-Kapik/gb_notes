from core.controller import Controller
from core.model import Model
from core.veiw import View


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.run()


if __name__ == "__main__":
    main()
