import requests
import subprocess
import re
import json
import base64

import urllib3
urllib3.disable_warnings()

from champion_info import ChampionInfo

API_MAP = {
    "career_stats": "lol-career-stats/v1/position-averages/season/{season}/{position}/{tier}/{queue}",
    "summoner_info": "/lol-summoner/v1/summoners?name={name}",
    "match_history": "/lol-match-history/v1/products/lol/{puuid}/matches",  
    "career_stats": "/lol-career-stats/v1/summoner-games/{puuid}/season/{season}",
    "summoner_profile": "/lol-summoner/v1/summoner-profile?puuid={puuid}",
    "matches": "/lol-match-history/v1/products/lol/{summoner}/matches",
    "gamemeta": "/lol-match-history/v1/games/{gameId}",
    "champion": "/lol-champ-select/v1/grid-champions/{championId}",
}


# dump 文件
def dump_file(data, filename):
    if isinstance(data, dict):
        with open(filename, "w", encoding="utf-8") as f:
            for key, value in data.items():
                f.write(f"{key}: {json.dumps(value)}\n")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

# 执行win命令
def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(error)
    return output

# 解析客户端进程信息
def parse_client_info(client_info):
    client_info = str(client_info)
    # print(f"client_info: {client_info}")
    token_str = re.findall("(?<=--remoting-auth-token=).+(?=\" \"--app-port)", client_info)
    port_str = re.findall("(?<=--app-port=).+(?=\" \"--install-directory)", client_info)
    pid_str = re.findall("(?<=--app-pid=).+(?=\" \"--output-base-dir)", client_info)
    return token_str[0], port_str[0], pid_str[0]

# 查召唤师20把游戏id
def get_20_games(puuid, headers):
    result = []
    # 查历史20把战绩
    match_url = f'https://127.0.0.1:{port}{API_MAP["matches"].format(summoner=puuid)}'
    response = requests.get(match_url, headers=headers, verify=False)
    data = response.json()
    games = data.get("games", {}).get("games", [])
    for game in games:
        gameid = game.get("gameId")
        result.append(gameid)
    return result

# 查询一把游戏的10个玩家
def get_10_players(gameid, headers):
    result = []
    match_url = f'https://127.0.0.1:{port}{API_MAP["gamemeta"].format(gameId=gameid)}'
    response = requests.get(match_url, headers=headers, verify=False)
    data = response.json()
    players_info = data.get("participantIdentities", [])
    result = [info.get("player", {}).get("puuid") for info in players_info]
    return result

# 查询一把游戏的英雄胜率信息
def update_game_champion_info(gameid, headers, champion_info: ChampionInfo):
    result = []
    match_url = f'https://127.0.0.1:{port}{API_MAP["gamemeta"].format(gameId=gameid)}'
    response = requests.get(match_url, headers=headers, verify=False)
    data = response.json()
    participants = data.get("participants", [])
    for participant in participants:
        championId = participant.get("championId")
        is_win = participant.get("stats", {}).get("win")
        position = participant.get("timeline", {}).get("lane")
        champion_info.update_info(position, championId, is_win)
    return result

# 获取客户端进程信息
output = execute_command("wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline")
token, port, pid = parse_client_info(output)
auth = base64.b64encode(("riot:" + token).encode("UTF-8")).decode("UTF-8")

# 查询召唤师信息
headers = {
    "Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Basic " + auth
}


summoner_url = f'https://127.0.0.1:{port}{API_MAP["summoner_info"].format(name="死亡射线丶yeye然")}'
response = requests.get(summoner_url, headers=headers, verify=False)
data = response.json()
puuid = data.get("puuid")

total_gameid_list = []
total_puuid_list = [puuid]
player_index = 0
game_index = 0

# 初始化信息
champion_info = ChampionInfo()
total_num = 5000
while game_index <= total_num:
    
    if game_index % 20 == 0:
        print(f"已计算完毕{len(total_gameid_list)}局")
    
    # 1. 更新gameid列表
    if game_index == len(total_gameid_list):
        current_puuid = total_puuid_list[player_index]
        player_index += 1
        game_list = get_20_games(current_puuid, headers)
        for game_id in game_list:
            if game_id not in total_gameid_list:
                total_gameid_list.append(game_id)
        # 没有更新的比赛了 
        if game_index == len(total_gameid_list):
            print("no new games")
            break
                

    # 2. 更新playerid列表 
    current_gameid = total_gameid_list[game_index]
    player_list = get_10_players(current_gameid, headers)
    for playerid in player_list:
        if playerid not in total_puuid_list:
            total_puuid_list.append(playerid)

    # 没有更新的选手了
    if player_index == len(total_puuid_list):
        print("no new players")
        break
    
    # 3. 查询一局游戏英雄胜率信息
    update_game_champion_info(current_gameid, headers, champion_info)
    game_index += 1

champion_info.resort(game_index)

dump_file(champion_info.mid_info, "rank/mid.txt")
dump_file(champion_info.top_info, "rank/top.txt")
dump_file(champion_info.bot_info, "rank/bot.txt")
dump_file(champion_info.jug_info, "rank/jug.txt")
    
    
    

