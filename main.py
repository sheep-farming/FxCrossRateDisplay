import xmlrpclib
import os
import time

proxy = xmlrpclib.ServerProxy("http://localhost:2222/")


proxydata = proxy.wsq("USDCNY.FX,EURUSD.FX,USDHKD.FX,EURCNY.FX,EURHKD.FX,HKDCNY.FX","rt_last")
UC = proxydata['Data'][0][0]
CU = 1/UC
EU = proxydata['Data'][0][1]
UE = 1/EU
UH = proxydata['Data'][0][2]
HU = 1/UH
EC = proxydata['Data'][0][3]
CE = 1/EC
EH = proxydata['Data'][0][4]
HE = 1/EH
HC = proxydata['Data'][0][5]
CH = 1/HC

hUC=UC
hCU=CU
hEU=EU
hUE=UE
hUH=UH
hHU=HU
hEC=EC
hCE=CE
hEH=EH
hHE=hEH
hHC=HC
hCH=CH
cR='\x1b[41m'
cG='\x1b[42m'
cW='\x1b[44m'
cUC=int(UC==hUC)*cW+int(UC>hUC)*cR+int(UC<hUC)*cG
cCU=int(CU==hCU)*cW+int(CU>hCU)*cR+int(CU<hCU)*cG
cEU=int(EU==hEU)*cW+int(EU>hEU)*cR+int(EU<hEU)*cG
cUE=int(UE==hUE)*cW+int(UE>hUE)*cR+int(UE<hUE)*cG
cUH=int(UH==hUH)*cW+int(UH>hUH)*cR+int(UH<hUH)*cG
cHU=int(HU==hHU)*cW+int(HU>hHU)*cR+int(HU<hHU)*cG
cEC=int(EC==hEC)*cW+int(EC>hEC)*cR+int(EC<hEC)*cG
cCE=int(CE==hCE)*cW+int(CE>hCE)*cR+int(CE<hCE)*cG
cEH=int(EH==hEH)*cW+int(EH>hEH)*cR+int(EH<hEH)*cG
cHE=int(HE==hHE)*cW+int(HE>hHE)*cR+int(HE<hHE)*cG
cHC=int(HC==hHC)*cW+int(HC>hHC)*cR+int(HC<hHC)*cG
cCH=int(CH==hCH)*cW+int(CH>hCH)*cR+int(CH<hCH)*cG




'''
	USD EUR HKD CNY
USD
EUR
HKD
CNY
'''
sN=' '*6
sUU=cW+'  --  '
while 1:
	proxydata = proxy.wsq("USDCNY.FX,EURUSD.FX,USDHKD.FX,EURCNY.FX,EURHKD.FX,HKDCNY.FX","rt_last")
	UC = proxydata['Data'][0][0]
	CU = 1/UC
	EU = proxydata['Data'][0][1]
	UE = 1/EU
	UH = proxydata['Data'][0][2]
	HU = 1/UH
	EC = proxydata['Data'][0][3]
	CE = 1/EC
	EH = proxydata['Data'][0][4]
	HE = 1/EH
	HC = proxydata['Data'][0][5]
	CH = 1/HC

	cUC=int(UC==hUC)*cW+int(UC>hUC)*cR+int(UC<hUC)*cG
	cCU=int(CU==hCU)*cW+int(CU>hCU)*cR+int(CU<hCU)*cG
	cEU=int(EU==hEU)*cW+int(EU>hEU)*cR+int(EU<hEU)*cG
	cUE=int(UE==hUE)*cW+int(UE>hUE)*cR+int(UE<hUE)*cG
	cUH=int(UH==hUH)*cW+int(UH>hUH)*cR+int(UH<hUH)*cG
	cHU=int(HU==hHU)*cW+int(HU>hHU)*cR+int(HU<hHU)*cG
	cEC=int(EC==hEC)*cW+int(EC>hEC)*cR+int(EC<hEC)*cG
	cCE=int(CE==hCE)*cW+int(CE>hCE)*cR+int(CE<hCE)*cG
	cEH=int(EH==hEH)*cW+int(EH>hEH)*cR+int(EH<hEH)*cG
	cHE=int(HE==hHE)*cW+int(HE>hHE)*cR+int(HE<hHE)*cG
	cHC=int(HC==hHC)*cW+int(HC>hHC)*cR+int(HC<hHC)*cG
	cCH=int(CH==hCH)*cW+int(CH>hCH)*cR+int(CH<hCH)*cG

	sUC=cUC+str(UC)[0:6]+'0'*(6-len(str(UC)))
	sCU=cCU+str(CU)[0:6]+'0'*(6-len(str(CU)))
	sEU=cEU+str(EU)[0:6]+'0'*(6-len(str(EU)))
	sUE=cUE+str(UE)[0:6]+'0'*(6-len(str(UE)))
	sUH=cUH+str(UH)[0:6]+'0'*(6-len(str(UH)))
	sHU=cHU+str(HU)[0:6]+'0'*(6-len(str(HU)))
	sEC=cEC+str(EC)[0:6]+'0'*(6-len(str(EC)))
	sCE=cCE+str(CE)[0:6]+'0'*(6-len(str(CE)))
	sEH=cEH+str(EH)[0:6]+'0'*(6-len(str(EH)))
	sHE=cHE+str(HE)[0:6]+'0'*(6-len(str(HE)))
	sHC=cHC+str(HC)[0:6]+'0'*(6-len(str(HC)))
	sCH=cCH+str(CH)[0:6]+'0'*(6-len(str(CH)))


	os.system('clear')
	print proxydata['Times'][0].value
	print sN, 'USD   ','EUR   ','HKD   ','CNY   '
	print 'USD   ','\x1b[44m'+sUU,sEU,sHU,sCU+'\x1b[0m'
	print 'EUR   ','\x1b[44m'+sUE,sUU,sHE,sCE+'\x1b[0m'
	print 'HKD   ','\x1b[44m'+sUH,sEH,sUU,sCH+'\x1b[0m'
	print 'CNY   ','\x1b[44m'+sUC,sEC,sHC,sUU+'\x1b[0m'

	hUC=UC
	hCU=CU
	hEU=EU
	hUE=UE
	hUH=UH
	hHU=HU
	hEC=EC
	hCE=CE
	hEH=EH
	hHE=HE
	hHC=HC
	hCH=CH

	time.sleep(0.5)


