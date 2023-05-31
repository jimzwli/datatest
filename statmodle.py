class AppStat:
    def __init__(self, application_name: str, issues: [], app_link): 

        self.application_name = application_name        
        self.link = app_link
        
        red_count = 0
        yellow_count = 0
        env_prod = 'Compliant'
        env_non = 'Compliant'
        is_env_prod_red = False
        is_env_non_red = False
        is_env_prod_amber = False
        is_env_non_amber = False
        issue_worst_case = {}
        for issue in issues:
            issue_att = issue.get_attributes()
            issue_name = issue_att['issue_name']
            issue_env = issue_att['issue_env']
            score_value = issue_att['score_value']
            time_to_red = issue_att['time_to_red']
            if score_value == 'r':
                red_count += 1
            if score_value == 'a':
                yellow_count += 1
            if issue_att['issue_env'].upper() == 'NON' and score_value == 'r':
                env_non = 'Non Compliant'
                is_env_non_red = True
            if issue_att['issue_env'].upper() == 'NON' and score_value == 'a' and env_non == 'Compliant':
                env_non = 'Due Soon'    
            if issue_att['issue_env'].upper() == 'PROD' and score_value == 'r':
                env_prod = 'Non Compliant'
                is_env_prod_red = True
            if issue_att['issue_env'].upper() == 'PROD' and score_value == 'a' and env_non == 'Compliant':
                env_prod = 'Due Soon'                 
            
            if issue_att['issue_env'].upper() == 'NON' and score_value == 'a':
                is_env_non_amber = True 
            if issue_att['issue_env'].upper() == 'PROD' and score_value == 'a':
                is_env_prod_amber = True 


                
            if time_to_red is not None:
                if issue_name in issue_worst_case:
                    previous_time_to_red = issue_worst_case[issue_name] 
                    print(f'previous time to red for {issue_name} in {application_name} is {previous_time_to_red}')
                    if time_to_red > previous_time_to_red:
                        issue_worst_case[issue_name] = time_to_red
                    else:
                        continue
                else:
                    issue_worst_case[issue_name] = time_to_red
            if issue_name not in issue_worst_case:
                issue_worst_case[issue_name] = -9999            
                
        self.red = red_count
        self.yellow = yellow_count 
        self.env_prod = env_prod
        self.env_non = env_non
        self.issue_worst_case = issue_worst_case  
        self.is_env_prod_red = is_env_prod_red
        self.is_env_non_red = is_env_non_red
        self.is_env_non_amber = is_env_non_amber
        self.is_env_prod_amber = is_env_prod_amber      

    def get_attributes(self):
        return self.__dict__
