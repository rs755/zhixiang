houdu_dict = {'bihousw': 10, 'bihoudw': 5, 'yaogaisw': 7, 'yaogaidw': 5, 'dianban': 1, 'neika_geban': 3}  # 厚度
caizhi_dict = {'o': '', 'sw水墨印': '180g/120g/100g/120g/160g', 'sw彩印': 'W250g/140g/100/140g/180g', 'dw水墨印': 'K230g/H140g/K230g', 'dw彩印': 'W250g/H140g/K230g'}  # 材质
neika_geban_chicun = {'sw': 15, 'dw': 10}  # 纸箱尺寸要减去的量


def rounding(num):
    if str(num)[-1] == '1':
        return num - 1
    elif str(num)[-1] == '9':
        return num + 1
    else:
        return num


def calculator(guanzhijing, guanzonggao, dsw, guan_paibu, yinshua, neika_geban, dianban_c):
    bihou = houdu_dict['bihou' + dsw]  # 壁厚
    yaogai = houdu_dict['yaogai' + dsw]  # 摇盖厚
    if yinshua != '水墨印' and yinshua != '彩印':
        caizhi = 'o'
    else:
        caizhi = dsw + yinshua
    if neika_geban == 'neika':
        neika_paibu = [guan_paibu[0]-1, guan_paibu[1]-1]
        geban_c = 0
    elif neika_geban == 'geban':
        neika_paibu = [0, 0]
        geban_c = guan_paibu[1]-1
    else:
        neika_paibu = [0, 0]
        geban_c = 0
    L = (guanzhijing + 1) * guan_paibu[0] + bihou + 3 + houdu_dict['neika_geban'] * neika_paibu[0]
    W = (guanzhijing + 1) * guan_paibu[1] + bihou + 3 + houdu_dict['neika_geban'] * (neika_paibu[1] + geban_c)
    H = guanzonggao + bihou + yaogai + houdu_dict['dianban'] * dianban_c

    neibaozhuang = ''
    if neika_paibu[0]:
        neika_L = rounding(L - neika_geban_chicun[dsw])
        neika_W = rounding(W - neika_geban_chicun[dsw])
        neika_H = rounding(H - neika_geban_chicun[dsw])
        neibaozhuang += '内卡：{}x{}x{}mm'.format(neika_L, neika_W, neika_H)
    if geban_c:
        geban_L = rounding(L - neika_geban_chicun[dsw])
        geban_H = rounding(H - neika_geban_chicun[dsw])
        neibaozhuang += '隔{}：{}x{}mm'.format(geban_c, geban_L, geban_H)
    if dianban_c:
        dianban_L = rounding(L - neika_geban_chicun[dsw])
        dianban_W = rounding(W - neika_geban_chicun[dsw])
        neibaozhuang += '垫板：{}x{}mm'.format(dianban_L, dianban_W)
    return "{}\n{}*{}*{}mm\n{}\n{}".format(caizhi_dict[caizhi], L, W, H, yinshua, neibaozhuang)
