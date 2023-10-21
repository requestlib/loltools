
NAME_ID = {"1": "黑暗之女", "2": "狂战士", "3": "正义巨像", "4": "卡牌大师", "5": "德邦总管", "6": "无畏战车", "7": "诡术妖姬", "8": "猩红收割者", "9": "远古恐惧", "10": "正义天使", "11": "无极剑圣", "12": "牛头酋长", "13": "符文法师", "14": "亡灵战神", "15": "战争女神", "16": "众星之子", "17": "迅捷斥候", "18": "麦林炮手", "19": "祖安怒兽", "20": "雪原双子", "21": "赏金猎人", "22": "寒冰射手", "23": "蛮族之王", "24": "武器大师", "25": "堕落天使", "26": "时光守护者", "27": "炼金术士", "28": "痛苦之拥", "29": "瘟疫之源", "30": "死亡颂唱者", "31": "虚空恐惧", "32": "殇之木乃伊", "33": "披甲龙龟", "34": "冰晶凤凰", "35": "恶魔小丑", "36": "祖安狂人", "37": "琴瑟仙女", "38": "虚空行者", "39": "刀锋舞者", "40": "风暴之怒", "41": "海洋之灾", "42": "英勇投弹手", "43": "天启者", "44": "瓦洛兰之盾", "45": "邪恶小法师", "48": "巨魔之王", "50": "诺克萨斯统领", "51": "皮城女警", "53": "蒸汽机器人", "54": "熔岩巨兽", "55": "不祥之刃", "56": "永恒梦魇", "57": "扭曲树精", "58": "荒漠屠夫", "59": "德玛西亚皇子", "60": "蜘蛛女皇", "61": "发条魔灵", "62": "齐天大圣", "63": "复仇焰魂", "64": "盲僧", "67": "暗夜猎手", "68": "机械公敌", "69": "魔蛇之拥", "72": "水晶先锋", "74": "大发明家", "75": "沙漠死神", "76": "狂野女猎手", "77": "兽灵行者", "78": "圣锤之毅", "79": "酒桶", "80": "不屈之枪", "81": "探险家", "82": "铁铠冥魂", "83": "牧魂人", "84": "离群之刺", "85": "狂暴之心", "86": "德玛西亚之力", "89": "曙光女神", "90": "虚空先知", "91": "刀锋之影", "92": "放逐之刃", "96": "深渊巨口", "98": "暮光之眼", "99": "光辉女郎", "101": "远古巫灵", "102": "龙血武姬", "103": "九尾妖狐", "104": "法外狂徒", "105": "潮汐海灵", "106": "不灭狂雷", "107": "傲之追猎者", "110": "惩戒之箭", "111": "深海泰坦", "112": "机械先驱", "113": "北地之怒", "114": "无双剑姬", "115": "爆破鬼才", "117": "仙灵女巫", "119": "荣耀行刑官", "120": "战争之影", "121": "虚空掠夺者", "122": "诺克萨斯之手", "126": "未来守护者", "127": "冰霜女巫", "131": "皎月女神", "133": "德玛西亚之翼", "134": "暗黑元首", "136": "铸星龙王", "141": "影流之镰", "142": "暮光星灵", "143": "荆棘之兴", "145": "虚空之女", "147": "星籁歌姬", "150": "迷失之牙", "154": "生化魔人", "157": "疾风剑豪", "161": "虚空之眼", "163": "岩雀", "164": "青钢影", "166": "影哨", "200": "虚空女皇", "201": "弗雷尔卓德之心", "202": "戏命师", "203": "永猎双子", "221": "祖安花火", "222": "暴走萝莉", "223": "河流之王", "233": "狂厄蔷薇", "234": "破败之王", "235": "涤魂圣枪", "236": "圣枪游侠", "238": "影流之主", "240": "暴怒骑士", "245": "时间刺客", "246": "元素女皇", "254": "皮城执法官", "266": "暗裔剑魔", "267": "唤潮鲛姬", "268": "沙漠皇帝", "350": "魔法猫咪", "360": "沙漠玫瑰", "412": "魂锁典狱长", "420": "海兽祭司", "421": "虚空遁地兽", "427": "翠神", "429": "复仇之矛", "432": "星界游神", "497": "幻翎", "498": "逆羽", "516": "山隐之焰", "517": "解脱者", "518": "万花通灵", "523": "残月之肃", "526": "镕铁少女", "555": "血港鬼影", "711": "愁云使者", "777": "封魔剑魂", "875": "腕豪", "876": "含羞蓓蕾", "887": "灵罗娃娃", "888": "炼金男爵", "895": "不羁之悦", "897": "纳祖芒荣耀", "902": "明烛", "950": "百裂冥犬"}


class ChampionInfo():

    def __str__(self) -> str:
        return f"上路"

    def __init__(self) -> None:
        self.name_id = NAME_ID
        self.top_info = dict()
        self.jug_info = dict()
        self.mid_info = dict()
        self.bot_info = dict()
        
        for value in self.name_id.values():
            self.top_info[value] = {
                "total": 0,
                "win": 0,
                "fail": 0,
                "win_rate": 0
            }
            self.jug_info[value] = {
                "total": 0,
                "win": 0,
                "fail": 0,
                "win_rate": 0
            }
            self.mid_info[value] = {
                "total": 0,
                "win": 0,
                "fail": 0,
                "win_rate": 0
            }
            self.bot_info[value] = {
                "total": 0,
                "win": 0,
                "fail": 0,
                "win_rate": 0
            }

    # 加入一把新的游戏统计,更新数据
    def update_info(self, position, championid, win):
        name = self.name_id[str(championid)]
        if position == "TOP":
            if win:
                self.top_info[name]["total"] += 1
                self.top_info[name]["win"] += 1
                win_rate = round(self.top_info[name]["win"] / self.top_info[name]["total"] * 100, 2)
                self.top_info[name]["win_rate"] = win_rate
            if not win:
                self.top_info[name]["total"] += 1
                self.top_info[name]["fail"] += 1
                win_rate = round(self.top_info[name]["win"] / self.top_info[name]["total"] * 100, 2)
                self.top_info[name]["win_rate"] = win_rate
        if position == "JUNGLE":
            if win:
                self.jug_info[name]["total"] += 1
                self.jug_info[name]["win"] += 1
                win_rate = round(self.jug_info[name]["win"] / self.jug_info[name]["total"] * 100, 2)
                self.jug_info[name]["win_rate"] = win_rate
            if not win:
                self.jug_info[name]["total"] += 1
                self.jug_info[name]["fail"] += 1
                win_rate = round(self.jug_info[name]["win"] / self.jug_info[name]["total"] * 100, 2)
                self.jug_info[name]["win_rate"] = win_rate
        if position == "MIDDLE":
            if win:
                self.mid_info[name]["total"] += 1
                self.mid_info[name]["win"] += 1
                win_rate = round(self.mid_info[name]["win"] / self.mid_info[name]["total"] * 100, 2)
                self.mid_info[name]["win_rate"] = win_rate
            if not win:
                self.mid_info[name]["total"] += 1
                self.mid_info[name]["fail"] += 1
                win_rate = round(self.mid_info[name]["win"] / self.mid_info[name]["total"] * 100, 2)
                self.mid_info[name]["win_rate"] = win_rate
        if position == "BOTTOM":
            if win:
                self.bot_info[name]["total"] += 1
                self.bot_info[name]["win"] += 1
                win_rate = round(self.bot_info[name]["win"] / self.bot_info[name]["total"] * 100, 2)
                self.bot_info[name]["win_rate"] = win_rate
            if not win:
                self.bot_info[name]["total"] += 1
                self.bot_info[name]["fail"] += 1
                win_rate = round(self.bot_info[name]["win"] / self.bot_info[name]["total"] * 100, 2)
                self.bot_info[name]["win_rate"] = win_rate
    
    # 重新排序, 去掉小于10把的英雄, 按胜率高到低排序
    def resort(self, total):
        keys = NAME_ID.values()
        threshold = total * 0.025
        for key in keys:
            if self.mid_info[key]["total"] <= threshold:
                del self.mid_info[key]
            if self.bot_info[key]["total"] <= threshold:
                del self.bot_info[key]
            if self.jug_info[key]["total"] <= threshold:
                del self.jug_info[key]
            if self.top_info[key]["total"] <= threshold:
                del self.top_info[key]
        # 排序
        self.mid_info = dict(sorted(self.mid_info.items(), key=lambda x:x[1]["win_rate"], reverse=True))
        self.bot_info = dict(sorted(self.bot_info.items(), key=lambda x:x[1]["win_rate"], reverse=True))
        self.jug_info = dict(sorted(self.jug_info.items(), key=lambda x:x[1]["win_rate"], reverse=True))
        self.top_info = dict(sorted(self.top_info.items(), key=lambda x:x[1]["win_rate"], reverse=True))
        
                