from LamdaAutomation.Library import uiLibrary
import time
obj = uiLibrary.uiLibrary()

class contactLibraryUi():
    def __init__(self):
        pass

    def launchContactUi(self):
        obj.clickBytext("Contacts")


    def clickByPlus(self):
        obj.clickByPlus()
    def fullname(self):
        obj.fullName("Full name")

    def pressBackUi(self):
        obj.pressBack()






    # def newNameCreate(self):
    #     obj(resourceId="com.android.dialer:id/menu_add").click()
    #     time.sleep(2)
    #     # Enter First Name
    #     obj(text="Full name").click()
    #     subprocess.run("adb shell input text Android", shell=True)
    #     obj.press.down()
    #     time.sleep(3)
    #     # Enter phoneNumber
    #     d(className="android.widget.EditText", instance=3).click()
    #     subprocess.run("adb shell input text 12345", shell=True)
    #     time.sleep(2)
    #     obj.press.back()
    #     # Click Save
    #     obj(text="Done").click()
    #     time.sleep(2)
