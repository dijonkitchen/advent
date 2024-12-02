list_1 = [3, 4, 2, 1, 3, 3]
list_2 = [4, 3, 5, 3, 9, 3]

def paired_distance(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    total_distance = 0

    for i in range(len(sorted_list_1)):
        total_distance += abs(sorted_list_1[i] - sorted_list_2[i])

    return total_distance

print(paired_distance(list_1, list_2))

input = """18944   47230
94847   63037
93893   35622
37174   43365
77982   51397
31706   96051
67726   11902
71456   76965
40482   93061
14585   31152
57069   76739
40699   45538
48676   35141
23514   84329
36128   58619
19869   55004
53224   66466
23070   22452
69524   10212
24599   76499
41935   93701
47751   75200
22288   79000
48293   64117
18945   83950
77769   10212
65140   58619
11513   69837
89714   28488
52610   69684
27185   48656
83658   15787
91134   84764
53850   57354
55054   10212
10212   81939
54102   54749
21657   95309
74862   70479
24811   93701
44850   72214
37491   15131
39163   41356
30157   79478
72424   44104
43654   68485
49496   85056
35899   85495
82281   21503
97192   58619
46034   41302
88365   22452
78817   42083
75589   15628
97939   36953
48643   16469
76050   18546
25408   10212
16067   25012
76415   75766
39296   87007
57548   55243
79498   79292
27852   49166
82634   96695
78249   96938
56840   93780
12951   28946
13039   49166
22477   10074
88807   10212
42685   85959
93702   83921
49909   29611
40950   16129
17686   99806
98863   29649
57293   41383
42078   42809
85441   75766
26599   22452
31809   40317
40119   89377
76115   72872
81044   44280
57936   31570
23584   44970
46888   96589
15361   55594
63692   74559
52670   31750
60619   18861
13696   27415
89912   47230
72773   84214
83210   16630
81206   82152
77155   25012
47208   96589
27327   75766
96293   75766
94802   18939
50909   40761
52198   69276
51653   96252
32519   47906
42094   49166
30025   74276
79623   29594
21295   75766
86206   58773
28359   12935
87017   93701
24615   51435
29542   91998
62901   80808
99146   48462
93075   83501
12847   71229
11612   67385
51369   87988
18870   10212
61738   69411
90693   31667
93786   74967
57197   86660
77071   54749
65104   57354
29984   83935
54425   69634
40618   79059
35774   16648
78840   16210
80413   56785
39217   25298
93831   50040
32680   55594
59870   50040
36131   67911
71258   97112
46357   91998
46740   54902
96459   90222
52806   28324
46820   56708
30526   35626
29428   44549
21148   28946
84200   41021
36356   29549
25777   75766
29472   66900
68046   91615
37179   84320
53210   97112
68886   70490
38812   50077
70453   22452
35806   71290
76766   76089
41867   33965
80657   49842
60247   21877
75830   16129
47465   22452
70411   47230
10471   40477
71528   65211
10691   39320
70085   13626
81136   51123
73681   88207
93864   90161
16042   21503
19117   14263
39492   26125
25417   93176
85049   64490
30406   28946
13936   40223
55243   10212
64181   75766
98237   22179
23552   30923
41294   48019
67196   55243
64661   29550
59452   93701
92837   97112
36014   48646
46410   91998
45131   32289
95566   58325
32847   92161
42927   47621
17116   44104
18876   44104
43451   64810
30220   55654
26157   47230
26861   45774
76012   28557
64192   79495
28946   12740
63292   61488
23478   61247
45638   59390
62148   25012
15588   79809
61594   54593
43461   75119
56158   26910
64821   16129
71462   42138
19014   52709
54415   31726
10780   26628
81105   13443
17184   47230
93701   63170
63671   23085
42812   70453
40766   21503
99854   41302
89526   47230
59515   92251
83921   75766
37583   93701
94103   23018
58212   75766
18584   54593
68062   54088
20139   67251
42424   20275
65341   22452
36194   44104
84111   62555
87601   57354
47336   83921
75923   91998
19615   83340
46509   21503
12075   82277
66851   96589
95505   93701
81644   32516
57336   17727
12682   90905
52826   68088
62855   40799
92119   83921
32885   93701
75637   70453
28707   86404
45032   97112
58498   47961
85626   17279
60072   85959
73172   75766
19185   73497
84031   93176
22488   20544
22074   28656
68023   96589
91623   31654
33490   29082
88696   22485
48398   91998
60841   92396
75629   57133
63314   28896
31311   91998
23917   19993
27798   99891
48238   15083
28428   26662
17958   72086
14206   87315
13904   66292
89364   35379
49166   58278
34424   80519
57587   72976
37012   97112
87711   55243
51942   61233
67747   12348
90926   25573
42892   75766
81837   50805
97461   76662
84405   25012
96786   47230
87719   97112
99414   11771
16685   57613
92494   44104
50709   76415
88473   31588
90391   56730
12159   44104
41424   49166
61248   57226
12277   21503
70185   93176
52564   38541
90462   76530
54612   25944
36957   78976
99626   40838
74461   48804
52764   59795
39568   13839
59180   34793
79871   95283
80594   97112
38245   79495
16766   47245
97273   52603
63895   55243
14683   66083
21429   43338
11489   76415
31788   41198
92919   93701
32081   89099
94955   90022
46573   26879
31615   54593
43751   86933
64967   84391
43567   22452
92406   42601
31462   44457
94913   51858
49742   69674
37148   82620
73210   28164
34140   49166
98962   49166
59416   34928
65077   80693
76448   57315
75645   73007
88343   71889
62221   91998
16215   19777
17452   41302
22985   83948
70440   59065
12100   21677
94845   43833
35379   72336
23269   16029
46025   92161
88652   54749
38841   10212
50077   12087
65896   41302
87949   43913
44934   87596
30760   50040
41302   73959
69787   55243
58816   10212
69377   47230
19377   49904
31559   83921
94937   22452
66329   22485
81585   27836
70384   35736
83758   96589
97318   41302
54935   22452
44104   55243
37414   96172
39932   83921
21164   75386
20226   22452
15034   92161
57192   97112
64008   57354
73625   22452
61123   15919
75907   50077
54845   33251
20037   44104
80669   40465
42188   21503
22974   52138
77086   59531
91679   35709
52264   77686
67647   97112
53545   67863
66273   54593
17748   20578
84923   24554
22010   76415
74303   85928
99586   77484
63990   54749
18839   94320
15584   57354
95309   79495
39376   55243
93614   49141
58781   97102
47844   58619
10765   14103
61349   28946
85686   11125
82542   49166
43208   75766
96568   80715
54906   94639
70032   99196
47768   44104
58932   11863
12943   44104
56429   85959
96596   83921
11965   57354
99730   96675
86594   75708
42049   92161
19333   25012
10197   18778
71145   77443
22777   93701
51275   58028
31605   54304
21126   18400
78695   47230
14591   44661
72862   96589
91673   49166
94405   16129
42737   18769
66822   72342
11928   37147
97867   41856
20453   10212
29753   22485
28106   93930
33749   73377
69689   28789
87973   37705
39634   77935
29043   93176
12534   54749
98827   91998
50279   85959
79552   44104
48382   57012
69488   41302
90802   58619
56253   18828
82457   75766
43272   84374
69955   35561
35744   44588
90267   50040
77933   69756
88884   97112
94463   50087
73911   76407
13999   26120
65181   91732
20556   83036
64565   64378
38024   87984
43790   27992
77458   85959
56630   57551
95681   32462
65381   69595
87770   55243
97854   85959
34976   69043
19094   87279
33712   39331
90408   91998
93191   67478
91732   37381
65511   58619
29134   10212
76517   19790
10213   58843
34474   23878
91075   21503
46159   20494
91998   51669
13733   83609
74667   21503
19170   93701
20715   30508
47230   84073
15999   91214
81634   25591
54188   16688
74813   33434
17109   77375
32457   55243
76430   44104
29624   73312
85473   18668
40572   22452
29607   55594
30213   93176
47775   50077
86680   66588
46833   85959
48630   57354
54046   24686
23735   30358
80324   97523
50040   83004
53711   87200
61254   87730
34102   32331
59675   49166
28571   81539
13257   58619
44802   93176
82857   12949
44862   47077
96280   24082
35949   93176
34949   40295
51993   92251
32228   20459
82185   27052
53353   35330
13317   47729
57354   54593
24588   82337
61603   47230
80008   42380
49943   72523
84307   49166
45773   54293
36986   73229
29364   21503
20558   16129
44114   17585
88385   93701
42932   92398
96098   54749
96999   91773
90750   90896
64574   78656
18171   25740
50769   24584
93931   81203
89260   21503
14790   94095
67994   93176
12061   53549
47020   93701
48991   54749
56852   41302
70634   82333
54495   25012
82926   93176
67073   79495
98886   28946
21988   52120
17454   54313
79488   25164
60506   33312
73047   10212
66249   58619
31977   55243
63947   93701
54164   13046
29541   50040
63772   58619
67198   56809
24815   28640
71105   49818
67768   23781
42104   44663
64630   46771
49050   19826
92251   36395
82298   92161
87431   90814
48735   97112
63297   84056
10242   96191
15536   10212
68342   55243
26369   80824
96578   69322
80436   82624
68000   92957
79933   15335
63448   10920
15201   33091
96589   54593
20892   10212
51320   75766
89063   55594
65447   55243
69822   17782
42234   76245
85711   25012
68441   47803
16247   26624
79340   97112
47625   85959
23346   45152
13216   57163
46823   12437
34734   97112
31009   44104
30966   62410
29816   11109
44296   62522
91146   93176
87497   43586
32766   76415
51035   10212
71296   55243
75426   55243
28710   98182
21499   83921
49897   93701
11047   75602
19301   83921
71952   55644
53953   29216
65252   53928
11297   44892
69216   63943
75593   47230
64588   33871
33596   27248
87795   22452
75735   23770
18984   82627
70964   50713
25012   40595
64376   68992
79130   92161
70928   83921
28105   46123
75311   75766
64681   50077
80149   47230
83384   49779
81964   79495
61988   91817
78530   72933
25077   84903
26746   89143
79841   96589
80091   97112
74009   58619
22015   89474
43335   53663
67290   93176
26972   93176
52053   54753
71797   48683
29863   70453
58622   87355
39688   22485
98551   61312
32935   86934
21503   87030
43145   47014
52037   75766
31154   54749
78771   63537
74726   72016
22627   79449
91490   58619
12378   91998
13791   54593
92309   81031
97743   10488
46991   21503
43379   21503
68578   37930
20747   47481
57979   49166
80764   54749
59937   80861
38023   73245
36777   55594
11134   43268
47553   35055
51697   36843
59588   76415
85954   79495
95116   22452
78383   88263
74457   21503
44750   23198
96943   48662
70595   67297
38495   41302
99282   85959
19789   31234
14657   16129
30453   93292
93006   34741
15549   22452
33189   41302
93264   76547
16879   40208
46625   50077
88328   70606
57696   18759
60422   62378
83887   51563
92370   38878
41866   27454
34293   49166
83169   81581
34596   57686
19560   76071
19908   46014
63265   43382
19655   58619
16129   22452
17838   27565
70807   93176
62466   77102
57211   76759
60411   44104
21273   17788
59649   97112
73223   20907
58619   35350
35738   31884
27293   11323
67969   52518
92182   97420
39381   40446
68568   43023
58113   35379
97245   41469
75766   90083
91865   74124
12934   36845
76019   38641
48986   54749
73496   25012
93379   21605
88146   48770
47797   59580
33006   29227
42707   97112
23721   66473
86828   18440
14394   79994
61565   35379
54593   50880
85724   22452
64482   32957
43344   21503
95699   25992
35083   12351
11406   38997
97112   90114
98420   25012
39795   49166
57669   97112
78923   76321
63818   10212
17069   41302
71609   17287
11979   10024
91958   58619
63742   26084
34252   66795
68540   14997
50641   83481
47078   62283
53520   58619
79753   25578
31556   85959
86806   78396
64837   77295
46299   35061
10178   53643
51271   34592
70164   50040
75382   74994
96328   84339
14474   18893
73953   52647
41992   22452
20774   46788
38943   97112
50706   47230
32552   49166
69499   45525
82320   41302
14284   35506
21129   18163
26033   54749
95841   94117
75943   49792
74166   85487
27422   55594
99070   38411
67909   21503
68155   20217
46712   95309
89923   45279
52140   93176
44691   44104
22882   93176
27130   54749
87675   66254
89247   51315
65642   18761
62227   41302
79684   19736
58150   42772
38963   79221
91347   44220
74372   15945
79880   49166
15344   22021
81435   53735
31720   95309
20893   53573
21428   97112
77219   50254
93168   79652
46470   22799
13916   54343
44571   10212
78253   75448
53441   69271
56604   59124
83031   57354
73221   85959
70286   85602
23558   71319
62792   93833
91565   79844
87897   55243
24942   90862
77979   46204
90706   61262
17540   48178
18849   81415
83764   91998
28524   16518
93176   83921
50231   44104
84711   47230
72984   52209
71275   47230
52221   11747
30372   41302
30491   58619
93725   52746
46123   29982
92682   75766
16791   25011
57080   50855
47889   59729
16588   81297
14075   48108
80217   96589
98665   70670
48993   55243
91736   41302
22932   78151
33131   69055
37822   77210
10510   43894
76205   93265
17602   35218
21795   62616
70951   55594
50038   93701
52201   16129
28495   73598
15447   42046
59435   70569
98043   75766
22452   54749
35291   31377
63005   10212
14067   21992
82541   25012
29993   96165
85783   59975
23967   72432
57653   52100
10791   58619
37026   22111
79495   55594
97207   49166
24762   88906
24334   72863
27419   93701
79024   75966
86102   17800
46419   54562
34920   11321
58941   49166
17314   61455
17973   70453
24639   72312
42333   76831
13105   39302
91291   40186
23180   98335
84749   49166
87013   87375
88076   98205
77537   52198
91923   47230
55594   67158
76558   87324
92161   69424
39570   35102
56125   58619
86910   60084
65214   47557
69772   75766
31965   25012
10787   54355
77598   83921
56571   93619
42570   68150
41380   46042
86959   55243
81566   37677
30393   30036
55306   34684
66852   87858
58522   44104
13778   71928
86536   54593
42608   91638
20104   41606
63473   85959
62223   67538
87086   10212
87362   51946
16601   55594
88987   25012
45833   44104
54847   55243
41811   10212
86186   50040
85959   41302
84368   47230
60047   76415
36271   48161
34552   57354
40260   25012
22485   75766
12864   54749
29790   94926
53753   99080
95354   55243
75656   92251
63218   70114
72838   66217
83900   86625
50686   47230
73375   20626
44389   40350
37107   41302
42017   52198
40010   79495
24899   16129
88484   90297
54749   61453
56650   15943
24261   22452
30705   58404
84721   83818
57738   58760
58394   67066
86517   67505
18834   55594
19773   49166
62524   18019
71111   54448
16209   96301
87316   22485
15921   39505
83605   21276
51080   32589
16575   21128
31651   49166
66721   94774"""

# split text input
lines = input.split("\n")
lines = [line.strip() for line in lines]
list_1 = []
list_2 = []

for line in lines:
    line = line.split("   ")
    list_1.append(int(line[0]))
    list_2.append(int(line[1]))

print(paired_distance(list_1, list_2))
# 1590491
