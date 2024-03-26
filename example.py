import winccpy
import time
con = winccpy.Client()
conn = con.connection("CGOK-ARM1\\WINCC", "CC_HMI_9HMA_20_12_17_11_52_17R")
while True:
    result = con.query(tagId='1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;24;25;26;27;28;29;30;31;32;33;34;35;36;37;38;39;40;41;42;43;44;45;46;47;48;49;50;151;141', dateStart='0000-00-00 00:00:25:000', dateEnd='0000-00-00 00:00:00:000')
    resDict = con.unique(result)
    for i in result:
        print i
    print resDict
con.close()

