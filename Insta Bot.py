import time
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys


class instaBot:

    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password


    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(1)
        user_name = self.driver.find_element_by_xpath('//input[@name = "username"]')
        user_name.clear()
        user_name.send_keys(self.username)
        pass_word = self.driver.find_element_by_xpath('//input[@name = "password"]')
        pass_word.clear()
        pass_word.send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        time.sleep(5)
        self.driver.get('https://www.instagram.com/' + str(self.username))
        # self.driver.get('https://www.instagram.com/')
        # if (self.driver.find_element_by_xpath('//div[@role = "dialog"]').is_displayed()):
        #    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        #   time.sleep(1)
        #   self.driver.get('https://www.instagram.com/' + str(self.username))
        # elif (self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div').is_displayed()):
        #   self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        #   time.sleep(1)
        #   self.driver.get('https://www.instagram.com/' + str(self.username))


    def Quit(self):
        self.driver.quit()


    def make_list(self, list_xpath):
        self.driver.find_element_by_xpath(list_xpath).click()
        time.sleep(5)
        win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
        last_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
        time.sleep(1)
        while True:
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", win)
            time.sleep(1)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
            time.sleep(1)
            if new_height == last_height:
                break
            last_height = new_height
        follower_list_link = self.driver.find_elements_by_tag_name('a')
        my_list = [i.get_attribute('title') for i in follower_list_link if '' != i.get_attribute('title')]
        print(my_list)
        return my_list


    def make_list_of_a_list_of_targets(self, target, list_xpath):
        targets = target.split("','")
        full_list = []
        for i in range(len(targets)):
            self.driver.get('https://www.instagram.com/' + str(targets[i]))
            time.sleep(2)
            self.driver.find_element_by_xpath(list_xpath).click()
            time.sleep(4)
            win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
            last_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
            while True:
                self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", win)
                time.sleep(2)
                new_height = self.driver.execute_script("return arguments[0].scrollHeight", win)
                time.sleep(2)
                if new_height == last_height:
                    break
                last_height = new_height
            follower_list_link = self.driver.find_elements_by_tag_name('a')
            new_list = [i.get_attribute('title') for i in follower_list_link if '' != i.get_attribute('title')]
            full_list = full_list + new_list
            full_list = list(dict.fromkeys(full_list))
            print(full_list)
        # you can remove some one you want from your list in here
        exception_list = []
        full_list = [x for x in full_list if x not in exception_list]
        print(full_list)

        return full_list


    def follow_request_acceptor(self, waite):
        self.driver.get('https://www.instagram.com/accounts/privacy_and_security/')
        self.driver.find_element_by_xpath('//*[@id="accountPrivacy"]/label/div').click()
        time.sleep(1)
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button[1]').click()
            self.driver.get('https://www.instagram.com/' + str(self.username))
            time.sleep(waite)
            self.driver.refresh()
            self.driver.get('https://www.instagram.com/accounts/privacy_and_security/')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="accountPrivacy"]/label/div').click()
        except:
            pass

    def follow_people_in_suggestion_list(self, num):
        self.driver.get('https://www.instagram.com/explore/people/suggested/')
        time.sleep(2)

        for i in range(num):
            try:
                 self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + str(i + 1) + ']/div[3]/button').click()
                 time.sleep(1)
                 print(str(i) + 'id is followed')
                 self.driver.execute_script('scroll(0,' + str(i * 50) + ')')
                 time.sleep(1)
            except:
                pass

    def follow_like_list_of_explorhashtags_post(self, num_of_opening_post, num_of_follow_of_every_post,num_of_opening_hashtag,hashtag):
        hashtags = hashtag.split('#')

        for h in range(num_of_opening_hashtag):
            self.driver.get('https://www.instagram.com/explore/tags/' + str(hashtags[random.randint(0,len(hashtags) - 1)]) + '/')
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            link = self.driver.find_elements_by_tag_name('a')
            posts_links = [l.get_attribute('href') for l in link if '.com/p/' in l.get_attribute('href')]

            for i in range(num_of_opening_post):
                self.driver.get(posts_links[random.randint(0 , len(posts_links) - 1)])
                time.sleep(2)

                try:
                   self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[2]/div/div/button').click()
                   time.sleep(2)
                   for j in range(num_of_follow_of_every_post):
                        check_text = self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/div/div/div[' + str(j + 1) + ']/div[3]/button').text
                        win = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div')
                        if check_text == 'Follow':
                            self.driver.find_element_by_xpath(
                            '/html/body/div[4]/div/div/div[2]/div/div/div[' + str(j + 1) + ']/div[3]/button').click()
                            time.sleep(2)
                            print(str(j + 1) + 'id followe from ' + str(i + 1) + 'post and' + str(h + 1) + 'hashtag')

                        else:
                            self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                            time.sleep(2)

                except:
                    pass


    def follow_list_of_someting_of_ids(self, id, num, list_xpath):
        ids = id.split(',')
        for i in range(len(ids)):
            self.driver.get('https://www.instagram.com/' + str(ids[i]))
            time.sleep(2)
            self.driver.find_element_by_xpath(list_xpath).click()
            time.sleep(4)

            for j in range(num):
               if j <= 5:
                check_text = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[3]/button').text
                win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
                if check_text == 'Follow':
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[3]/button').click()
                    time.sleep(2)
                else:
                    self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                    time.sleep(2)

               elif j > 5:
                   check_text = self.driver.find_element_by_xpath(
                       '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[2]/button').text
                   win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
                   if check_text == 'Follow':
                       self.driver.find_element_by_xpath(
                           '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[2]/button').click()
                       time.sleep(2)
                   else:
                       self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                       time.sleep(2)


    def unfollow(self,num):
        self.driver.get('https://www.instagram.com/' + str(self.username))
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        for j in range(num):
          try:
            if j <= 6:
                check_text = self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[3]/button').text
                win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
                if check_text == 'Following':
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[3]/button').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
                    time.sleep(1)
                    self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                    time.sleep(1)
                    print(str(j + 1) + ' follower unfollowed')

                else:
                    self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                    time.sleep(2)

            elif j > 6:
                check_text = self.driver.find_element_by_xpath(
                    '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[2]/button').text
                win = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
                if check_text == 'Following':
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div[2]/ul/div/li[' + str(j + 1) + ']/div/div[2]/button').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
                    time.sleep(1)
                    self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                    time.sleep(1)
                    print(str(j + 1) + ' follower unfollowed')
                else:
                    self.driver.execute_script("arguments[0].scrollTo(0, " + str(j * 42) + " );", win)
                    time.sleep(2)
          except:
               pass


    def unfollow_who_desent_follow_back(self,num):
        self.driver.get('https://www.instagram.com/' + str(self.username))
        time.sleep(2)
        follower_list = instaBot.make_list(self,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.driver.get('https://www.instagram.com/' + str(self.username))
        time.sleep(2)
        folloing_list = instaBot.make_list(self,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        no_follow_back_list = [x for x in folloing_list if x not in follower_list]
        print(no_follow_back_list)
        try:
         for i in range(num):
            self.driver.get('https://www.instagram.com/' + str(no_follow_back_list[i]))
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
            time.sleep(1)
        except:
            pass

    def unfollow_a_nofollowback_list_txtfile(self,num,directori):
       file = open(directori, mode="r+")
       a = file.read()
       remaind_list = a.split("','")
       for i in range(num):
           try:
                   self.driver.get('https://www.instagram.com/' + str(remaind_list[i]))
                   time.sleep(3)
                   self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
                   time.sleep(1)
                   self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                   print(str(i + 1) + 'id' + str(remaind_list[i]) + ' unfollowed')

                   del remaind_list[0:1]
                   file.truncate(0)
                   file.seek(1)
                   file.write(str(remaind_list))
           except:
               del remaind_list[0:1]
               file.truncate(0)
               file.seek(1)
               file.write(str(remaind_list))

       print(str(len(remaind_list)) + 'are remaining to unfollow')
       file.close()



    def unfollow_a_nofollowback_selebritylist_txtfile(self, num, directori):
        file = open(directori, mode="r+")
        a = file.read()
        remaind_list = a.split("','")
        for i in range(num):
            try:
                self.driver.get('https://www.instagram.com/' + str(remaind_list[i]))
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                print(str(i + 1) + 'id' + str(remaind_list[i]) + ' unfollowed')


            except:
               pass

        print(str(len(remaind_list)) + 'are remaining to unfollow')
        file.close()



    def unfollow_spampages_from_a_txtfile(self,num,directori):
        file = open(directori, mode="r+")
        a = file.read()
        remaind_list = a.split("', '")
        for i in range(num):
            try:
                self.driver.get('https://www.instagram.com/' + str(remaind_list[i]))
                time.sleep(3)
                num_of_following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
                if(int(num_of_following) > 1000):
                    self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                    print(str(remaind_list[i]) + ' cheked')
                    del remaind_list[0:1]
                    file.truncate(0)
                    file.seek(1)
                    file.write(str(remaind_list))
            except:
                del remaind_list[0:1]
                file.truncate(0)
                file.seek(1)
                file.write(str(remaind_list))

        print(str(len(remaind_list)) + 'are remaining to check')
        file.close()



    def like_timeline_posts(self, num):
        self.driver.get('https://www.instagram.com/')
        time.sleep(1)
        self.driver.execute_script('scroll(0,300)')
        for i in range(num):
            time.sleep(1)
            self.driver.execute_script('scroll(0,' + str((i + 1) * 800) + ')')
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[' + str(
                    i + 1) + ']/div[2]/section[1]/span[1]/button').click()


    def block_a_list(self,num):
        file = open("C:\\Users\\asus\\Desktop\\Instagram Bot\\remaindlist_backup.txt", mode="r+")
        a = file.read()
        remaind_list = a.split("', '")
        for i in range(num):
             try:
                self.driver.get('https://www.instagram.com/' + str(remaind_list[i]))
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button').click()
                time.sleep(1)
                chek = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[1]').text
                print(chek)
                if chek == 'Block this user':
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button[1]').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/button').click()
                    time.sleep(3)
                    print(str(remaind_list[i]) + ' blocked')
                    del remaind_list[0:1]
                    file.truncate(0)
                    file.seek(1)
                    file.write(str(remaind_list))
                else:
                    del remaind_list[0:1]
                    file.truncate(0)
                    file.seek(1)
                    file.write(str(remaind_list))

             except:
                 pass



        print(str(len(remaind_list)) + 'are remaining to block')
        file.close()





    def follow_privetpags_an_idlist(self,num,directory):
        file = open(directory, mode="r+")
        a = file.read()
        follower_list = a.split("', '")
        b = 0
        for i in range(num):

          try:
            self.driver.get('https://www.instagram.com/' + str(follower_list[i]))
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()
            time.sleep(1)
            b = b + 1
            print(str(b) + 'id followed')
            del follower_list[0:1]
            file.truncate(0)
            file.seek(1)
            file.write(str(follower_list))
            
          except:
              del follower_list[0:1]
              file.truncate(0)
              file.seek(1)
              file.write(str(follower_list))

        print(str(len(follower_list)) + 'are remaining to follow')
        file.close()



    def follow_publicpags_an_idlist(self, num, directory):
        #with out deleting the ids in the list
        file = open(directory, mode="r+")
        a = file.read()
        follower_list = a.split("','")
        b = 0
        for i in range(num):

            try:
                self.driver.get('https://www.instagram.com/' + str(follower_list[i]))
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
                time.sleep(1)
                b = b + 1
                print(str(b) + 'id followed')


            except:
                pass

        print(str(len(follower_list)) + 'are remaining to follow')
        file.close()


#######################################################################################################








    def follow_list_by_id_2(self, id, num, list_xpath):
        ids = id.split(',')
        for i in range(len(ids)):
            self.driver.get('https://www.instagram.com/' + str(ids[i]))
            time.sleep(2)
            self.driver.find_element_by_xpath(list_xpath).click()
            time.sleep(5)

            for j in range(num):

                Element = self.driver.find_element_by_xpath('//button[@class="sqdOP.L3NKy.y3zKF"]')
                self.driver.execute_script("arguments[0].scrollIntoView();",Element)
                Element.click()








    def follow_followers_by_id_2(self, id):
        ids = id.split(',')
        for i in range(len(ids)):
            self.driver.get('https://www.instagram.com/' + str(ids[i]))
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(2)
            link_list = [self.driver.find_elements_by_tag_name('a')]
            self.driver.get

    def like_timeline_posts_2(self, num):
        self.driver.get('https://www.instagram.com/')

        link = []
        while len(link) < num:
            link = self.driver.find_elements_by_tag_name('a')
            self.driver.execute_script('scroll(0,' + str(len(link) * 100) + ')')
            time.sleep(2)

            posts_links = []
            for l in link:
                if 'com/p/' in l.get_attribute('href'):
                    posts_links.append(l.get_attribute('href'))
                    for p in range(len(posts_links)):
                        self.driver.get(posts_links[l])
                        time.sleep(2)
                        # self.driver.find_element_by_class_name('wpO6b').click()

    def like_hashtag_posts(self, hashtag, num):
        hashtags = hashtag.split(',')
        for i in range(len(hashtags)):
            self.driver.get('https://www.instagram.com/explore/tags/' + str(hashtags[i]))
            link = []
            while len(link) < num:
                self.driver.execute_script('scroll(0,' + str(len(link) * 100) + ')')
                link = self.driver.find_elements_by_tag_name('a')

            posts_links = []

            for l in link:
                if 'com/p/' in l.get_attribute('href'):
                    posts_links.append(l.get_attribute('href'))

                for l in range(len(posts_links)):
                    self.driver.get(posts_links[l])
                    self.driver.find_element_by_class_name('wpO6b').click()
                    # num_like += 1
                    # if (num_like > 700):
                    # break

    def like_hashtag_posts_2(self, hashtag, num):
        hashtags = hashtag.split(',')
        for i in range(len(hashtags)):
            self.driver.get('https://www.instagram.com/explore/tags/' + str(hashtags[i]))
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click()
            time.sleep(5)
            for j in range(0, num):
                self.driver.find_element_by_class_name('wpO6b').click()
                time.sleep(2)
                self.driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow').click()

    def story_seen(self):
        self.driver.get('https://www.instagram.com/')
        if self.driver.find_element_by_xpath('/html/body/div[4]/div').is_displayed():
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            self.driver.find_element_by_css_selector('canvas.CfWVH').click()

    def make_a_list_of_my_followers(self):
        self.driver.get('https://www.instagram.com/' + str(self.username))
        time.sleep(3)
        num_myfollowers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        list_of_my_followers = []

        for i in range(int(num_myfollowers) // 20):
            list_of_my_followers = self.driver.find_elements_by_tag_name('a')
            list_of_my_followers = list(dict.fromkeys(list_of_my_followers))
            time.sleep(1)
            followers_window = self.driver.find_element_by_xpath('//div[@class="isgrP"]')
            self.driver.execute_script("return arguments[0].scrollHeight", followers_window)

        print(list_of_my_followers)




id1 = instaBot('__sr.mdi', '************')
id1.login()

#id1.unfollow_spampages_from_a_txtfile(20,'C:\\Users\\asus\\Desktop\\Instagram Bot\\sarafallowinglist.txt')
#id1.follow_privetpags_an_idlist(50,"C:\\Users\\asus\\Desktop\\Instagram Bot\\koslist.txt")
id1.follow_publicpags_an_idlist(50,"C:\\Users\\asus\\Desktop\\Instagram Bot\\selebriti.txt")
#id1.follow_publicpags_an_idlist(50,"C:\\Users\\asus\\Desktop\\Instagram Bot\\foreigner_selebriti.txt")
#id1.unfollow_a_nofollowback_selebritylist_txtfile(50,"C:\\Users\\asus\\Desktop\\Instagram Bot\\selebriti.txt")
#id1.unfollow_a_nofollowback_selebritylist_txtfile(50,"C:\\Users\\asus\\Desktop\\Instagram Bot\\foreigner_selebriti.txt")
#id1.block_a_list(100)
#id1.unfollow_a_nofollowback_list_txtfile(70,"C:\\Users\\asus\\Desktop\\Instagram Bot\\saraunfollowlist.txt")
#id1.follow_people_in_suggestion_list(50)
#id1.follow_request_acceptor(10)
id1.Quit()

####################################################################################################



id3 = instaBot('nastaran._.tx','*********')
id3.login()
#id3.follow_privetpags_an_idlist(100,"C:\\Users\\asus\\Desktop\\Instagram Bot\\sharif_follower.txt")
id3.follow_people_in_suggestion_list(50)
id3.Quit()


######################################################################################################


id2 = instaBot('bita._.18charkh','********')
id2.login()
id2.follow_people_in_suggestion_list(70)
#id2.unfollow_who_desent_follow_back(50)
#id2.unfollow_a_nofollowback_list_txtfile(60,"C:\\Users\\asus\\Desktop\\Instagram Bot\\bitaunfollowlist.txt")
id2.unfollow(30)
id2.follow_request_acceptor(10)
id2.Quit()
