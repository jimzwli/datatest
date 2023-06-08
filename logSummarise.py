class LogSummarise:
    def __init__(self, system_name: str, issues: [], app_link): 

        self.system_name = system_name        
        self.link = app_link

        red_count = 0
        yellow_count = 0
        resource_a = 'Health'
        resource_b = 'Health'
        is_resource_a_red = False
        is_resource_b_red = False
        is_resource_a_amber = False
        is_resource_b_amber = False
    
        for issue in issues:
            issue_att = issue.get_attributes()
            issue_name = issue_att['issue_name']
            issue_resource= issue_att['issue_resource']
            state_value = issue_att['state_value']
            time_to_red = issue_att['time_to_red']
            if state_value == 'r':
                red_count += 1
            if state_value == 'a':
                yellow_count += 1
            if issue_att['issue_resource'].upper() == 'Z1' and state_value == 'r':
                resource_b = 'Non Health'
                is_resource_b_red = True
            if issue_att['issue_resource'].upper() == 'Z1' and state_value == 'a' and resource_b == 'Health':
                resource_b = 'To Down'    
            if issue_att['issue_resource'].upper() == 'A1' and state_value == 'r':
                resource_a = 'Non Health'
                is_resource_a_red = True
            if issue_att['issue_resource'].upper() == 'A1' and state_value == 'a' and resource_b == 'Health':
                resource_a = 'To Down'                 

            if issue_att['issue_resource'].upper() == 'Z1' and state_value == 'a':
                is_resource_b_amber = True 
            if issue_att['issue_resource'].upper() == 'A1' and state_value == 'a':
                is_resource_a_amber = True        

        self.red = red_count
        self.yellow = yellow_count 
        self.resource_a = resource_a
        self.resource_b = resource_b 
        self.is_resource_a_red = is_resource_a_red
        self.is_resource_b_red = is_resource_b_red
        self.is_resource_b_amber = is_resource_b_amber
        self.is_resource_a_amber = is_resource_a_amber      

    def get_attributes(self):
        return self.__dict__
