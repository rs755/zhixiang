houdu = {'bihousw': 10, 'bihoudw': 5, 'yaogaisw': 7, 'yaogaidw': 5, 'dianban': 1, 'neika_geban': 3}  # 厚度
caizhi = {'o': '', 'sws': '180g/120g/100g/120g/160g', 'swc': 'W250g/140g/100/140g/180g', 'dws': 'K230g/H140g/K230g', 'dwc': 'W250g/H140g/K230g'}  # 材质
neika_geban = {'sw': 15, 'dw': 10}


def rounding(num):
    if str(num)[-1] == '1':
        return num - 1
    elif str(num)[-1] == '9':
        return num + 1
    else:
        return num


def calculator(dsw, guanzhijing, guangao, gaigao, guan_heng_c, guan_shu_c, neika_heng_c, neika_shu_c, geban_c, dianban_c, yinshua):
    bihou = houdu['bihou' + dsw]  # 壁厚
    yaogai = houdu['yaogai' + dsw]  # 摇盖厚
    L = (guanzhijing + 1) * guan_heng_c + bihou + 3 + houdu['neika_geban'] * neika_heng_c  #
    W = (guanzhijing + 1) * guan_shu_c + bihou + 3 + houdu['neika_geban'] * (neika_shu_c + geban_c)  #
    H = (guangao + gaigao - 7) + bihou + yaogai + houdu['dianban'] * dianban_c  #

    neibaozhuang = ''
    if neika_heng_c:
        neika_L = rounding(L - neika_geban[dsw])
        neika_W = rounding(W - neika_geban[dsw])
        neika_H = rounding(H - neika_geban[dsw])
        neibaozhuang += '内卡：{}x{}x{}mm'.format(neika_L, neika_W, neika_H)
    if geban_c:
        geban_L = rounding(L - neika_geban[dsw])
        geban_H = rounding(H - neika_geban[dsw])
        neibaozhuang += '隔{}：{}x{}mm'.format(geban_c, geban_L, geban_H)
    if dianban_c:
        dianban_L = rounding(L - neika_geban[dsw])
        dianban_W = rounding(W - neika_geban[dsw])
        neibaozhuang += '垫板：{}x{}mm'.format(dianban_L, dianban_W)
    return "{}\n{}*{}*{}mm\n{}\n{}".format(caizhi[dsw], L, W, H, yinshua, neibaozhuang)
