# vroid-to-mmd-shapekeys.py
# This file is part of VRoid to MMD in Blender
#
# Copyright (C) 2026 sephdotwmv
#
# VRoid to MMD in Blender is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# VRoid to MMD in Blender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VRoid to MMD in Blender; if not, see <https://www.gnu.org/licenses/>.

import bpy

for key in bpy.context.active_object.mmd_root.vertex_morphs:
    # **Missing visemes:**
    # 
    # Eyes:
    # なごみ - Howawa
    # はぅ - > <
    # はちゅ目 - O O
    # 星目 - EyeStar
    # はぁと - EyeHeart
    # 瞳小 - EyeSmall
    # 瞳縦潰れ - EyeSmall-v
    # 光下 - EyeUnderli
    # 恐ろしい子！ - EyeFunky (Please note that the exclamation point here is somehow double-width)
    # ハイライト消 - EyeHi-off
    # 映り込み消 - EyeRef-off
    # 喜び - Joy
    # わぉ?! - Wao?!
    # なごみω - Howawa ω
    # 悲しむ - Wail
    # 敵意 - Hostility
    #
    # Mouth:
    # あ２ - a 2
    # ∧ - Mouse_2
    # □ - □ (What the fuck does this mean)
    # ω - Omega
    # ω□ - ω□ (Again, what the fuck does this mean)
    # にやり - Niyari
    # にやり2 - Niyari2
    # ぺろっ - Pero
    # てへぺろ - Bero-tehe
    # てへぺろ２ - Bero-tehe2
    # 口角上げ - MouseUP
    # 口角下げ - MouseDW
    # 歯無し上 - ToothAnon
    # 歯無し下 - ToothBnon
    #
    # Brows:
    # 真面目 - Serious
    # 上 - UP
    # 下 - Down
    match key.name:
        case "Fcl_BRW_Fun_R":
            key.name = "にこり右"
            key.category = "EYEBROW"
        case "Fcl_BRW_Fun_L":
            key.name = "にこり左"
            key.category = "EYEBROW"
        case "Fcl_BRW_Fun":
            key.name = "にこり"
            key.name_e = "Smily"
            key.category = "EYEBROW"
        case "Fcl_BRW_Joy_R":
            key.name = "にこり2右"
            key.category = "EYEBROW"
        case "Fcl_BRW_Joy_L":
            key.name = "にこり2左"
            key.category = "EYEBROW"
        case "Fcl_BRW_Joy":
            key.name = "にこり2"
            key.category = "EYEBROW"
        case "Fcl_BRW_Sorrow_R":
            key.name = "困る右"
            key.category = "EYEBROW"
        case "Fcl_BRW_Sorrow_L":
            key.name = "困る左"
            key.category = "EYEBROW"
        case "Fcl_BRW_Sorrow":
            key.name = "困る"
            key.name_e = "Trouble"
            key.category = "EYEBROW"
        case "Fcl_BRW_Angry_R":
            key.name = "怒り右"
            key.category = "EYEBROW"
        case "Fcl_BRW_Angry_L":
            key.name = "怒り左"
            key.category = "EYEBROW"
        case "Fcl_BRW_Angry":
            key.name = "怒り"
            key.name_e = "Get angry"
            key.category = "EYEBROW"
        case "Fcl_BRW_Surprised_R":
            key.name = "驚き右"
            key.category = "EYEBROW"
        case "Fcl_BRW_Surprised_L":
            key.name = "驚き左"
            key.category = "EYEBROW"
        case "Fcl_BRW_Surprised":
            key.name = "驚き"
            key.category = "EYEBROW"
        case "Fcl_EYE_Surprised_R":
            key.name = "びっくり右"
            key.category = "EYE"
        case "Fcl_EYE_Surprised_L":
            key.name = "びっくり左"
            key.category = "EYE"
        case "Fcl_EYE_Surprised":
            key.name = "びっくり"
            key.name_e = "Ha!!!"
            key.category = "EYE"
        case "Fcl_EYE_Close_R":
            key.name = "ｳｨﾝｸ２右"
            key.name_e = "Wink-c"
            key.category = "EYE"
        case "Fcl_EYE_Close_L":
            key.name = "ウィンク２"
            key.name_e = "Wink-b"
            key.category = "EYE"
        case "Fcl_EYE_Close":
            key.name = "まばたき"
            key.name_e = "Blink"
            key.category = "EYE"
        case "Fcl_EYE_Joy_R":
            key.name = "ウィンク右"
            key.name_e = "Wink-a"
            key.category = "EYE"
        case "Fcl_EYE_Joy_L":
            key.name = "ウィンク"
            key.name_e = "Wink"
            key.category = "EYE"
        case "Fcl_EYE_Joy":
            key.name = "笑い"
            key.name_e = "Smile"
            key.category = "EYE"
        case "Fcl_EYE_Fun_R":
            key.name = "目を細める右"
            key.category = "EYE"
        case "Fcl_EYE_Fun_L":
            key.name = "目を細める左"
            key.category = "EYE"
        case "Fcl_EYE_Fun":
            key.name = "目を細める"
            key.category = "EYE"
        case "Fcl_EYE_Angry_R":
            key.name = "ｷﾘｯ右"
            key.category = "EYE"
        case "Fcl_EYE_Angry_L":
            key.name = "ｷﾘｯ左"
            key.category = "EYE"
        case "Fcl_EYE_Angry":
            key.name = "ｷﾘｯ"
            key.name_e = "Kiri-eye"
            key.category = "EYE"
        case "Fcl_EYE_Sorrow_R":
            key.name = "じと目右"
            key.category = "EYE"
        case "Fcl_EYE_Sorrow_L":
            key.name = "じと目左"
            key.category = "EYE"
        case "Fcl_EYE_Sorrow":
            key.name = "じと目"
            key.name_e = "Jito-eye"
            key.category = "EYE"
        case "Fcl_EYE_Spread_R":
            key.name = "上瞼↑右"
            key.category = "EYE"
        case "Fcl_EYE_Spread_L":
            key.name = "上瞼↑左"
            key.category = "EYE"
        case "Fcl_EYE_Spread":
            key.name = "上瞼↑"
            key.category = "EYE"
        case "Fcl_EYE_Natural":
            key.name = "ナチュラル"
            key.category = "EYE"
        case "Fcl_EYE_Iris_Hide":
            key.name = "白目"
            key.category = "EYE"
        case "Fcl_EYE_Iris_Hide_R":
            key.name = "白目右"
            key.category = "EYE"
        case "Fcl_EYE_Iris_Hide_L":
            key.name = "白目左"
            key.category = "EYE"
        case "Fcl_EYE_Highlight_Hide":
            key.name = "ハイライトなし"
            key.category = "EYE"
        case "Fcl_EYE_Highlight_Hide_R":
            key.name = "ハイライトなし右"
            key.category = "EYE"
        case "Fcl_EYE_Highlight_Hide_L":
            key.name = "ハイライトなし左"
            key.category = "EYE"
        case "Fcl_MTH_A":
            key.name = "あ"
            key.name_e = "a"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_I":
            key.name = "い"
            key.name_e = "i"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_U":
            key.name = "う"
            key.name_u = "u"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_E":
            key.name = "え"
            key.name_e = "e"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_O":
            key.name = "お"
            key.name_e = "o"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_Neutral":
            key.name = "ん"
            key.name_e = "n"
            key.category = "MOUTH"
        case "Fcl_MTH_Close":
            key.name = "一文字"
            key.category = "MOUTH"
        case "Fcl_MTH_Up":
            key.name = "口上"
            key.category = "MOUTH"
        case "Fcl_MTH_Down":
            key.name = "口下"
            key.category = "MOUTH"
        case "Fcl_MTH_Angry_R":
            key.name = "Λ右"
            key.category = "MOUTH"
        case "Fcl_MTH_Angry_L":
            key.name = "Λ左"
            key.category = "MOUTH"
        case "Fcl_MTH_Angry":
            key.name = "Λ"
            key.category = "MOUTH"
        case "Fcl_MTH_Small":
            key.name = "うー"
            key.category = "MOUTH"
        case "Fcl_MTH_Large":
            key.name = "口横広げ"
            key.name_e = "MouseWD"
            key.category = "MOUTH"
        case "Fcl_MTH_Fun_R":
            key.name = "にっこり右"
            key.category = "MOUTH"
        case "Fcl_MTH_Fun_L":
            key.name = "にっこり左"
            key.category = "MOUTH"
        case "Fcl_MTH_Fun":
            key.name = "にっこり"
            key.name_e = "Smile"
            key.category = "MOUTH"
        case "Fcl_MTH_Joy":
            key.name = "ワ"
            key.name_e = "Wa"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_Sorrow":
            key.name = "▲"
            key.name_e = "Mouse_1"
            key.category = "MOUTH" # TODO: this might be incorrect
        case "Fcl_MTH_Surprised":
            key.name = "わー頂点"
            key.category = "MOUTH"
        case "Fcl_MTH_SkinFung_L":
            key.name = "肌牙左"
            key.category = "MOUTH"
        case "Fcl_MTH_SkinFung_R":
            key.name = "肌牙右"
            key.category = "MOUTH"
        case "Fcl_MTH_SkinFung":
            key.name = "肌牙"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1":
            key.name = "牙"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Up_R":
            key.name = "牙上右"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Up_L":
            key.name = "牙上左"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Up":
            key.name = "牙上"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Low_R":
            key.name = "牙下右"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Low_L":
            key.name = "牙下左"
            key.category = "MOUTH"
        case "Fcl_HA_Fung1_Low":
            key.name = "牙下"
            key.category = "MOUTH"
        case "Fcl_HA_Fung2_Up":
            key.name = "ギザ歯上"
            key.category = "MOUTH"
        case "Fcl_HA_Fung2_Low":
            key.name = "ギザ歯下"
            key.category = "MOUTH"
        case "Fcl_HA_Fung2":
            key.name = "ギザ歯"
            key.category = "MOUTH"
        case "Fcl_HA_Fung3_Up":
            key.name = "真ん中牙上"
            key.category = "MOUTH"
        case "Fcl_HA_Fung3_Low":
            key.name = "真ん中牙下"
            key.category = "MOUTH"
        case "Fcl_HA_Fung3":
            key.name = "真ん中牙"
            key.category = "MOUTH"
        case "Fcl_HA_Hide":
            key.name = "歯隠"
            key.category = "MOUTH"
        case "Fcl_HA_Short_Up":
            key.name = "歯短上"
            key.category = "MOUTH"
        case "Fcl_HA_Short_Low":
            key.name = "歯短下"
            key.category = "MOUTH"
        case "Fcl_HA_Short":
            key.name = "歯短"
            key.category = "MOUTH"
        case "Fcl_ALL_Neutral":
            key.name = "ニュートラル"
            key.category = "OTHER"
        case "Fcl_ALL_Angry":
            key.name = "怒"
            key.category = "OTHER"
        case "Fcl_ALL_Fun":
            key.name = "楽"
            key.category = "OTHER"
        case "Fcl_ALL_Joy":
            key.name = "喜"
            key.category = "OTHER"
        case "Fcl_ALL_Sorrow":
            key.name = "哀"
            key.category = "OTHER"
        case "Fcl_ALL_Surprised":
            key.name = "驚"
            key.category = "OTHER"
        case _:
            pass