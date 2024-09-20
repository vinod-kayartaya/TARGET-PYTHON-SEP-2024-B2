class Phone:
    def __init__(self) -> None:
        super().__init__()
        print('Phone.__init__() called')

class MobilePhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        print('MobilePhone.__init__() called')

    def f1(self):
        print('MobilePhone.f1() called')

class Camera:
    def __init__(self) -> None:
        super().__init__()
        print('Camera.__init__() called')

    def f1(self):
        print('Camera.f1() called')

class CameraPhone(Camera, MobilePhone):
    def __init__(self) -> None:
        super().__init__()
        print('CameraPhone.__init__() called')

def main():
    cp = CameraPhone()
    print(f'{CameraPhone.mro() = }')

    cp.f1()
    Camera.f1(cp)
    MobilePhone.f1(cp)


if __name__ == '__main__':
    main()
    

