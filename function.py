houdu_dict = {'bihousw': 10, 'bihoudw': 5, 'yaogaisw': 7, 'yaogaidw': 5, 'dianban': 1, 'neika_geban': 3}  # 厚度
caizhi_dict = {'o': '', 'sws': '180g/120g/100g/120g/160g', 'swc': 'W250g/140g/100/140g/180g', 'dws': 'K230g/H140g/K230g', 'dwc': 'W250g/H140g/K230g'}  # 材质
neika_geban = {'sw': 15, 'dw': 10}  # 纸箱尺寸要减去的量


def rounding(num):
    if str(num)[-1] == '1':
        return num - 1
    elif str(num)[-1] == '9':
        return num + 1
    else:
        return num


def calculator(dsw, guanzhijing, guanzonggao, guan_paibu, neika_paibu, geban_c, dianban_c, yinshua, caizhi):
    bihou = houdu_dict['bihou' + dsw]  # 壁厚
    yaogai = houdu_dict['yaogai' + dsw]  # 摇盖厚
    L = (guanzhijing + 1) * guan_paibu[0] + bihou + 3 + houdu_dict['neika_geban'] * neika_paibu[0]
    W = (guanzhijing + 1) * guan_paibu[1] + bihou + 3 + houdu_dict['neika_geban'] * (neika_paibu[1] + geban_c)
    H = guanzonggao + bihou + yaogai + houdu_dict['dianban'] * dianban_c

    neibaozhuang = '"'
    if neika_paibu[0]:
        neika_L = rounding(L - neika_geban[dsw])
        neika_W = rounding(W - neika_geban[dsw])
        neika_H = rounding(H - neika_geban[dsw])
        neibaozhuang += '内卡：{}x{}x{}mm\n'.format(neika_L, neika_W, neika_H)
    if geban_c:
        geban_L = rounding(L - neika_geban[dsw])
        geban_H = rounding(H - neika_geban[dsw])
        neibaozhuang += '隔{}：{}x{}mm'.format(geban_c, geban_L, geban_H)
    if dianban_c:
        dianban_L = rounding(L - neika_geban[dsw])
        dianban_W = rounding(W - neika_geban[dsw])
        neibaozhuang += '垫板：{}x{}mm'.format(dianban_L, dianban_W)
    neibaozhuang += '"'
    return "{}\n{}*{}*{}mm\n{}\n{}".format(caizhi_dict[caizhi], L, W, H, yinshua, neibaozhuang)
