import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import time

UnityApp = "Unity 2018.3.6f1 Personal - RoboSub2019.unity - TransdecEnvironment_3 - PC, Mac & Linux Standalone <DX11>";
image_num = 0

def get_fps_delay(fps):
	return 1/fps;

# Wyszukanie nazwy aplikacji Unity dla win32gui
def get_all_apps():
	toplist, winlist = [], []
	def enum_cb(hwnd, results):
	    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
	win32gui.EnumWindows(enum_cb, toplist)
	print(winlist) #Aby wyszukac aplikacji Unity


def get_screenshot(save_screenshot = False):
	global image_num
	hwnd = win32gui.FindWindow(None, UnityApp)
	#print("haloA")
	#print(hwnd)

	# Change the line below depending on whether you want the whole window
	# or just the client area. 
	#left, top, right, bot = win32gui.GetClientRect(hwnd)
	left, top, right, bot = win32gui.GetWindowRect(hwnd)
	w = right - left
	h = bot - top
	#print("haloB")
	hwndDC = win32gui.GetWindowDC(hwnd)
	mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
	saveDC = mfcDC.CreateCompatibleDC()

	saveBitMap = win32ui.CreateBitmap()
	saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
	#print("haloC")
	saveDC.SelectObject(saveBitMap)
	#print("haloD")

	# Change the line below depending on whether you want the whole window
	# or just the client area. 
	#result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
	result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
	#print(result)
	#print("haloD")
	bmpinfo = saveBitMap.GetInfo()
	bmpstr = saveBitMap.GetBitmapBits(True)

	w = 1280
	h = 720
	area = (328, 273, 1608, 993)
	#area = (159, 117, 1439, 837)
	area = (168, 123, 168 + w, 123 + h)
	im = Image.frombuffer(
	    'RGB',
	    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
	    bmpstr, 'raw', 'BGRX', 0, 1)

	im = im.crop(area)
	#print("haloE")
	win32gui.DeleteObject(saveBitMap.GetHandle())
	saveDC.DeleteDC()
	mfcDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, hwndDC)

	if result == 1 and save_screenshot:
	    im.save("test{0}.png".format(image_num))
	    image_num += 1

	return im


if __name__ == '__main__':
	get_all_apps()
	
	while True:
		time.sleep(get_fps_delay(60))
		im = get_screenshot(True)
	