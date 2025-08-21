from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    COMPANY_ID_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_company_id")
    USERNAME_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_username")
    PASSWORD_INPUT = (AppiumBy.ID, "id.edot.ework:id/tv_password")
    LOGIN_BUTTON = (AppiumBy.ID, "id.edot.ework:id/button_text")
    ERROR_MESSAGE = (AppiumBy.ID, "id.edot.ework:id/textView")
    OK_ERROR = (AppiumBy.ID, "id.edot.ework:id/button_text")
    CLOSE_ERROR = (AppiumBy.ID, "id.edot.ework:id/btn_x")
    SUCCESS_LOGIN = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.GridView/android.view.ViewGroup[5]/android.widget.TextView")
    NEW_CUSTOMER = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.GridView/android.view.ViewGroup[5]")


