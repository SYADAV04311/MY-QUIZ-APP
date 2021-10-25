question_set = {
    1 : ['Bimbisara was the founder of which one of the following dynasties?', 'Haryanka', ['Nanda', 'Shunga', 'Maurya', 'Haryanka']],
    2 : [' A Janapadin was the ___ of a janapada?', 'Ruler', ['servant' , 'Ruler' , 'Minister' , 'Army General']],
    3 : ['The territory of Porus who offered strong resistance to Alexander was situated between the rivers of?', 'Jhelum', ['Jhelum', 'Ravi', 'Sutlej', 'Godavari']],
    4 : [' Champa was the capital of which one of the following Mahajanapadas in Ancient India?', 'Anga', ['Anga', 'kasi', 'Vajji', 'Magadh']],
    5 : ['Wadia Institute of Himalayan Geology is located at?', 'Dehradun', ['Dehradun', 'Kulu', 'Kohima', 'Mizoram']],
    6 : ['Poona pact was signed on?', '1930', ['1930', '1947', '1928', '1957']],
    7 : ['Which Team won the title of ICC World cup 2019?', 'England', ['India', 'Pakistan', 'Australia', 'England']],
    8 : ['Which Team Won the title of Vivo IPL 2021?', 'CSK', ['Delhi capitals', 'CSK', 'KKR', 'Mumbai Indians']],
    9 : ['Which player is at number one in the ranking of ICC T20?', 'Babar Azam', ['Kl Rahul', 'Rohit Sharma', 'Virat Kohli', 'Babar Azam']],
    10: ['Which Bollywood personality has launched an online platform called ‘Pravasi Rojgar’ to help migrants find job opportunities?', 'Sonu Sood', ['Sonu Sood', 'Nawazzuddin siddiqui', 'Salman Khan', 'shahrukh khan']],
    11: ['Which Bollywood personality was named by NITI Aayog to promote the Women Entrepreneurship platform (WEP)?','Sushant Singh Rajput',['Priyanka Chopra', 'Vidya Balan', 'Sushant Singh Rajput', 'Akshay Kumar']],
    12: ['As of 2020, which is the only Bollywood movie to win 13 Filmfare Awards?','Gully Boy',['Uri: The Surgical Strike', 'Gully Boy', 'Saand Ki Aankh', 'Article 15']]
}

level = {
            'e' : [7, 8, 9, 12], 
            'm' : [4, 5, 6, 11], 
            'h' : [1, 2, 3, 10]
        }
count = 0

class quiz_app:
    
    def selected_option(ops):
        ans = input("Please select option: ")
        if ans == 'd':
            return ops[3]
        elif ans == 'c':
            return ops[2]
        elif ans == 'b':
            return ops[1]
        elif ans == 'a':
            return ops[0]
        
    def display_questions(question , options):
        try:
            print ('Question: ' , question)
            print ('(a)' , options[0] , end=' ')
            print ('(b)' , options[1] , end=' ')
            print ('(c)' , options[2] , end=' ')
            print ('(d)' , options[3] )

        except KeyError :
            print ('Oops something went wrong!!')

    def get_question_answer_options(q_no):
        que = question_set[q_no][0]
        ans = question_set[q_no][1]
        ops = question_set[q_no][2]
        return que , ans , ops

    def verify_answer(selected_ans, ans):
        global count
        try :
            if selected_ans in ans:
                print ('Your answer is correct\n')
                count = count + 1
            else :
                print("Your answer is wrong\n")
                print ('This is correct answer:', ans)

        except TypeError:
            print ('The selected option is not correct\n')

    def group_quiz(selected_group):
#         print(selected_group)
        for q_no in selected_group:
            que, ans, ops = quiz_app.get_question_answer_options(q_no)
            quiz_app.display_questions(que, ops)
            selected_answer = quiz_app.selected_option(ops)
            quiz_app.verify_answer(selected_answer, ans)

    def start():
        diff = input ("Select difficulty level 'e' for easy, 'm' for moderate, 'h' for hard :")
        user_name=input("Kindly enter your name: ")
        print ("\nHello ", user_name)
        print ("Hey Welcome to SANDEEP KBC Quiz, let's begin: ")
        quiz_app.group_quiz(level[diff])
        print(user_name, "you have scored ", count)

    def remove_question():
        delete_question =int(input("Kindly enter the question 'key' you want to delete:"))
    #     print(level)
    #     print(level['h'])

        #update the level as well from the level dictionary
        h = level['h']
        h.remove(delete_question)
        level['h'] = h

        m = level['m']
        m.remove(delete_question)
        level['m'] = m

        e = level['e']
        e.remove(delete_question)
        level['e'] = e

        #now delete the question from question dictionary
        del question_set[delete_question]
    #     print(level)

    def add_question():
        diff_level = input ("Kindly enter e: for Easy \n Enter m: for Moderate \n Enter h: for Hard: ")
        question = input ("Please enter new question: ")
        ans = input ("Please enter answer: ")
        ans_op = input ("Kindly enter options comma separated eg: a,b,c,d: ").split (',')
        que_ans = [question , ans, ans_op]
        question_set[len(question_set) + 1] = que_ans
        if diff_level == 'h':
            level['h'].append(len(question_set))
        elif diff_level == 'e':
            level['e'].append(len(question_set))
        elif diff_level == 'm':
            level['m'].append(len(question_set))
        return diff_level , que_ans , ans_op

while True:
    try :
        print ('\n****************HEY WELCOME TO SANDEEP KBC QUIZ*******************')
        print ('Kindly hit 1 for taking Quiz:')
        print ('Kindly hit 2 for SuperUser access:')
        print ('Kindly hit 3 for Exit:')
        option = input('Please select any option:')
        option = int(option)
        if option == 1 :
            quiz_app.start()
        elif option == 2 :
            super_user = input ("Kindly enter super username:")
            if super_user == "SANDEEP YADAV" :

                admin_option = 1
                while admin_option != 4 :
                    try :
                        print('\n***************',super_user,'**************')
                        print('Hit 1 for adding new question :')
                        print('Hit 2 for deleting question :')
                        print('Hit 3 for updating question :')
                        print('Hit 4 to Quit :')
                        admin_option = input('Please select any option: ')
                        admin_option = int(admin_option)
                        if admin_option == 1:
                            quiz_app.add_question()
                        elif admin_option == 2:
                            quiz_app.remove_question()
                        elif admin_option == 3:
                            diff_level = input ("Kindly enter e: for Easy \n Enter m: for Moderate \n Enter h: for Hard")
                            update_question_key =int(input("Kindly enter the question 'key' you want to update:"))
                            question = input ("Please enter new question: ")
                            ans = input ("Please enter answer: ")
                            ans_op = input ("Kindly enter options comma separated eg: a,b,c,d: ").split (',')
                            question_set[update_question_key] = [question , ans, ans_op]
                        elif admin_option == 4:
                            break
                    except ValueError :
                        print ("Kindly enter valid number")

            else :
                print(super_user, "You do not have super user permission, kindly login with super user." )
        elif option == 3:
            exit()
    except ValueError :
        print("Please select correct option")

