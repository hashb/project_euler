'''
from math import sqrt
X_Values = []
D_Values = []

for D in xrange(2,1001):
    if sqrt(D) == int(sqrt(D)): continue
    x=0.1
    y=1
    while x != int(x):
        x = sqrt(1 + (D*(y**2)))
        y+=1
    print D
    D_Values.append(D)
    X_Values.append(x)

print max(X_Values),X_Values.index(max(X_Values)),D_Values.index(X_Values.index(max(X_Values)))
'''
data = [3,2,9,5,8,3,19,10,7,649,15,4,33,17,170,9,55,197,24,5,51,26,127,9801,11,1520,17,23,35,6,73,37,25,19,2049,13,3482,199,161,24335,48,7,99,50,649,66249,485,89,15,151,19603,530,31,1766319049,63,8,129,65,48842,33,7775,251,3480,17,2281249,3699,26,57799,351,53,80,9,163,82,55,285769,10405,28,197,500001,19,1574,1151,12151,2143295,39,49,62809633,99,10,201,101,227528,51,41,32080051,962,1351,158070671986249,21,295,127,1204353,1025,1126,9801,649,306917,120,11,243,122,4620799,930249,449,4730624,577,16855,6499,10610,23,2588599,145925,244,35,6083073,47,77563250,71,95,143,12,289,145,97,73,25801741449,49,1728148040,37,2177,21295,249,25,46698728731849,7743,1324,721,11775,19601,64080026,2049,1079,1700902565,168,13,339,170,24248647,2499849,1451,2024,199,62423,1601,4190210,161,2469645423824185801,27,487,24335,9249,7501,1682,4607,55,52021,8994000,97,6224323426849,195,14,393,197,16266196520,99,515095,19731763,57,4999,39689,59535,1151,649,46551,29,278354373650,66249,194399,695359189925,44,485,3844063,126003,74,89,1665,149,224,15,451,226,151,5848201,91,76,19603,1072400673,5201,46,561799,228151,11663,6195120,31,10085143557001249,19601,70226,1766319049,51841,88805,85292,63,8553815,39480499,3674890,127,3222617399,255,16,513,257,847225,129,192119201,104980517,139128,65,73738369,685,2402,4771081927,13449,5291,115974983600,33,727,3959299,199,7775,159150073798980475849,2501,1520,251,2262200630049,2351,138274082,24220799,2431,561835,288,17,579,290,2281249,12320649,4801,2024999,3699,48599,335473872499,415,1351,5883392537695,4276623,2524,57799,489,35,88529282,351,64202725495,848719,16883880,53,32188120829134849,392499,71,12799,248678907849,107,12901780,161,215,323,18,649,325,217,163,2376415,109,2785589801443970,13447,73,63804373719695,604,55,2063810353129713793,114243,97970,285769,10626551,37,130576328,10405,6761,17299,641602,1567,169648201,449,62425,77617,10157115393,258065,954809,500001,3401,176579805797,360,19,723,362,4954951,23915529,907925,19019995568,1151,8396801,213859,1695,12151,52387849,3365,15124,2143295,233,8749,12941197220540690,39,1015,164998439999,18768,4801,95831,111555,3482,62809633,3287049,79,7338680,99,46437143,312086396361222451,159,199,838721786045180184649,399,20,801,401,669878,201,161,59468095,2663,101,25052977273092427986049,81,49730,103537981567,113399,24335,18412804,5201,85322647,33857,270174970,41,3879474045914926879468217167061449,7022501,4607,32080051,143649,88751,62,1850887,1524095,2862251,151560720,1351,104564907854286695713,125,146,158070671986249,4599,293,440,21,883,442,295,43468489,110166015,148,127,71798771299708449,19601,46471490,1204353,1653751,16916040084175685,64,1025,6983244756398928218113,22899,499850,2535751,1182351890184201,43,247512720456368,9801,15871,938319425,1625626,649,137215,1691,7838695,306917,87,193549,57799,28799,8777860001,1617319577991743,2989440,241,1859131879201,483,22,969,485,51906073840568,243,7592629975,1039681,93628044170,29767,935662752649,73035,89,4620799,1201887,179777,4490,930249,11242731902975,3832352837,24648,449,809,45,1351,44757606858751,313201220822405001,271,4188548960,665857,13771351,4625,17406,16855,590968985399,2367,14851876,6499,32961431500035201,19603,81810300626,225144199,6049,84056091546952933775,528,23,1059,530,2588599,74859849,3678725,1618804,145925,192349463,9536081203,3970,119071,3707453360023867028800645599667005001,4293183,669337,2449,1961,701,160177601264642,6083073,1766319049,30580901,8380,47,624635837407,60756099699,1814,12032115501124999,27849,7937,506568295,71,522785,220938497,68122,95,435259412378569,95609285,2024,143,16760473211643448449,191,181124355061630786130,287,383,575,24,1153,577,385,289,152071153975,193,8429543,145,33281,33867877212256207699,1907162,97,41423166067036218751,5781,165676,73,721517598849,1098305,18514,25801741449,463287093751,1574351,24686379794520,49,38902815462492318420311478049,687,48842,5972991296311683199,930249,42187499,164076033968,2737,605695,10323982819,236926,2177,464018873584078278910994299849,348291186245,124,21295,3363593612801313,10093,517213510553282930,249,7775,13804370063,624,25,1251,626,46698728731849,123245001,251,48961575312998650035560,7743,440772247,8711856945587257031251,126,3505951,1419278889601,42283,24220799,1039681,2609429220845977814049,5777,1988960193026,11775,1024001,305,120187368,19601,1123593226162199,51,1735,8212499464321351,10499986568677299849,8915765,737709209,2049,2281249,1693,5930,1079,16421658242965910275055840472270471049,1718102501,103,1700902565,13719,27365201,107119097,56447,14226117859054135,5791211,58620,337,4765506835465395993032041249,675,26,1353,677,17792625320,339,10743166003415,1197901,170067682,57799,95592800063517769,10850138895,165337,24248647,105,1471,31138100617500578690,2499849,246401,38782105445014642382885,33639,1451,34849,51999603,2271050,8193151,277631049,53,1159172,79201,237161,34595,2526,62423,665782673992201,1279,80,1601,5286367,4115,75646,35115719688199,6998399,8933399183036079503,403480310400,161,18632176943292415,22619537,242,2469645423824185801,9801,485,728,27,1459,730,487,195307849,10394175,244,24335,252975383,163,98015661073616742153890,9249,7352695,263091151,714024,7501,12769001,61268974069299,82,5658247,1084616384895,2550251,7293318466794882424418960,4607,308526027863,836977699,1209,55,3750107388553,413959717,551,52021,1280001,6349,719724601,161784071999999,285769,145933611945744638015,31212,18817,535781868388881310859702308423201,111,2989136930,6224323426849,3607394696649,10405,4620799,195,223,5964562960504723,11785490,391,67606199,783,28,1569,785,34625394242,393,16116667272575,6616066879,225,197,4393,1828310451,6626,529178298454520220799,1221759532448649,113,424,19601,500002000001,295496099,7226,515095,1514868641,6166395,51841948,19731763,376455160998025676163201,27379,1382072163578616410,57,2167,4206992174549,156644,4999,343,40899,1574,39689,9000987377460935993101449,7397,235170474903644006168,59535,48599,222239304685,900602,1151,479835713751049,146411,9799705,842401,9478657,6552578705,34336355806,46551,12151,42112785797,840,29,1683,842,154962314660167628644999,299537289,2143295,8193151,66249,1501654712948695,2449,8418574,194399,215454135724113414336120649,1294299,3041,695359189925,131822292741249,703,2058844771979643060124010,3871,541601801,358022566147312125503,18524026608,470449,242688628535063329,42435,70226,3844063,60192738698751,59,19442812076,126003,62809633,3725,120126,10951,116476476553,9314703,107245324,89,22606256615916825861249,19601,34878475759617272473442,1665,119,7743524593057655851637765,469224,149,13231974717803657215,179,3970,100351,6091434999,299,359,449,599,899,30,1801,901,601,451,361,301,123823410343073497682,102151,80801,181,371832584927520,151,515734243080407,62563299,121,5848201,823604599,4120901,4481603010937119451551263720,91,2522057712835735,351605368773852499,638,11551,1555849,304560297142335,227528,768555217,13224937103288377430049,61,6681448801,1072400673,75263,3034565,1376,5201,480644425002415999597113107233,17151,122695,4231,1068924905989944201,106133,737,561799,275561,45225786400145,13509645362,228151,609622436806639069525576201,202501,224208076,11663,15090531843660371073,32080051,2095256249,76759023628799,14849,16762522330425599,960,31,1923,962,10085143557001249,446526729,57499,4649532557817485528,19601,13588951,215395035859,12479806786330,9863382151,903223,488825745235215,1249,1766319049,108832847723078562849,118337,360449,51841,158070671986249,8837,284088,88805,332929,49299,377,14549450527,550271588560695,881,379516400906811930638014896080,63,2647,1135,8835999,8553815,14418057673,984076901,102688615,39480499]

print max(data)