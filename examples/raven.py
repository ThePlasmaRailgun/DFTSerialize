from decimal import Decimal as d


def w(h):
    return (h > 0) - (h < 0) or 1


def f(p):
    if p < 1:
        return 1
    else:
        return p * f(p - 1)


def u(s):
    z = d(0)
    for k in range(s):
        z += (d(-1) ** k) * (
                d(f(6 * k)) / ((f(k) ** 3) * (f(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
    return float((z * d(10005).sqrt() / 4270934400) ** (-1))


g = u(5)


def r(h):
    if h > 1 or h < -1:
        return -r(1 / h) + w(h) * g / 2
    elif h == 1 or h == -1:
        return g / 4

    j = 0
    for r in range(80):
        j += (-1) ** r * (h ** (2 * r + 1)) / (2 * r + 1)
    return j


a = [r(2 ** (-i)) for i in range(30)]


def s(n):
    if n < -g / 2 or n > g / 2:
        if n < 0:
            x, y = s(n + g)
        else:
            x, y = s(n - g)
        return -x, -y

    x, y = 1, 0

    for i in range(0, 30):
        d = 1.0 * w(n)

        u, v = x, y

        x = u - (d * (2 ** (-i)) * v)
        y = (d * (2 ** (-i)) * u) + v

        n = n - (d * a[i])

    return 0.6072529350088814 * x, 0.6072529350088814 * y


def o(h, e):
    x, y = h
    u, v = e

    return (x * u - y * v), (x * v + y * u)


def k(p):
    q = 2 ** p[0]
    h, e = s(p[1])

    return h * q, e * q


def dark_magic():
    return [print(chr(int(round(sum(x[0] for x in [o(c[a], k(o([0, 2], [3.14159265358979 * a * n / len(c), 0])))
                              for a in range(len(c))]) / len(c)))), end="") for n in range(l)]

c, l = [(35474.0, 0.0),
        (-2012.5213556620856, 9916.056213934444),
        (2983.89537182944, 1322.9114852689763),
        (-8277.856182380849, 11733.502931162746),
        (-10712.097574328858, -10441.427272724864),
        (3969.1170949350626, -2314.1488082497153),
        (-3454.2528182131923, -8319.416741175779),
        (15696.88599416638, -2713.3800097567896),
        (-167.66399188611285, 11372.894673233886),
        (1397.4105064284618, 544.372654022818),
        (-5451.176395183905, 12264.354350579624),
        (-12310.641684993128, -8713.58452366106),
        (4082.3619856200876, -4372.280632541844),
        (-4095.2782685356615, -6835.480153293483),
        (14359.245307715082, -5207.665456509678),
        (1829.8337492207222, 12004.76796964954),
        (563.3746871947797, -549.8595302681947),
        (-2809.5580308393114, 12982.440969886762),
        (-14509.238255123353, -6661.27289139767),
        (4851.648391633938, -6433.757459237097),
        (-3982.1710145265693, -4810.789706591455),
        (12870.637608321738, -7324.30651394549),
        (4651.81489984798, 12124.518590686),
        (-906.5650334157256, 267.76170533267805),
        (-546.4259305437754, 11567.539213505996),
        (-15567.107837098065, -4627.781732083476),
        (3932.9412916873243, -7892.160066149544),
        (-4259.980012759549, -4076.074350713425),
        (10645.185962349307, -9815.596213704079),
        (6441.735432385034, 12237.620951121193),
        (-3064.3126279520893, 448.89267214549284),
        (1595.7817063596053, 10171.768312298916),
        (-16426.24780350193, -1333.452699074459),
        (2662.3252592534327, -9431.50297506264),
        (-3307.3884760306964, -1743.7713323916894),
        (8843.225934805809, -11705.644188136852),
        (9136.912197351663, 11203.408598182865),
        (-3826.1257465935137, 1245.1037633261485),
        (3026.883425393842, 9129.218224164695),
        (-15950.271464198495, 1818.4229767358283),
        (1592.727712743112, -11468.556146798246),
        (-2567.806004020547, -860.8536154158428),
        (6328.9316515939245, -11864.920645667817),
        (11617.86401975607, 9976.959558322314),
        (-4543.633052754171, 3245.2629056249707),
        (4206.726423574073, 7309.802279712022),
        (-15527.68503335601, 4144.962932685856),
        (-929.1368962054021, -12024.438364644098),
        (-897.8866676444625, -528.0918933916281),
        (4623.2935633704965, -12272.169867954779),
        (13599.301635735794, 8188.891904400147),
        (-3727.0275811005517, 5191.286135133005),
        (4928.370630702418, 6059.764912538831),
        (-14455.35761233635, 6959.504626012196),
        (-2679.253018220056, -12257.430161248723),
        (-232.8897783039356, -799.466986414021),
        (1759.7518808628738, -12095.979912665138),
        (15258.41797378724, 5482.506621765771),
        (-4399.2854159542485, 6800.209026176593),
        (3779.8497881856165, 3973.70023861943),
        (-12613.782095295484, 9060.196613958018),
        (-5409.688624600672, -12755.21618528559),
        (1831.067266309987, -235.6027040042195),
        (-283.9124973174697, -11521.283601692952),
        (16053.744266669266, 3141.5661172905675),
        (-3273.4761385933602, 8207.676949065497),
        (4285.493968404341, 2708.52002493872),
        (-10184.541576754722, 10922.861975311127),
        (-8178.206532233202, -12154.192044215892),
        (2423.855310863728, -1769.6416477262032),
        (-1930.634543220146, -9748.521338499733),
        (16619.0, -83.13843876330793),
        (-2297.2069314712517, 10155.998959601155),
        (3335.5157070316727, 827.7519640453098),
        (-7972.876404687977, 11592.11433716904),
        (-9765.384130516477, -11213.391141488642),
        (3465.6137021760487, -1598.799599349676),
        (-2985.1168481812124, -8568.139049698902),
        (15885.97203174244, -3154.4197282587966),
        (-43.425498268735055, 11379.631480994227),
        (1921.9736351644333, 819.4244148306425),
        (-5522.428342174251, 12669.421902915114),
        (-12762.607240747571, -9039.632444658953),
        (4660.449016486051, -4662.375597571247),
        (-4405.0431654632475, -7012.00925212871),
        (15100.667092135487, -5707.130237618443),
        (1999.1815358615495, 12850.94393531786),
        (108.26160442826614, -103.54915830621144),
        (-3510.797949583496, 12488.382655901727),
        (-15073.250379310452, -6292.4981718735535),
        (4373.299521381889, -6168.810326446627),
        (-4565.796252656774, -5106.1279460122805),
        (13516.585677244624, -7941.581548209389),
        (4878.485735828061, 12524.632501271448),
        (-1080.955130013287, 308.69630708050545),
        (-535.1194355650787, 11998.107521001803),
        (-16224.179285946548, -4439.487134432164),
        (3416.2290759112557, -7334.30742712834),
        (-3907.156949086033, -2952.3469906611645),
        (11453.979330956789, -9852.742699856899),
        (6857.0894943503245, 12081.935961446152),
        (-2297.5426577287494, 749.7649376518661),
        (1070.6130991505627, 11099.613620819398),
        (-15781.63621775747, -1812.2362500510126),
        (3177.483111938547, -9550.15534782862),
        (-3418.076951586331, -1949.054070703683),
        (9477.171071575942, -11286.3743270996),
        (9477.171071575945, 11286.374327099595),
        (-3418.076951586331, 1949.054070703683),
        (3177.4831119385467, 9550.15534782862),
        (-15781.636217757472, 1812.2362500510162),
        (1070.6130991505627, -11099.613620819398),
        (-2297.54265772875, -749.7649376518661),
        (6857.0894943503245, -12081.935961446152),
        (11453.979330956789, 9852.742699856899),
        (-3907.156949086033, 2952.3469906611626),
        (3416.229075911257, 7334.30742712834),
        (-16224.179285946548, 4439.487134432164),
        (-535.1194355650812, -11998.107521001799),
        (-1080.955130013289, -308.69630708050954),
        (4878.485735828061, -12524.632501271448),
        (13516.58567724462, 7941.581548209389),
        (-4565.796252656777, 5106.127946012282),
        (4373.299521381889, 6168.810326446627),
        (-15073.250379310448, 6292.498171873554),
        (-3510.797949583496, -12488.382655901725),
        (108.26160442826614, 103.54915830621144),
        (1999.1815358615504, -12850.943935317862),
        (15100.667092135489, 5707.13023761844),
        (-4405.0431654632475, 7012.00925212871),
        (4660.449016486049, 4662.3755975712465),
        (-12762.607240747573, 9039.632444658953),
        (-5522.428342174251, -12669.421902915114),
        (1921.9736351644333, -819.4244148306425),
        (-43.42549826873483, -11379.631480994227),
        (15885.97203174244, 3154.4197282587966),
        (-2985.116848181212, 8568.1390496989),
        (3465.6137021760487, 1598.7995993496752),
        (-9765.384130516477, 11213.391141488642),
        (-7972.876404687978, -11592.114337169041),
        (3335.5157070316723, -827.7519640453115),
        (-2297.2069314712517, -10155.998959601155),
        (16619.0, 83.1384387633044),
        (-1930.6345432201451, 9748.521338499735),
        (2423.855310863728, 1769.6416477262032),
        (-8178.206532233199, 12154.192044215895),
        (-10184.541576754722, -10922.861975311125),
        (4285.493968404341, -2708.52002493872),
        (-3273.476138593362, -8207.676949065499),
        (16053.744266669262, -3141.5661172905684),
        (-283.9124973174697, 11521.283601692952),
        (1831.067266309984, 235.60270400421632),
        (-5409.688624600669, 12755.216185285595),
        (-12613.782095295484, -9060.196613958018),
        (3779.849788185615, -3973.7002386194254),
        (-4399.2854159542485, -6800.209026176593),
        (15258.41797378724, -5482.506621765771),
        (1759.7518808628756, 12095.97991266514),
        (-232.8897783039372, 799.4669864140267),
        (-2679.253018220056, 12257.430161248723),
        (-14455.357612336351, -6959.504626012196),
        (4928.370630702419, -6059.764912538831),
        (-3727.0275811005517, -5191.286135133005),
        (13599.301635735792, -8188.891904400147),
        (4623.293563370496, 12272.169867954777),
        (-897.8866676444625, 528.0918933916281),
        (-929.1368962054014, 12024.438364644097),
        (-15527.685033356012, -4144.962932685856),
        (4206.726423574073, -7309.802279712022),
        (-4543.633052754175, -3245.26290562497),
        (11617.864019756069, -9976.959558322316),
        (6328.9316515939245, 11864.920645667817),
        (-2567.806004020552, 860.853615415841),
        (1592.7277127431096, 11468.556146798244),
        (-15950.271464198495, -1818.4229767358283),
        (3026.8834253938435, -9129.218224164697),
        (-3826.12574659351, -1245.1037633261494),
        (9136.912197351663, -11203.408598182865),
        (8843.225934805809, 11705.644188136852),
        (-3307.388476030693, 1743.7713323916923),
        (2662.3252592534327, 9431.50297506264),
        (-16426.24780350193, 1333.4526990744623),
        (1595.7817063596017, -10171.768312298918),
        (-3064.3126279520893, -448.89267214549284),
        (6441.735432385036, -12237.620951121195),
        (10645.185962349311, 9815.596213704077),
        (-4259.980012759549, 4076.074350713425),
        (3932.9412916873216, 7892.160066149538),
        (-15567.107837098065, 4627.7817320834765),
        (-546.4259305437754, -11567.539213505996),
        (-906.5650334157226, -267.76170533267305),
        (4651.814899847977, -12124.518590686002),
        (12870.637608321738, 7324.30651394549),
        (-3982.1710145265674, 4810.789706591457),
        (4851.648391633939, 6433.757459237098),
        (-14509.238255123353, 6661.27289139767),
        (-2809.5580308393105, -12982.440969886762),
        (563.3746871947792, 549.8595302681911),
        (1829.8337492207222, -12004.76796964954),
        (14359.245307715082, 5207.665456509676),
        (-4095.278268535659, 6835.480153293485),
        (4082.3619856200876, 4372.280632541844),
        (-12310.641684993127, 8713.58452366106),
        (-5451.176395183907, -12264.35435057962),
        (1397.4105064284618, -544.372654022818),
        (-167.66399188611103, -11372.89467323389),
        (15696.885994166385, 2713.3800097567914),
        (-3454.2528182131923, 8319.416741175779),
        (3969.11709493506, 2314.148808249713),
        (-10712.097574328858, 10441.427272724863),
        (-8277.856182380849, -11733.502931162746),
        (2983.8953718294406, -1322.9114852689709),
        (-2012.5213556620856, -9916.056213934444)], 213

dark_magic()