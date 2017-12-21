import os
import time
test_list = [1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7,
             8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8,
             1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, 1, 2, 4, 5, 6, 7,
             8, 9, 7, 8, 1, 2, 4, 5, 6, 7, 8, 9, 7, 8, ]
#一共有110个数，以50为单位进行处理，


def calculate_query_order_num():
    result = ModelOrderWithdraw().find_pending_withdraw_order()#首先找到所有的订单数
    if len(result) <= 50:
        order_list = ",".join([i.withdraw_order_no for i in result])#如果数量<=50,那么就直接进行查询，
        fuyou_search_withdraw_result(order_list)
    else:
        #数量大于50
        division, subplus_num = divmod(len(result), 50)#得到除以50的商和余数
        count = division+1 if subplus_num != 0 else division
        for i in range(count):
            query_data = result[50*i:50*(i+1)]
            order_list = ",".join(query_data)
            fuyou_search_withdraw_result(order_list)
            time.sleep(300)

def fuyou_search_withdraw_result(order_list):
    pass


