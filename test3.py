import os, sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
from slacker import Slacker
import time, calendar


# 크레온 플러스 공통 OBJECT
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpStock = win32com.client.Dispatch('DsCbo1.StockMst')
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311')  



print("cpCodeMgr: ", cpCodeMgr.CodeToName("A051910"))      # 종목 이름 - 110(get_stock_balance(code))

print("cpStatus1: ", cpStatus.IsConnect)                   # (크레온 플러스)연결 여부 체크 - 40(check_creon_system())
print("cpStatus2: ", cpStatus.LimitRequestRemainTime)      # remain_time?? - 199(buy_etf(code)), 241(sell_all())

print("cpTradeUtil1: ", cpTradeUtil.TradeInit(0))           # X 주문 관련 초기화?? - 45(check_creon_system()), 82(get_stock_balance(code)), 115(get_current_cash()), 183(buy_etf(code)), 217(sell_all())
print("cpTradeUtil2: ", cpTradeUtil.AccountNumber[0])       # 계좌 번호 - 83(get_stock_balance(code)), 116(get_current_cash()), 184(buy_etf(code)), 218(sell_all())
print("cpTradeUtil3: ", cpTradeUtil.GoodsList(cpTradeUtil.AccountNumber[0], 1))            # -1:전체, 1:주식, 2:선물/옵션 - 84(get_stock_balance(code)), 117(get_current_cash()), 185(buy_etf(code)), 219(sell_all())

print("cpStock1: ", cpStock.SetInputValue(0, "A051910"))        # 종목코드에 대한 가격 정보 - 52(get_current_price(code))
print("cpStock2: ", cpStock.BlockRequest())                # ?? - 53(get_current_price(code))
print("cpStock3: ", cpStock.GetHeaderValue(11))            # 현재가 - 54(get_current_price(code))
print("cpStock4: ", cpStock.GetHeaderValue(16))            # 매수호가 - 55(get_current_price(code))
print("cpStock5: ", cpStock.GetHeaderValue(17))            # 매도호가 - 56(get_current_price(code))

# 이 밑으로 그냥 돌리면 에러남
# print("cpOhlc1: ", cpOhlc.SetInputValue(0, "A051910"))           # 종목코드 - 62(get_ohlc(code, qty))
# print("cpOhlc2: ", cpOhlc.SetInputValue(1, ord('2'))        # 1:기간, 2:개수 - 63(get_ohlc(code, qty))
# print("cpOhlc3: ", cpOhlc.SetInputValue(4, qty)             # 요청개수 - 64(get_ohlc(code, qty))
# print("cpOhlc4: ", cpOhlc.SetInputValue(5, [0, 2, 3, 4, 5]) # 0:날짜, 2~5:OHLC - 65(get_ohlc(code, qty))
# print("cpOhlc5: ", cpOhlc.SetInputValue(6, ord('D'))        # D:일단위 - 66(get_ohlc(code, qty))
# print("cpOhlc6: ", cpOhlc.SetInputValue(9, ord('1'))        # 0:무수정주가, 1:수정주가 - 67(get_ohlc(code, qty))
# print("cpOhlc7: ", cpOhlc.BlockRequest())                   # ?? - 68(get_ohlc(code, qty))
# print("cpOhlc8: ", cpOhlc.GetHeaderValue(3))                # 3:수신개수 - 69(get_ohlc(code, qty))


# count = cpOhlc.GetHeaderValue(3)   # 3:수신개수

# for i in range(count): 
#     index.append(cpOhlc.GetDataValue(0, i)) 
#     rows.append([cpOhlc.GetDataValue(1, i), cpOhlc.GetDataValue(2, i),
#         cpOhlc.GetDataValue(3, i), cpOhlc.GetDataValue(4, i)]) 
# df = pd.DataFrame(rows, columns=columns, index=index) 
# return df
# print("cpOhlc8: ", cpOhlc.GetDataValue(0, i))                # ?? - 74(get_ohlc(code, qty))
# print("cpOhlc8: ", cpOhlc.GetDataValue(1, i))                # ?? - 75(get_ohlc(code, qty))
# print("cpOhlc8: ", cpOhlc.GetDataValue(2, i))                # ?? - 75(get_ohlc(code, qty))
# print("cpOhlc8: ", cpOhlc.GetDataValue(3, i))                # ?? - 76(get_ohlc(code, qty))
# print("cpOhlc8: ", cpOhlc.GetDataValue(4, i))                # ?? - 76(get_ohlc(code, qty))

# print("cpBalance", )                #
# 80: def get_stock_balance(code):
    # cpTradeUtil.TradeInit()
    # acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
    # accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    # cpBalance.SetInputValue(0, acc)         # 계좌번호
    # cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    # cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
    # cpBalance.BlockRequest()     

# print("cpCash", )
# 113: def get_current_cash():
cpTradeUtil.TradeInit()
acc = cpTradeUtil.AccountNumber[0]    # 계좌번호
accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
cpCash.SetInputValue(0, acc)              # 계좌번호
cpCash.SetInputValue(1, accFlag[0])      # 상품구분 - 주식 상품 중 첫번째
cpCash.BlockRequest() 
# return cpCash.GetHeaderValue(9) # 증거금 100% 주문 가능 금액
print("cpCash: ", cpCash.GetHeaderValue(9))     # 잔고 - 122(get_current_cash())

# cpOrder ...
cpOrder.SetInputValue(0, "2")        # 2: 매수
cpOrder.SetInputValue(1, cpTradeUtil.AccountNumber[0])        # 계좌번호
cpOrder.SetInputValue(2, cpTradeUtil.GoodsList(acc, 1)[0]) # 상품구분 - 주식 상품 중 첫번째
cpOrder.SetInputValue(3, "A051910")       # 종목코드
cpOrder.SetInputValue(4, 0)    # 매수할 수량
cpOrder.SetInputValue(7, "2")        # 주문조건 0:기본, 1:IOC, 2:FOK
cpOrder.SetInputValue(8, "12")       # 주문호가 1:보통, 3:시장가
                                        # 5:조건부, 12:최유리, 13:최우선 
# 매수 주문 요청
ret = cpOrder.BlockRequest() 
print("cpOrder: ", ret)


def get_current_cash():
    """증거금 100% 주문 가능 금액을 반환한다."""
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]    # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    cpCash.SetInputValue(0, acc)              # 계좌번호
    cpCash.SetInputValue(1, accFlag[0])      # 상품구분 - 주식 상품 중 첫번째
    cpCash.BlockRequest() 
    return cpCash.GetHeaderValue(9) # 증거금 100% 주문 가능 금액

print(int(get_current_cash()))