import argparse,sys

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--path", type=str, default='')
parser.add_argument("--sounds", type=str, default='./Sounds/')
args = parser.parse_args()

def uhelp():
    print('\nSing On The Bytes V1.0')
    print('By OdorajBotoj')
    print('\n执行格式: python3 ./SOTB.py --path=<曲谱位置> [ --sounds=<音源目录,默认\'./Sounds/\'>]')
    print('已知问题:声音源文件时长不一\n\n')
uhelp()

def wri_mus(lst):
    sys.path.append(args.sounds)
    import music_dict
    m_cla = music_dict.m_d()
    m_dic = m_cla.md
    with open('out.mp3','wb') as out_mus_f:
        for i in lst:
            j = str()
            j = m_dic.get(i)
            mus_fn = open(str(args.sounds + j),'rb')
            out_mus_f.write(mus_fn.read())
            mus_fn.close()
    return

if args.path:
    try:
        music_flie = open(args.path,'r',encoding='utf-8')
        m_f_str = music_flie.read()
        music_flie.close()
    except Exception:
        print('打开源文件失败!')
        music_flie.close()
        exit()
    m_f_lst = list(m_f_str)
    wri_mus(m_f_lst)
    print('完成,已输出至out.mp3\n\n')
else:pass

