import win32file
import win32con
import pywintypes
import datetime

class DateSetter:
    def setTime(self, filename, date_tuple):
        (day, month, year) = date_tuple
        generated_time = datetime.datetime(year, month, day)
        target_time = pywintypes.Time(generated_time)

        winfile = win32file.CreateFile(filename,
                                       win32con.GENERIC_WRITE,
                                       win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
                                       None,
                                       win32con.OPEN_EXISTING,
                                       win32con.FILE_ATTRIBUTE_NORMAL,
                                       None)

        win32file.SetFileTime(winfile, target_time, None, None)
        winfile.close()
