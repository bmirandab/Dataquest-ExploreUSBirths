
# coding: utf-8

# In[1]:


def read_csv(filename):
    string_data = open(filename).read()
    string_list = string_data.split("\n")[1:]
    final_list = []
    
    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list
        
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[2]:


cdc_list[0:10]


# In[3]:


def month_births(listname):
    births_per_month = {}
    
    for row in listname:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births        
    return births_per_month

cdc_month_births = month_births(cdc_list)  



# In[4]:


cdc_month_births


# In[5]:


def dow_births(listname):
    day_of_week = {}
    
    for row in listname:
        weekday = row[3]
        births = row[4]
        if weekday in day_of_week:
            day_of_week[weekday] = day_of_week[weekday] + births
        else:
            day_of_week[weekday] = births
    return day_of_week
      
        
cdc_day_births = dow_births(cdc_list)


# In[6]:


cdc_day_births


# In[7]:


def calc_counts(filename, column):
    births_summary = {}
        
    for row in filename:
        column_number = row[column]
        births = row[4]
        if column_number in births_summary:
            births_summary[column_number] = births_summary[column_number] + births
        else:
            births_summary[column_number] = births
    return births_summary

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)
        
        


# In[8]:


cdc_year_births


# In[9]:


cdc_month_births


# In[10]:


cdc_dom_births


# In[11]:


cdc_dow_births


# In[12]:


def calc_minmax(dictionary, time_unit):
    minmax_dict = []
    
    maximum = max(dictionary.keys(), key = (lambda k: dictionary[k]))
    minimum = min(dictionary.keys(), key = (lambda k: dictionary[k]))
    minmax_dict.append({
        "max_births":dictionary[maximum],
        "max_time": maximum,
        "time_unit": time_unit
              })
    minmax_dict.append({
        "min_births": dictionary[minimum],
        "min_time": minimum,
        "time_unit": time_unit
                })
    return minmax_dict

minmax_cdc_year_births = calc_minmax(cdc_year_births, "year")
minmax_cdc_month_births = calc_minmax(cdc_month_births, "month")
minmax_cdc_dom_births = calc_minmax(cdc_dom_births, "day")
minmax_cdc_dow_births = calc_minmax(cdc_dow_births, "weekday") 



# In[13]:


minmax_cdc_year_births


# In[14]:


minmax_cdc_month_births


# In[15]:


minmax_cdc_dom_births


# In[16]:


minmax_cdc_dow_births


# In[17]:


def calc_diff(filename, date_one, date_two, column, column_value):
    birth_rate_result = []
    previous_birth_rate = 0
               
    for row in filename:
        year = row[0]
        current_birth_rate = row[4]
        time_unit = row[column]
        if year in range(date_one,date_two):
            if time_unit is column_value:
                birth_rate_diff = (current_birth_rate - previous_birth_rate)
                if birth_rate_diff > 0:
                    growth_status = "increased"
                    previous_birth_rate = current_birth_rate
                elif birth_rate_diff < 0:
                    growth_status = "decreased"
                    previous_birth_rate = current_birth_rate
                elif birth_rate_diff == 0:
                    growth_status = "static"
                    previous_birth_rate = current_birth_rate
    
                birth_rate_result.append([birth_rate_diff, growth_status,row[0]])
        
    return birth_rate_result
    
        

birth_rate_calc = calc_diff(cdc_list, 1994, 2003, 3, 6)
               


# In[18]:


birth_rate_calc[0:10]


# In[19]:


ssa_list = read_csv("US_births_2000-2014_SSA.csv")


# In[20]:


ssa_list[0:10]


# In[21]:


def remove_duplicates(dataset_one, dataset_two):
    clean_list = []
    list_one = dataset_one[:]
    list_two = dataset_two[:]
    merged_list = []

    for row_one in list_one:
        year_one = row_one[0]
        month_one = row_one[1]
        dom_one = row_one[2]
        dow_one = row_one[3]
        births_one = row_one[4]
        for row_two in list_two:
            year_two = row_two[0]
            month_two = row_two[1]
            dom_two = row_two[2]
            dow_two = row_two[3]
            births_two = row_two[4]
            if year_one == year_two and month_one == month_two and dom_one == dom_two and dow_one == dow_two:
                avg_births = round((births_one + births_two) / 2.0)
                new_row = [year_one, month_one, dom_one, dow_one, avg_births]
                clean_list.append(new_row)
                list_one_modified = list_one.remove(row_one)
                list_two_modified = list_two.remove(row_two)
    merged_list = list_one + list_two + clean_list
    return merged_list



# In[22]:


cdcssa_merged = remove_duplicates(cdc_list, ssa_list)


# In[28]:


cdcssa_merged[3500:3510]

