from selenium import webdriver

import time
import threading

browser=webdriver.Chrome()
#�����½ҳ��
browser.get('https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/')

#��½
def login(number,password):
    phone_number=browser.find_element_by_id('lUsername')#ͨ��id��λ���ֻ�����
    pwd=browser.find_element_by_id('lPassword')#����
    login_btn=browser.find_element_by_class_name('wall-sub-btn')#��½��ť

    phone_number.send_keys(number)#�����ֻ�����
    pwd.send_keys(password)#��������
    login_btn.click()#�����½��ť

 #ת��������Ƶҳ��
def to_course(key):

    time.sleep(5)
    current=browser.current_window_handle#��ǰҳ��ľ��
    key=browser.find_element_by_partial_link_text(key)#�ҵ��γ�
    key.click()#��ת��������Ƶҳ��
    time.sleep(1)#�ȴ�ҳ�����
   #��Ϊ��ת���µ�ҳ�棬����browserҪ�л����µ�ҳ�����
    handles=browser.window_handles
    for handle in handles:
          if handle!=current:
             browser.switch_to.window(handle)

    time.sleep(10)
    try:
        video=browser.find_element_by_id('mediaplayer')#��λ��Ƶ����
        video.click()#�������
    except:
         pass



#�ж��Ƿ��д��ⴰ�ڵ���
def is_exist():
    while True:
         try:
             browser.switch_to.default_content()
             browser.switch_to.frame('tmDialog_iframe')#���ⴰ������һ��frame���棬Ҫ�л�
             box=browser.find_elements_by_class_name('answerOption')#�����б�
             radio=box[0].find_element_by_tag_name('input')#�ҵ���һ��ѡ��
             radio.click()  #ѡ��
             browser.switch_to.default_content()
             browser.find_element_by_link_text('�ر�').click()#�رմ��ⴰ��
         except:
             browser.switch_to.parent_frame()#û�е������л��ر�����frame
         time.sleep(5)

#�жϵ�ǰ��Ƶ�Ƿ����
def is_end():
     while True:
         try:
            video=browser.find_element_by_id('mediaplayer')#��λ��Ƶ����
            #��ȡ��ǰ���ŵĽ���
            current_time=video.find_element_by_class_name('currentTime').get_attribute('textContent')
            #����Ƶ����ʱ��
            total_time=video.find_element_by_class_name('duration').get_attribute('textContent')
            print(current_time,total_time)
            if current_time==total_time:
                #��ǰ��Ƶ���Ž����������һ��
                js="document.ElementById('nextBtn').click()"#js�ű�
                browser.execute_script(js)
                time.sleep(10)     #10����һ��
         except:
            current_time='00:00'
            total_time= '00:01'



 if __name__=='__main__':

    '''
     number=''#�ֻ�����
     password=''#����
    key=''#�γ����ƣ����Բ�������
           
     '''
    login(number,password)
    to_course(key)
    #�������߳�
    t1=threading.Thread(target=is_exist)
    t2=threading.Thread(target=is_end)
    t2.start()
    time.sleep(3)
    t1.start()
    t2.join()
    t1.join()