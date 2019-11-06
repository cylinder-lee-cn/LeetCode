"""
820. 单词的压缩编码


给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，
我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

示例：
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

提示：
1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。
"""


class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # words = sorted([word[::-1] for word in set(words)])
        # # print(words)
        # last = ""
        # ans = 0
        # for word in words + [""]:
        #     if not word.startswith(last):
        #         ans += len(last) + 1
        #     last = word
        # return ans
        newwords = sorted([w[::-1] for w in words])

        baseword = newwords[0]
        wordslength = len(baseword)

        for i in range(1, len(newwords)):
            word = newwords[i]
            wordlen = len(word)
            if word.startswith(baseword):
                wordslength = wordslength - len(baseword) + wordlen
            else:
                wordslength = wordslength + wordlen + 1
            baseword = word
        return wordslength + 1


s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))
print(s.minimumLengthEncoding(['me', 'time']))
print(
    s.minimumLengthEncoding([
        "gtgwzg", "bgmwmrk", "nqslwdi", "nwsfvi", "ixfez", "muovikm",
        "cfxptlx", "nffdyw", "zrmtvv", "odmhe", "btupmf", "sjfmx", "pytwab",
        "kznqxp", "jngry", "ppivkj", "bwwmqpq", "lxbnu", "altks", "motdd",
        "jimgy", "lppjek", "kbanc", "lxtgvb", "uqvvek", "ntpxnyn", "qlrdcx",
        "xcmgzwt", "gtcapjg", "sntqu", "tkfwow", "xqbja", "fyqbiw", "ruawk",
        "frjdyp", "txknwrh", "kzyjg", "bttxz", "lgntv", "ewfxgz", "lchzsg",
        "yqfoa", "zhsbm", "htxcg", "qjqkxou", "gkcxv", "lhsjs", "igrtnjv",
        "ifuecww", "slzcs", "yceue", "retyxs", "klybm", "jbxjv", "erhosw",
        "bjhjpjr", "nvwkcq", "mezursm", "ykbvin", "xzlij", "uiopt", "zyuxddz",
        "rmfhp", "xfltr", "csluqps", "gzuvj", "oyqyjy", "lgjuw", "hytegp",
        "gkoxj", "boirzbg", "dsqre", "gxrgabo", "jdlab", "kchijrb", "kuozwmp",
        "vrjqov", "hfmehfl", "xkonfn", "yfhkp", "ocota", "akfao", "qllffp",
        "etrpndt", "nrnmeh", "kaemhl", "diqeja", "wxclkjl", "bggfny", "krvmmx",
        "wofbj", "dliqwvn", "fcihtkt", "fonqx", "irawity", "kkmlx", "gjmshvq",
        "llcov", "vyqbaz", "ypprher", "erzcn", "zdzmj", "secthxg", "dnyxtvn",
        "ivqrk", "xzstj", "tvmepa", "rweifqm", "tjvoeme", "lquuq", "xeulv",
        "gxmyfrx", "ahltke", "hgbgr", "gtddmv", "dbrol", "tmqlk", "bmfaok",
        "iqojj", "zowni", "gwkvkgs", "mtoxm", "wyinnug", "kfotoix", "duymz",
        "keywrvl", "mukloly", "lfcycan", "illypju", "jfmlw", "atmaai", "lcsrk",
        "aarsej", "gylent", "cvoorpa", "awpczi", "vsrerd", "gngvhu", "fhwkc",
        "wsvftqb", "yevwb", "vgcpwb", "zymvkkh", "bziergz", "regjz", "ajhdn",
        "bgqwre", "kqfqax", "cjyly", "vinwbe", "ymkbtst", "oavwn", "onjzg",
        "qssxa", "eiakw", "zpcke", "ifgotsq", "adjdprf", "ilbtt", "vcjgw",
        "zzbjnin", "nztco", "dbyruh", "nvsvk", "jgits", "erzqz", "leqns",
        "twrrlp", "rqymf", "vmzijn", "kegnmyk", "oqbmcg", "otzae", "wtnls",
        "gstgfvy", "pqcjlui", "mxuitc", "tthpkeo", "ilhfm", "mganq", "akfti",
        "savwla", "jknboxy", "gizapl", "kkogrl", "bxflyea", "djeqc", "trypds",
        "ifowgv", "wojnr", "zqtpjh", "hirqg", "bfssfo", "wklsjey", "flvmqe",
        "lccbypw", "vatqhl", "exoqnda", "timli", "dfqsw", "vpqofqw", "wkqmuw",
        "jjrak", "ehqkwsc", "aszlpxn", "pcljgad", "oulhg", "miuirt", "fnpbpb",
        "slgcj", "sobzp", "qjjaaz", "xyzqeyp", "hxcdwyz", "zoxfyc", "dpjezj",
        "nhlbk", "wjgbvxc", "vskzyvm", "yjknun", "magigau", "qdyztsp",
        "tzauro", "cyafd", "tueqrk", "vbsndz", "oenku", "onyxixo", "cznrfu",
        "vylwwl", "cjquqf", "dtvjbs", "hrbax", "vtfkhsv", "kgunkh", "gzoralk",
        "rrnyslz", "ynqxm", "cpgky", "xhasqk", "mobfn", "qzumziz", "gttim",
        "cfvghnl", "bqlna", "saaaoa", "bdejifh", "uwddhyf", "ucqde", "yahxi",
        "ghjytm", "pfdtj", "ncqyqz", "bwplqpm", "jmdprp", "wjzuh", "oyvsn",
        "uxlqcco", "rgxzul", "mzhgvih", "iauvz", "zpygy", "mptoxu", "veektwe",
        "ulaietf", "bqcymhk", "hibij", "fzcoy", "ksrdhev", "auvxxqg", "bkqvrj",
        "egkcxj", "vdczklu", "wopnw", "wtfxx", "zdryst", "yfxyi", "hdezi",
        "cwsoiof", "gwfuqg", "wikkxzu", "vakgw", "jtoqr", "qzrzgo", "ovqtjk",
        "fvouhbd", "iunwj", "aafavex", "wwaisl", "idcyou", "pmbbjxw", "icjufh",
        "rjzog", "exhvn", "dypdbhr", "crvpii", "uylzlrp", "sutckm", "sxakybe",
        "kxhlcve", "xnnbz", "xrvwgj", "tfzqzz", "mzknfo", "anlfzcr", "lwsdak",
        "eqjgkk", "njdqzuw", "bvbrtx", "jozfbs", "zenxg", "rkpaoft", "aeztwv",
        "zdftrrx", "uurpcsk", "qdxkz", "ijjuxiv", "excyqo", "qqvbfz",
        "aywtfnl", "zpmfprc", "rydfsn", "nvfohp", "mvbjpx", "jpbkjef", "ogwhp",
        "ubaxvg", "ofrqfy", "zyhvyo", "wlakxaa", "tnzyk", "saapyr", "tcmpeb",
        "etnyaq", "lrgsq", "mzpbs", "fkczm", "xxdgd", "lkibi", "gthxdj",
        "dgzld", "tnunjn", "hzzepd", "qhmoci", "dskxgx", "jfyyrzg", "hanzy",
        "pzier", "thxkmx", "fktcrf", "ymdjvmf", "hgzhek", "qcelftn", "yoget",
        "hsadqp", "ydiip", "lkhztjr", "pjkfbi", "wskxv", "qezzdtk", "zereg",
        "lcqvjym", "epdlycj", "lqfnau", "njehxn", "srafi", "dhfwu", "wztjr",
        "ucwgnqv", "wigdg", "jkzcglz", "oxxjx", "yqvlodf", "mmaltkd", "fqahe",
        "nfdef", "urxct", "hzhardk", "ugvufrl", "qoraj", "itsymq", "dxvbn",
        "hvgmwb", "vyoab", "wqexj", "rzimt", "aejilm", "fbetztv", "gzktuf",
        "yxhursl", "uxluoui", "vlhpj", "cazppiu", "skibpc", "iaawl", "bgpqqjw",
        "haworva", "dkdzrd", "oertq", "prphs", "pwoikd", "jzxtju", "lukslx",
        "mwzgsa", "zbmymir", "aarvrk", "vcnarwb", "yvbae", "mblgdx", "wpknz",
        "ftdowg", "ogayhz", "qmemfr", "ldqbre", "oexhbh", "pndmji", "lmmhxnb",
        "ecmutw", "zsblbn", "aimqqnz", "ubsft", "xzagmrb", "lswjdx", "glevzy",
        "kmkzoec", "kimrwg", "akote", "uovrxi", "kfocof", "sikiqtk", "iyjyf",
        "pkpsqu", "otsxxoe", "eoxyld", "snljhud", "ryuqnn", "osadi", "teqsj",
        "ulvrij", "kfjcz", "wvfqwon", "zkisf", "zanaxlm", "zzgegc", "dvcpuj",
        "qdgcjg", "ziwqwr", "enxcv", "cecwvep", "tqoctkw", "zwoau", "opkglae",
        "olpvlts", "zdtrcl", "klrvh", "obrqs", "iwykadf", "vvugv", "sxskcjo",
        "vhyeg", "ydbaeb", "tzgplyf", "bwhyp", "uwombi", "svkodw", "otszu",
        "bkyqfup", "rojnt", "bauroa", "bcribk", "ctihaog", "xktdiel",
        "hkvctki", "wheih", "ylhxy", "wgosp", "bvgtk", "xpclcti", "uktyodd",
        "gfblo", "toaur", "cxdvo", "qezdwdb", "mdvdk", "zyhbs", "akbydkw",
        "wejgqnr", "qifti", "kxalog", "nklzot", "fgoas", "apeymfw", "mdjgo",
        "xifpo", "hfouhi", "mdyyzf", "xacds", "zuijqyd", "hdhsop", "ivgfg",
        "uarodof", "lyqlzmc", "vcyqwnj", "uiekded", "uosqq", "quajnw", "adkri",
        "lxsbi", "porjvx", "awnkf", "sotppb", "sfhorj", "uuocxz", "vstcick",
        "gqvzobl", "rkccef", "rlihmff", "lazuav", "iyahmv", "jmuplkb",
        "oforwx", "ogeheqd", "qpayb", "txetvjv", "uxsgsrj", "procbt", "ehlkp",
        "vdtyz", "eqjyvll", "tkwrwud", "qivrv", "abkkllr", "khpzqpp",
        "cvlhohv", "nvzbx", "svvtji", "wmyveiu", "jrogfr", "zpphtie", "faoamt",
        "ksektw", "ujlilq", "ufuax", "mqjla", "fqrnf", "xcdaet", "kfqknho",
        "ofvdjn", "kxopf", "yysdl", "dgronv", "goknbep", "lyhuswu", "cqmvhx",
        "hoitpoi", "dgzqll", "hpyea", "xfzohrg", "ziyod", "jxkki", "vbyoxz",
        "ouylxxr", "mggezan", "shxvven", "yrqnj", "tzdyik", "syeaa", "fthdjm",
        "zjzvdse", "jxzdjdx", "ipxpb", "ollgnbu", "jcdjyxj", "bqltawp",
        "lhxyv", "dvggabj", "ahcuqje", "lnrtyaz", "kubtfl", "rjetqbx",
        "fogbvq", "tcwhba", "ksxusyg", "qlemv", "dsjnth", "zdmmncv", "sdrzpfk",
        "yyocl", "vtqst", "bobtwdu", "ivifxf", "uaxwlo", "piqiigo", "pifql",
        "tdhuue", "lrmdb", "peetwl", "lvwpwji", "dcibnrm", "ppamuxo", "pknto",
        "cbiova", "wdhekr", "kgipdgd", "jlpvi", "zoptbb", "yxeamj", "pjnac",
        "tpdprx", "bltdktt", "wtisu", "cezsmz", "bbbqxk", "hnyweo", "jsuuu",
        "bykgghi", "spulymw", "bynqe", "accaq", "lghcqe", "nqygqvx", "lfvkqbw",
        "duzud", "agmnlw", "gqhqc", "xkgie", "fumakny", "momon", "scubukr",
        "xrtmoe", "ywnbn", "wdkbdzv", "wyflbp", "vyaeb", "wwzzper", "veghzzz",
        "fdkrof", "bkjtao", "tbvpcis", "ftzghcq", "yjsfg", "ngdkr", "pllzc",
        "rgviwsm", "mydqr", "ilcjq", "kmoryr", "ocnwqw", "zxggamr", "kjlasr",
        "idjbkt", "bjvple", "oauzpzw", "gsxjp", "sehbaf", "uubptgp", "ebhaa",
        "ximeurd", "kqewx", "mmcaiba", "lzpqva", "viexed", "zbcocmi", "nxnuzv",
        "vyawhnk", "rozmsws", "oqbubyy", "lbvegpt", "xfxct", "jifzdqm",
        "bmnjwmc", "ptxcqc", "ovzsxog", "ylomlt", "quoic", "tlyjmyb", "fgxpcf",
        "wyhyzyb", "zngau", "zgsef", "phsinbl", "kgybiqo", "tvpsi", "cuxnlt",
        "hqrrs", "spkjg", "kstnc", "grcrons", "lmbjo", "mypsfq", "scwir",
        "ypngb", "rwqksn", "ehjufq", "yulvm", "vyqrmg", "luyto", "ueiqm",
        "tcgcqrg", "yknwn", "szrbbtv", "wupfh", "vwrmiq", "msleyih", "iqtae",
        "ezykx", "ilewp", "hcttjul", "esiianh", "wkuuv", "jszkrx", "gumys",
        "lketi", "zvpsb", "xsvlhst", "myywl", "svexdk", "biwsh", "kpbjcdf",
        "cyiwl", "ilhfm", "rvqbly", "ukowa", "gkmul", "krtcmi", "vwszj",
        "nxwipbr", "fsycct", "jeglcq", "donvsld", "bdckkdr", "iemljm", "gfpgc",
        "qilgqhx", "ounvam", "qyomyt", "zklqshf", "bpauei", "kenzs", "ytgaq",
        "nnepek", "tniqq", "swlbj", "ibdkeo", "oxoed", "scvcrs", "jbitcfz",
        "fjnrwjl", "jogkl", "pmeyrjc", "kahnos", "wozbzk", "ytdav", "pcley",
        "kjxsvub", "jfyxt", "xkttisb", "rvdhbpc", "vvbwnmi", "cecnlb",
        "jjqemu", "iasnf", "usrtyx", "vtastv", "gcbwnft", "qsiqvo", "rfbua",
        "utaxsxl", "msrkymm", "hjuppov", "jmhmcsc", "pdiujj", "eafuzlc",
        "srjvh", "kzrubm", "fkgzdj", "kjptq", "zrcid", "xiuqod", "nvfjea",
        "ioeod", "wncxt", "avbhjud", "qkxrl", "rbmhfcq", "shyvqbu", "ffcmv",
        "omfeko", "ucibm", "lexpw", "rjuqey", "qohfd", "fjgzi", "mlozc",
        "rstgl", "ntkraqo", "paykcw", "iaajb", "adpem", "gkgjbnj", "yxbuvg",
        "fqkxt", "jmyqte", "uzeqyj", "rumyxor", "gkfzleq", "dwngr", "thtqdtr",
        "yptnz", "xoadll", "psvhyce", "geoso", "lijtbu", "amkbuby", "gfpyw",
        "plkso", "owdmtvh", "fkxad", "keqdrz", "irxjure", "gfwepm", "wyxiom",
        "pyedlj", "mfszmv", "tkjiofn", "epjdigv", "jjnuh", "mtxks", "nvfts",
        "xtqhc", "xttlu", "sasra", "qfumac", "rwfavex", "rcwstl", "cfzmi",
        "htvxrs", "nokfsvv", "tbvtckp", "wsikt", "tyvwtw", "hyvzd", "edflcy",
        "wduqbbl", "xacrrb", "sfbzq", "adhhyy", "tltmppb", "imjooie", "joizol",
        "rbzhgs", "rcldg", "ikspo", "sxouwi", "llemmdb", "nkkfie", "uadfas",
        "rigylga", "mbnhs", "vwtsnh", "uiskft", "ppvhyr", "znaenz", "lbjldsk",
        "sizcja", "dzvlem", "iedleqf", "zhxzaqt", "zyeen", "ijdohjj", "dvycit",
        "nfqyxoc", "xgspmx", "gticsq", "tvodn", "zpvtu", "yvevn", "bugvglx",
        "pprlwl", "wikandw", "fmkqpzp", "sjfnjlf", "yswptd", "aeuqf", "ihynsy",
        "fnlrtb", "haewxo", "fvnzrx", "mudxoc", "vtdpd", "zuldtvj", "kerpq",
        "xeesgr", "enhkpmo", "bhhlngf", "vcqrcr", "drflmq", "dufvzsz", "fuouj",
        "bqcyqr", "tsiyu", "lrpnmx", "hfqhwz", "irfjh", "fikhwz", "qxptzm",
        "jzppff", "asutke", "byouz", "amqbvx", "jgsfh", "obdvlb", "sfcdx",
        "ofkxo", "asamcnd", "caxpnb", "qjaqpy", "zbtsmeu", "atzzwkl", "ebkpov",
        "gxuyje", "ybgbdd", "jqaca", "wnrqyt", "omxxneb", "xerpzsl", "iadesn",
        "mtbdwj", "qftiu", "fpeuu", "pipsu", "koxnbn", "ztult", "uguldn",
        "aceqlji", "uasdjf", "tcydz", "gswhdlg", "rieim", "ojplv", "tjmavcp",
        "tfbcvlh", "uutoacm", "ihsixk", "qwvagbe", "nxizc", "zvwfvk", "cdsyeb",
        "hambpgs", "hpsndyh", "gwjoyw", "ocqpmcm", "xrbmn", "grmefy", "wwoxg",
        "tyvgc", "voeqrnu", "rwnsj", "cnmnz", "dxltx", "xnybz", "jslwhka",
        "dremxm", "gfcba", "fijeyqo", "kxzpxyg", "idjbzud", "rfndjd", "gqyslh",
        "wpoznf", "cbzma", "dnvfyh", "spguxoa", "bhjhe", "pehce", "vwanott",
        "giwquq", "vhvwh", "krukn", "xojkq", "mpdfbk", "evlzdsw", "mlbytl",
        "dzeeupj", "pfyyieu", "khbxqla", "pjfdf", "ouvrzs", "liyksgg", "aimlb",
        "jujhbu", "qtxebe", "nermn", "itsnf", "whpetav", "pnjfufk", "xeutgz",
        "sbzev", "vimqnd", "dmagho", "qfwlrsd", "dnchdg", "ykmrpua", "fwlim",
        "mxxhdrc", "uewuwtk", "cubiq", "lrrot", "ntfzl", "epluzj", "lqxnwo",
        "cehhmlm", "ntewnl", "mqlxmr", "yifbwx", "srvzoge", "ocorz", "nahzh",
        "eyxyrv", "ygtxiq", "lznyt", "kntje", "qztqnwk", "zcuogu", "jvvqgir",
        "cgknqi", "jzdcl", "kbcnli", "ofavaz", "govvnq", "chmuflw", "vxkxu",
        "lgzbgu", "oaeleyg", "wbjjdiq", "rxzei", "orhgon", "swmrkye",
        "lfecfum", "zrwygt", "dnsly", "wayaxe", "idvhdd", "nzlrr", "qinomxp",
        "zqexfqg", "cgirjzp", "cxyrqt", "jledfgr", "xstkbu", "lsazo", "vqlam",
        "bwdacez", "mpyxys", "mjljmde", "hztog", "tjubtlz", "vhhhn", "ssercal",
        "xthbxt", "icyiu", "iljzz", "zhnjfm", "cktcwjh", "qetdt", "gdeenr",
        "lcktgy", "wzwoug", "mefjve", "fryrl", "fefwp", "dzvow", "ytomt",
        "wglib", "komqcu", "wztnrs", "gestvx", "hquwilc", "mxfzqf", "svhwm",
        "viymyf", "uolmu", "uirzdao", "iyprm", "uxjnyzd", "rcwczh", "qofsqkz",
        "oefie", "gmtgrn", "krrfs", "bfhsdnq", "cowzu", "fgrjjz", "xtpdn",
        "wiepso", "slgjrjd", "inlimj", "nscgl", "vvnby", "kxckw", "gllbjjp",
        "juvui", "kbzjd", "odhqpx", "pnpkvf", "fuleic", "inawlx", "essdsdj",
        "fvlud", "ttvjwz", "cnkmtdy", "xlchd", "isqhk", "vmilcks", "xoifyy",
        "bkygwh", "mgzdpre", "waemqvd", "ricio", "wycuo", "bqzkd", "pjazcp",
        "kqviffk", "ojfvq", "unlbnfb", "detmfih", "nytprpm", "fevnwin",
        "iydfpqc", "pkhlbi", "aetnje", "pzojli", "basba", "xutuv", "akncyfb",
        "nsiwt", "shovlwd", "qyayx", "mzjcre", "xadyr", "dxpxj", "mlcpp",
        "zzyaht", "vwqhyeq", "dwmla", "oizmbr", "egwzibj", "rfbmu", "fuzhg",
        "ynlbutf", "yycgtro", "humfhb", "lrkkga", "xglbsoe", "mvrdb", "fvxjbw",
        "lomacg", "fmfmal", "qykti", "oujsp", "nohogca", "dbyvxbi", "eawic",
        "qfzwp", "xrzbec", "rrqyw", "mtbhs", "hbrnv", "fnmeikj", "mwogm",
        "ovxyvn", "cvkqxcr", "xfnobdy", "pkity", "rbgtuwh", "odjnv", "zksyrl",
        "rzuceuk", "qukxs", "ipznvtc", "bsvzooz", "nzbpb", "xpiiir", "chkqepj",
        "wzwzzcw", "rhptep", "yjccu", "avijaiv", "kxpms", "ovwqsgo", "jjqvi",
        "wyrxpu", "kybsyhw", "kvyaj", "dnusp", "irgrjyj", "wpeico", "psgnk",
        "joevw", "pfyqwr", "sxlmcs", "ibblhvx", "aecsjes", "tuqnfd", "avemo",
        "fvijtdb", "zcehesf", "yowvgv", "fnrgd", "jpvkykx", "ekyho", "abtxc",
        "hptqmiy", "duwef", "bdsac", "mgamp", "wtsto", "efxhwad", "yhjwfe",
        "adnhhh", "ouykgrh", "sbtpmr", "fzkps", "mdilvvn", "ztvysu", "rafkn",
        "ledgijl", "ewlnpsr", "cedlekw", "gngcu", "phbqtb", "znfjwqk", "wrqkv",
        "tayvdd", "cceqg", "dabgyh", "wgutqn", "klseoo", "kaktas", "einjkvf",
        "gzmbvur", "plcskol", "vhpzaqz", "gcezm", "giavzjt", "prrai", "szrtye",
        "lbegl", "jkkunm", "ociydiw", "kstxl", "bqxhkzh", "jzzjv", "vbjzopr",
        "jvdkro", "padxe", "pmezf", "eqwlb", "nupajjp", "bkunbit", "xjqxtr",
        "wzuqmc", "dqozgi", "diqfj", "eqlfngp", "gvnggid", "znylx", "jajie",
        "qmsamw", "mttvg", "gzamj", "cscnb", "bvtreg", "qhbiq", "eklkjp",
        "fbcyl", "rdjsfqf", "qevuv", "jwislw", "unjvd", "fsbvb", "wqcrho",
        "orrylro", "zoxokla", "dgoja", "rgwja", "vqpzfh", "llhtc", "afoic",
        "arscma", "qfwfli", "ivcncxd", "ximts", "kwfebh", "wffmri", "ljace",
        "eonkn", "ueapcli", "qmocdvr", "mdviccj", "vwvyl", "savupw", "fanliyh",
        "ykwvsh", "yzqez", "vdxepxm", "soocy", "jqczsb", "ckufr", "gyusijy",
        "sbdvh", "hgbqt", "zrcka", "mhfhy", "shksov", "pfliju", "xlesen",
        "rgqiz", "mnajzkt", "iozcs", "hqikmbq", "ervfyim", "ezddw", "kgklyaw",
        "sfmqe", "lnaexsi", "llvvt", "bhiwu", "riigy", "gtdxlh", "vpkoeau",
        "apapx", "ebpwll", "pkhqe", "erulwb", "ljxkn", "zhcgls", "ejvxh",
        "fwlsjmq", "yrrykh", "stcxaw", "tgpbny", "grvkdk", "svuzxpf",
        "jwsmwcm", "kayffuh", "xnaisep", "qigyx", "dxnje", "nplwles", "qqomb",
        "xrnrvr", "qmqxr", "datvf", "vllggut", "cadczx", "nknpbhk", "izowycz",
        "pekxqfk", "unbrsm", "mcjown", "kaqiw", "obrurt", "dmwqli", "atjrc",
        "oqmlell", "wymlr", "xjpkztx", "wjyhkna", "otqju", "hblgv", "lxrbs",
        "gyfwu", "vdpmt", "kjmdibo", "ozapzmw", "jwcgtq", "dfymo", "qagvqil",
        "hittrny", "uinvmlm", "tehfpsl", "vpqnzqy", "sroki", "inxetz",
        "isnmony", "nzmvf", "dzufni", "nexqh", "fkjnvma", "gwvst", "idhwax",
        "neeuvln", "iecja", "zwzdp", "vfppg", "obbei", "dfgopn", "acijhp",
        "ixwtkp", "fpyny", "rzozlxq", "djuov", "hhfjcl", "kcnfa", "grguw",
        "dduiej", "rewvs", "imlwk", "fosbbtq", "xjclkjn", "wwpqgb", "jovsfes",
        "mhiaeuj", "fxjgk", "enngxv", "skiaud", "whfkr", "igchqb", "kftala",
        "dwjxl", "xepvk", "qidfjb", "titaly", "jplijvv", "nuzcon", "slleg",
        "tyycth", "dtvrvpd", "yubfqoi", "pkwsff", "zbbko", "nrggf", "hqgnna",
        "yfumb", "qubvic", "qjpwo", "vmepg", "btawj", "zveot", "xaivzxu",
        "tknsmv", "fgbvza", "fnsnqs", "qbismc", "arhyycq", "evvxs", "xpkees",
        "nuumqyd", "yzqdh", "oeeuxh", "vmjcm", "lkvgv", "mpxrugr", "tkxnx",
        "cpafxvh", "wrswmb", "eadznj", "bdvgwz", "ahiegu", "shedlup",
        "sejcyww", "zbusii", "lzdzak", "oymze", "vhbrz", "digdz", "xphzgg",
        "levzi", "tgkvqp", "kmxcnm", "bnwlngx", "iejarx", "dizrscz", "vsyqnv",
        "zkuoye", "beojpk", "hfhvzg", "gisjftm", "dvweqa", "keauzic", "lkjby",
        "ngguexc", "pohngye", "afjtde", "xhddc", "hhttmgi", "caczjl", "wgkfbv",
        "ulvax", "uemxgxs", "uqfzxu", "keaaw", "pdxhn", "waoly", "ukvfwy",
        "pentckg", "bgypmd", "ozywxef", "kxbyg", "ituij", "yssywlv", "iybzdz",
        "knpyeub", "sbkrdlh", "hsqvas", "wrjiuyo", "pgogqmv", "ofsoix",
        "dxldl", "ezhgfxg", "igpkh", "bobmm", "gddpayx", "ejihwu", "evxddr",
        "wdlcpqn", "zlucrvj", "lciroeu", "tozwakg", "ymrlcji", "cpupkp",
        "oqjaa", "ikerp", "eghad", "tntbl", "giqxr", "szavqhz", "acqawb",
        "hdfytnu", "qoksmwl", "snnplu", "drvhr", "uyjef", "kjlpxcr", "wivxg",
        "jemkix", "mlhcmd", "vlivttu", "georzc", "vagamm", "gndipgf",
        "cmvsbmv", "pbfyvz", "pgwye", "qyxpvs", "grjadvo", "vgfev", "kpfloyz",
        "lchpqln", "eejfkcs", "vlkrhp", "ppfukr", "pgrjbg", "wogtj", "cgivop",
        "jnpqoj", "ldlpbrr", "vlgal", "kbjar", "dngqm", "ikgadp", "jipvwuq",
        "xqvjkl", "ojtecxz", "updfcm", "xwbhr", "qhupf", "yuiat", "jhpfebe",
        "vnrrunw", "eunefe", "kzcbqd", "fvxufv", "koynws", "dgyfwb", "nyvekrk",
        "rjuotpr", "ymdwzj", "dnkmrlt", "abykta", "ubmbjdy", "pvarsmz",
        "ttnvs", "jqhejm", "zvrek", "edhxibz", "qexny", "oagswer", "twtur",
        "fmcbl", "qmdma", "zthlqwv", "bhwps", "czqgr", "gqbrrxx", "nkvgzrs",
        "cazmrjq", "nieyb", "bgsgq", "ukfakiz", "yztyra", "tyfrigv", "wlfhd",
        "rbyunj", "usvypgo", "hhkej", "jivtlg", "ifgzqu", "ofjrlw", "rlqyxnm",
        "smljy", "mbgwv", "fwlehwb", "qlogyx", "faxwc", "axaeo", "hkgsppo",
        "dencdr", "ddhbps", "jbxxoc", "pjxyk", "ctvqy", "qvvpzyu", "yewduf",
        "mugmbte", "lzfqvuc", "vhxpg", "jnmqj", "ennlwu", "qmjhiqg", "adierw",
        "goezh", "vjnoz", "rqagh", "emtspp", "nmmhe", "ssomw", "ofkwv",
        "ludzh", "otpfssv", "snwjzz", "ahimcsq", "tgoxkeg", "shnsfau",
        "cmcdlym", "ybnft", "kcoyn", "bonazcf", "gufvm", "tpmlzom", "eyzmod",
        "dokojaj", "xadbjwk", "ffvle", "ntteh", "jevrazt", "efkhc", "bbwntl",
        "srihk", "kmjadz", "qkxsvbq", "ddljp", "uwwuvth", "bipgo", "ihsmv",
        "xmmmcsj", "odmqr", "fttvlys", "shehiuy", "icgwi", "nsvmg", "zqjjkyk",
        "umrie", "spbqz", "xmidgzv", "yadhc", "mspibhn", "xtgxom", "rasfnft",
        "blerfgx", "zfpfq", "xkfclje", "tbzvw", "vgbvg", "ayngxcp", "ndyle",
        "vqbgsce", "fpshlx", "vqufvgv", "dkyccvy", "yyuyjf", "rfxmqdn",
        "sxugzm", "gjhbkv", "xhdjvx", "ymykgxb", "prknrk", "eabbpqr", "qxojf",
        "lzwhuby", "cpozcue", "ishbwlf", "mduhyjx", "rrhhav", "ufbafzp",
        "mfpwuww", "pobnaaj", "lrsxxj", "cohjf", "jkbxz", "sarme", "grklhj",
        "tqvkqy", "ytikna", "asntarp", "gslbu", "exorbu", "cjkwzu", "psdma",
        "zzpdol", "dvgloav", "yxbfakk", "emmcvx", "jlguic", "jjxkfmt",
        "iuendwj", "rathmt", "qyweiba", "xafoy", "dqsnc", "hvkowm", "eabcao",
        "phydpb", "rndnfwg", "qjahwwx", "ytpal", "htmau", "dopybqz", "nvjif",
        "vwwqi", "qermpq", "iizvetj", "xqfos", "rtcuhbe", "igjrfme", "ubxbb",
        "qppcb", "nohfxao", "nfyncug", "ddzhw", "froajrf", "sjjiss", "kqitq",
        "unzlbaj", "sbdaepv", "tvmhcga", "kqhgtom", "vamfzf", "gyofhng",
        "mabbme", "zdchndq", "zybctyd", "psqbrzl", "hyxfsrj", "xtgkdh",
        "ptwqat", "uucrov", "igljkfu", "pktoiui", "nhyil", "cshte", "pfsqa",
        "nsfsmze", "twcuf", "jfqwtd", "vinzb", "afruk", "txldlnj", "jsttu",
        "pkbczjm", "txpfq", "xbhwtcg", "cmcho", "jtuixpl", "xfefj", "oapaczq",
        "xcpvsw", "qbudm", "xdvtr", "hwkmj", "zagtjpd", "ohnawr", "flxbat",
        "epicea", "xmjnmbw", "ywvfcz", "rvyel", "nsuwwuz", "kknoqq", "mhsfiz",
        "hnromvi", "dedzukf", "uldavy", "pdcec", "qojqpmf", "sivfru", "xjayrn",
        "xwjuah", "vkqmb", "wuvkxpc", "nrhsb", "hashdly", "oeudry", "foqpt",
        "sdexar", "nuyli", "smxpkk", "mjheihb", "zmxlu", "ouiisf", "gmhjbb",
        "zozpja", "diimrrm", "uwonbw", "pegxoxf", "obdtpcn", "fdadto", "aekkg",
        "fjjxmeu", "dkqpptm", "wbfuzr", "lfteh", "rbtfbzo", "eglch", "qxrru",
        "oofwkgz", "rgigqr", "gnjpoep", "uexcxs", "mwfgk", "embebip", "suans",
        "oagqbqx", "plyzcsq", "huggwzw", "ccsxy", "waixkjw", "doqwr",
        "uqxkvkc", "yurkj", "slgbj", "mbqzm", "yssszr", "htoph", "gupqhgj",
        "kkrsdv", "uiuxfp", "qxacm", "uwmqc", "jbnzh", "sqyalww", "kcjsmx",
        "lonsz", "pzsmu", "cjqvjw", "qiiulzm", "wfoqt", "kdjnfe", "dsnpjn",
        "xnzmimc", "ulvdd", "fvxpmm", "rzklco", "whyolla", "ppmex", "bgaoi",
        "vskeguj", "kjwbh", "wzskso", "lnpkvie", "lcxsnc", "ddwpwc", "hezxemz",
        "tcgkj", "yawyd", "oymed", "ukqrx", "zfwmo", "ifswz", "mzjuo", "cafpb",
        "kubdbe", "owkux", "rhrvb", "usaev", "pkffvsn", "uindrki", "xeemo",
        "qumuu", "pldri", "ghusk", "xkzsrym", "mndqb", "fpvokz", "kfmeg",
        "lrhmj", "refbzvk", "qlbrmp", "ddjuaj", "foyet", "qtdujqj", "uwvhxsj",
        "xtmtkiz", "xpwvh", "fcgll", "dlnwmj", "rmfnoz", "pomnxn", "vhjcyi",
        "totup", "udgpv", "axpaddc", "qtzmga", "hoszek", "smsmmvg", "qoyvj",
        "vxqigxy", "pvwynx", "puxjpjv", "odcaxeo", "daeuw", "cdugp", "sgwgjdx",
        "buhfyf", "yiwykai", "ojtfyal", "tjaob", "oimmn", "bdtnidq", "zhysw",
        "bojjkf", "wkgqrd", "njecfik", "cnndzrq", "dsiaa", "kumtk", "towbx",
        "bzoirpz", "vtnxby", "plhdj", "rqpai", "ztaousd", "vspwkxu", "mikncyf",
        "pafxpnc", "bggcmvj", "tahqf", "izchgc", "xaspz", "zwfwl", "cwgcuci",
        "wzuzq", "rgrsyzu", "mgytix", "kqqakjw", "eekgzcm", "txbcw", "fcoxkag",
        "kqxac", "licntr", "vmweor", "bslmfto", "jzalnup", "tuiep", "dacwc",
        "zntmpb", "ikexnhq", "mlioa", "klwpv", "ddhbtg", "jurwdf", "jutynuo",
        "dlcicqo", "cnvqsq", "qqsiszn", "vqabt", "huaoigf", "bmlpczh", "dsnuy",
        "qrrqv", "edoxkud", "uqxdk", "gyphg", "rvyzzz", "epjhqj", "dejkvae",
        "zczwgm", "ulisrt", "ihuayib"
    ]))

"""
此题解法：
* 要点是需要判断一个单词是否完全被另外一个单词的尾部包含。如果直接判断的话需要对单词进行切片处理。
* 另外，完全相同的单词会被合并，在结果的长度上没有影响。
* 首先将原words去重，然后依次取每个单词进行翻转，再整体排序，这样就会得到按照字典序的一个数组
  所有尾部相同的自然被排列在一起，而且按照字符长短进行排列
* 然后取newwords的第一个作为基准，再遍历后续的数组，
  如果，后面的单词以基准为开头，那么单词总长就要减去原基准的长度后加上现在单词的长度，并且将
  基准换成现在的单词。
  反之，就要在总长度上增加现在单词的长度，再加一（就是#的长度）
* 完成遍历后的总长度再加一（末尾还有一个#）
"""
