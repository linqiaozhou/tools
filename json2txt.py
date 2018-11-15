#coding=utf-8
'''convert .json file to .txt for darknet 
'''
import os
import json
def json2txt(folder_path):
    file_list=[os.path.join(root,fn) for root,dir,files in os.walk(folder_opah) for fn in files]
    label='behavior_head'
    idx=0 #label index
    for file in file_lists:
        if file.endswith(json):
            json_obj=None
            with open(file) as f:
                json_obj=json.loads(f.read())
            txt_path=file[0:-4]+'.txt'
            new_txt=open(txt_path,'w+')
            if not json_obj.__contains__(label):
                new_txt.close()
                continue
            idx=0
            bbs_list=json_obj[labels]
            for bb in bbs_list:
                x1,y1 = bb[u'rect'][0][0].encode('utf-8'),bb[u'rect'][0][1].encode('utf-8')
                x2,y2 = bb[u'rect'][1][0].encode('utf-8'),bb[u'rect'][1][1].encode('utf-8')
                x1,x2=float(x1)/8192,float(x2)/8192  #convert coord
                y1,y2=float(y1)/8192,float(y2)/8192
                norm_cx,norm_cy =(x1+x2)/2,(y1+y2)/2
                norm_w,norm_h =(x2-x1),(y2-y1)
                new_txt.write('%d %f %f %f %f\n'%(idx,norm_cx,norm_cy,norm_w,norm_h))
                
