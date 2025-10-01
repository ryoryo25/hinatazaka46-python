from .member import Member, Name, Tags, Accounts, StringCase

# includes graduated members
ALL_MEMBERS = [
    Member( 0, 0, Name("ポカ", "Poka"), Tags("#pokablog")),
    Member( 1, 1, Name("井口 眞緒", "Mao Iguchi"), Tags("#maoblog", "#maotalk"), Accounts("iguchi.mao")),
    Member( 2, 1, Name("潮 紗理菜", "Sarina Ushio"), Tags("#sarinablog", "#sarinatalk", "#sarina8gram"), Accounts("ushiosarina8_8")),
    Member( 3, 1, Name("柿崎 芽実", "Memi Kakizaki"), Tags("#memiblog", "#memitalk")),
    Member( 4, 1, Name("影山 優佳", "Yuka Kageyama"), Tags("#kageblog", "#kagetalk", "#kagegram"), Accounts("kageyamayuka_official")),
    Member( 5, 1, Name("加藤 史帆", "Shiho Kato"), Tags("#shihoblog", "#shihotalk", "#shihogram"), Accounts("katoshi.official")),
    Member( 6, 1, Name("齊藤 京子", "Kyoko Saito"), Tags("#Kyonkoblog", "#Kyonkotalk", "#Kyonkogram"), Accounts("saitokyoko_official")),
    Member( 7, 1, Name("佐々木 久美", "Kumi Sasaki"), Tags("#kumiblog", "#kumitalk", "#kumigram"), Accounts("kumisasaki_")),
    Member( 8, 1, Name("佐々木 美玲", "Mirei Sasaki"), Tags("#mireiblog", "#mireitalk", "#panchangram"), Accounts("mireisasaki_official")),
    Member( 9, 1, Name("高瀬 愛奈", "Mana Takase"), Tags("#manablog", "#manatalk")),
    Member(10, 1, Name("高本 彩花", "Ayaka Takamoto"), Tags("#ayakablog", "#ayakatalk", "#ayacherigram"), Accounts("ayacheri._.official")),
    Member(11, 1, Name("東村 芽依", "Mei Higashimura"), Tags("#meiblog", "#meitalk", "#meigram"), Accounts("mei.higashimura")),
    Member(12, 2, Name("金村 美玖", "Miku Kanemura"), Tags("#mikublog", "#mikutalk", "#mikugram"), Accounts("miku_osushi")),
    Member(13, 2, Name("河田 陽菜", "Hina Kawata"), Tags("#hinablog", "#hinatalk", "#hina17gram"), Accounts("hina17_kawata")),
    Member(14, 2, Name("小坂 菜緒", "Nao Kosaka"), Tags("#naoblog", "#naotalk")),
    Member(15, 2, Name("富田 鈴花", "Suzuka Tomita"), Tags("#suzukablog", "#suzukatalk", "#suzygram"), Accounts("suzy.tomita")),
    Member(16, 2, Name("丹生 明里", "Akari Nibu"), Tags("#nibublog", "#nibutalk", "#nibugram"), Accounts("nibuchan_akari")),
    Member(17, 2, Name("濱岸 ひより", "Hiyori Hamagishi"), Tags("#hiyoriblog", "#hiyoritalk", "#hamahiyogram"), Accounts("hiyotan928_official")),
    Member(18, 2, Name("松田 好花", "Konoka Matsuda"), Tags("#konokablog", "#konokatalk", "#konokagram"), Accounts("matsudakonoka.yahos")),
    Member(19, 2, Name("宮田 愛萌", "Manamo Miyata"), Tags("#manamoblog", "#manamotalk", "#manamogram"), Accounts("manamomiyata_official")),
    Member(20, 2, Name("渡邉 美穂", "Miho Watanabe"), Tags("#mihoblog", "#mihotalk", "#mihogram"), Accounts("mihowatanabe_")),
    Member(21, 3, Name("上村 ひなの", "Hinano Kamimura"), Tags("#ひなのなのぶろぐ", "#ひなのなのとーく", "#ひなのなのぐらむ"), Accounts("hinanokamimura.official")),
    Member(22, 3, Name("髙橋 未来虹", "Mikuni Takahashi"), Tags("#mikuniblog", "#mikunitalk", "#mikunigram"), Accounts("mikuni.takahashi__")),
    Member(23, 3, Name("森本 茉莉", "Marie Morimoto"), Tags("#marieblog", "#marietalk", "#mariegram"), Accounts("mariemorimoto_official")),
    Member(24, 3, Name("山口 陽世", "Haruyo Yamaguchi"), Tags("#haruyoblog", "#haruyotalk", "#haruyogram"), Accounts("haruyoyamaguchi.official")),
    Member(25, 4, Name("石塚 瑶季", "Tamaki Ishizuka"), Tags("#tamakiblog", "#tamakitalk")),
    Member(26, 4, Name("岸 帆夏", "Honoka Kishi"), Tags("#kishihoblog", "#kishihotalk")),
    Member(27, 4, Name("小西 夏菜実", "Nanami Konishi"), Tags("#nanamiblog", "#nanamitalk", "#nanamigram"), Accounts("konishi773_official")),
    Member(28, 4, Name("清水 理央", "Rio Shimizu"), Tags("#rioblog", "#riotalk", "#riogram"), Accounts("rio_shimizu.official")),
    Member(29, 4, Name("正源司 陽子", "Yoko Shogenji"), Tags("#yokoblog", "#よーこからの連絡")),
    Member(30, 4, Name("竹内 希来里", "Kirari Takeuchi"), Tags("#kirariblog", "#kiraritalk")),
    Member(31, 4, Name("平尾 帆夏", "Honoka Hirao"), Tags("#hirahoblog", "#hirahotalk")),
    Member(32, 4, Name("平岡 海月", "Mitsuki Hiraoka"), Tags("#mitsukiblog", "#mitsukitalk", "#instakurage"), Accounts("mitsuki.hiraoka")),
    Member(33, 4, Name("藤嶌 果歩", "Kaho Fujishima"), Tags("#kahoblog", "#かほりん降臨中")),
    Member(34, 4, Name("宮地 すみれ", "Sumire Miyachi"), Tags("#sumireblog", "#sumiretalk")),
    Member(35, 4, Name("山下 葉留花", "Haruka Yamashita"), Tags("#haruharublog #はるはる日記", "#haruharutalk", "haruharugram"), Accounts("haruka.yamashita.official")),
    Member(36, 4, Name("渡辺 莉奈", "Rina Watanabe"), Tags("#rinashiblog", "#rinashitalk")),
    Member(37, 5, Name("大田 美月", "Mizuki Ota"), Tags("#みーちゃんのぶろぐ")),
    Member(38, 5, Name("大野 愛実", "Manami Ono"), Tags("#manamiblog")),
    Member(39, 5, Name("片山 紗希", "Saki Katayama"), Tags("#sakiblog")),
    Member(40, 5, Name("蔵盛 妃那乃", "Hinano Kuramori"), Tags("#蔵盛妃那乃日記")),
    Member(41, 5, Name("坂井 新奈", "Nina Sakai"), Tags("#ninablog")),
    Member(42, 5, Name("佐藤 優羽", "Yu Sato"), Tags("#satoyublog")),
    Member(43, 5, Name("下田 衣珠季", "Izuki Shimoda"), Tags("#izukiblog")),
    Member(44, 5, Name("高井 俐香", "Rika Takai"), Tags("#rikablog")),
    Member(45, 5, Name("鶴崎 仁香", "Niko Tsurusaki"), Tags("#にこにこぶろぐ")),
    Member(46, 5, Name("松尾 桜", "Sakura Matsuo"), Tags("#sakulovelog")),
]

ALL_MEMBER_NAMES_JA = [t.name.get_full_name() for t in ALL_MEMBERS]
ALL_MEMBER_NAMES_EN = [t.name.get_full_name(en=True) for t in ALL_MEMBERS]

def id_to_name(id: int, en: bool = False, case: StringCase = StringCase.Plain) -> str:
    """Converts member's ID to her name.
    """
    return ALL_MEMBERS[id].name.get_full_name(en, case)

def name_to_id(name: str, en: bool = False) -> int:
    """Converts member's name to her ID.
    """
    if en:
        return ALL_MEMBER_NAMES_EN.index(name)
    return ALL_MEMBER_NAMES_JA.index(name)

def id_to_blog_tag(id: int) -> str:
    """Gets member's blog hash tag from her ID.
    """
    return ALL_MEMBERS[id].tags.blog

def id_to_talk_tag(id: int) -> str:
    """Gets member's her official message app hash tag from her ID.
    """
    tag = ALL_MEMBERS[id].tags.talk
    return "" if tag is None else tag

def id_to_instagram_tag(id: int) -> str:
    """Gets member's instagram hash tag from her ID.
    """
    tag = ALL_MEMBERS[id].tags.instagram
    return "" if tag is None else tag

def id_to_instagram_account(id: int) -> str | None:
    """Gets member's instagram username from her ID.
    """
    accounts = ALL_MEMBERS[id].accounts
    return None if accounts is None else accounts.instagram

def instagram_accounts():
    """Generates all existing instagram accounts.
    """
    for member in ALL_MEMBERS:
        a = member.accounts
        if a is None:
            continue
        yield a.instagram

def get_nth_phase_list(n: int, en: bool = False) -> list[str]:
    """Generates a list of member's names within the n-th phase.
    """
    return [m.name.get_full_name(en) for m in ALL_MEMBERS if m.phase == n]

NAMES_JA_1ST = get_nth_phase_list(1)
NAMES_JA_2ND = get_nth_phase_list(2)
NAMES_JA_3RD = get_nth_phase_list(3)
NAMES_JA_4TH = get_nth_phase_list(4)
NAMES_JA_5TH = get_nth_phase_list(5)

GRADUATED_IDS = [
    1,  # "井口 眞緒"
    2,  # "潮 紗理菜"
    3,  # "柿崎 芽実"
    4,  # "影山 優佳"
    5,  # "加藤 史帆"
    6,  # "齊藤 京子"
    7,  # "佐々木 久美"
    8,  # "佐々木 美玲"
    9,  # "高瀬 愛奈"
    10, # "高本 彩花"
    11, # "東村 芽依"
    16, # "丹生 明里"
    17, # "濱岸 ひより"
    19, # "宮田 愛萌"
    20, # "渡邉 美穂"
    26, # "岸 帆夏"
]
GRADUATED_MEMBERS = [id_to_name(id) for id in GRADUATED_IDS]