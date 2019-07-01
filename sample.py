import win32com.client

objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS CONNECTION ERROR")
else:
	print("PLUS CONNECTION SUCCESS")

exit()