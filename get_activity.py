# import the required tools
from ADB_Action_Scipt import ActionScript
from RC_Code import SonyRCKey
from AppList import AppList

# create an instance of the class, variables can be change
tv = ActionScript()
rc = SonyRCKey()
app = AppList()

# Script Instructions
print("This will try to get the MainActivity of an app")
tv.get_activity_mfocus()

# ----------------------- Keep terminal open -----------------------------
close = input("Press Enter to close terminal")
