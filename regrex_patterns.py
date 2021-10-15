#完整型
#首选
king_clander_time =['(?<!/v )\S*/n[rc] [前中後之/nu ]{0,4}[^往卒時\s末今]+年\S*/t',  # 包含特殊表示在内的：汉武帝立三年 [^\s]*/nr ([^\s]+/v )*[^往]年[^\s]*/t
                    '(?<!/v )\S+/nr [既/d ]{0,4}立/v [一二三四五六七八九十元百]+[/m ]{0,4}[年歲]',
                    '(?<!/v )\S+/nr 即/v 位/n [一二三四五六七八九十元百]+[/m ]{0,4}年',
                    '(?<!/v )\S+/nr 享/v 國/n \S+/t']

nianhao_clander_time = '[太初|太始|天漢|建元|元朔|漢|元鼎|元光|元狩|征和|高后|元封|共和]\S+年\S*/t'
nianhao_regrex='太初|太始|天漢|建元|元朔|漢|元鼎|元光|元狩|征和|高后|元封|共和'
king_clander_time_5='\S+/nr 享/v 國/n \S+/t'
#没有的话用下面的
other_king_time=[#(?!( [一二三四五六七八九十元百]+年/t)) #[初/d ]在别国里面出现的比较吊，所以去掉
                 '立/v ./[wc] 是/r 為/v \S+/nr',
                 '即/v 位/n .+/[wc][ 是/r]{0,4} 為/v \S+/nr',
                 '立/v .+/w 是/r 為/v \S+/nr',
                 '立/v \S+/nr ./w 是/r 為/v \S+/n',
                 '\S+/[nrofp]{0,5} [初/d ]{0,4}立/v ./[wc]',
                 '\S+/[nrofp]{0,5} [初/d ]{0,4}即/v 位/n [，。]',#(?<!及/p)
                 '^\S+/nr {0,4}立/v ./[wc]|^\S+/nr [初/d ]{0,4}即/v 位/n',
                 '(?<!及/p) \S+/[ofpnr]{2,3} [初/d ]{0,4}即/v 位/n',#(?<!及/p)
                 '\S+/nr (?=[乃/d 於是/c遂/d]{0,9}[踐即]/v 天子/ofp 位/n)',
                 '\S+/nr [得/v ]{0,4}立/v 為/v(?! 趙王| 梁王| 皇后)',#
                 '\S+/nr [得/v ]{0,4}立/v 。',#
                 ]



#'(?<!及/p) \S+/[nrofp]{2,3} [初/d ]{0,4}即/v 位/n ./[wc][ 是/r 為/v \S+/n]{0,15}',#(?<!及/p)

# other_king_time=['\S+/nr [初/d ]{0,4}立/v ./[wc](?! 是/r 為/v)',#(?!( [一二三四五六七八九十元百]+年/t)) #[初/d ]
#                  '立/v \S+/nr ./w 是/r 為/v',
#                  '\S+/nr [初/d ]{0,4}即/v 位/n [，。]((?!/w 是/r 為/v))',#(?<!及/p)
#                  '^\S+/nr {0,4}立/v ./[wc]|^\S+/nr [初/d ]{0,4}即/v 位/n',
#                  '(?<!及/p) \S+/[ofpnr]{2,3} [初/d ]{0,4}即/v 位/n',#(?<!及/p)
#                  '\S+/nr (?=[乃/d 於是/c遂/d]{0,9}[踐即]/v 天子/ofp 位/n)',
#                  '\S+/nr [得/v ]{0,4}立/v 為/v(?! 趙王| 梁王| 皇后)',#
#                  '\S+/nr [得/v ]{0,4}立/v 。',#
#                  '(?<=立/v ，/w )是/r 為/v \S+/nr',
#                  '(?<=即/v 位/n ，/w )是/r 為/v \S+/nr',
#                  '(?<=立/v ).+ ，/w 是/r 為/v \S+/nr']
# other_king_time_10='立/v .+[公]/nr'
#re.findall(pattern,'a/nr 立/v ,/w 是/r 為/v ')
#省略型，需要确定时间基准

ellip_year_time=['(?<!/nr )[前中後之/nu ]{0,4}[一二三四五六七八九十元百]+年/t(?! 而/c| 之/u| 喪/n 畢/v)',
                 '(?<!/nr )[前中後之/nu ]{0,4}[一二三四五六七八九十元百]+年\S+/t(?! 而/c| 之/u| 喪/n 畢/v)',
                 '(?=/nr )[一二三四五六七八九十元百]+年\S+/t',#不仅有年份，还有进一步的时间信息'
                 '^[一二三四五六七八九十元百]+年/t(?! 而/c| 之/u| 喪/n 畢/v)' ,#只有年份，且出现在句首
                 '^[一二三四五六七八九十元百]+年\S+/t(?! 而/c| 之/u| 喪/n 畢/v)',
                 '(?<!/nr )立/v [一二三四五六七八九十元百]+年/t',]
# ellip_year_tim6_3='^[前中後][一二三四五六七八九十元百]+年\S*/t'


ellip_month_time_1='[一二三四五六七八九十元百正]+月\S+/t'
ellip_month_time_2='^[一二三四五六七八九十元百正]+月/t(?! 而/c| 之/u| 喪/n 畢/v)'
ellip_month_time_3='(?<!/t )[其至]/[rv] [一二三四五六七八九十元百正]+月\S+'
ellip_season_time='^[中仲孟季]{0,1}[春夏秋冬][^\s商時殷后]+/t'

ellip_day_time_1 = '[一二三四五六七八九十元百]+日[^\s|良日]+/t'
ellip_day_time_2 = '^[一二三四五六七八九十元百]+日/t(?! 之/u)'

#计算型，需要确定时间基准
#calculate_past='[同明往期旦来前旬后今即昨][日月年歲春夏秋冬]\S*/t'
calculate_now='^[是其此]/r [歲日時年春夏秋冬]/t|當/v 是/r [之/u ]{0,4}時/t'
calculate_now2='^[其]{0,1}[春夏秋冬]'
calculate_future=['^[其/r ]{0,4}[居後]/[v|n] [一二三四五六七八九十]+[年日天月]',
                  '^[居後]/[v|n] [一二三四五六七八九十]+[歲年日天月]', #去掉了这里的後
                  '^[其/r ]{0,4}[來明]年',
                  ]  #不能在中间  '^[一二三四五六七八九十]+歲'
#後/n 一歲/t



#other_time
#模糊型时间描述
obscure_time=['^[往來季長時終末凶期朞百即晏異他]+[年歲月日]/t',
                '^[昔]|nr/ 時/t ，',
                '[一二三四五六七八九]{2}[年]','後/n 歲/t 餘/n',
               '^初/[dt] ']



patterns_dict={
            'nianhao_clander_time':[nianhao_clander_time],
            'king_clander_time':king_clander_time,#‘优先返回文公即位二年’
            'other_king_time': other_king_time,
            'ellip_year_time':ellip_year_time,
            'ellip_month_time':[ellip_month_time_1,ellip_month_time_2,ellip_month_time_3],
            'ellip_season_time':[ellip_season_time],
            'ellip_day_time':[ellip_day_time_1,ellip_day_time_2],
            'calculate_now':[calculate_now,calculate_now2],
		    'calculate_future':calculate_future,
            'obscure_time': obscure_time}


