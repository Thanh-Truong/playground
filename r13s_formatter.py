import json
import copy
import pprint

DATA_ITEM_ID = 'id'
DATA_ITEM_TYPE = 'type'
DATA_ITEM_DATA = 'data'
MOVIE = 'movie'
SERIES = 'series'
R13S_CONFIG_JSON = 'r13s_config.json'
RECOMMENDATIONS = 'recommendations'

def __clone__(o):
    return copy.deepcopy(o)

def __validate(json, json_sample):
    for key, value in json_sample.items():
        acutal_value = json[key]
        assert((type(acutal_value) is type(value)) 
                or (type(acutal_value).__name__ == 'unicode' 
                    and  type(value).__name__ == 'str')
                or (type(acutal_value).__name__ == 'str' 
                    and  type(value).__name__ == 'unicode')) 

def __load_sample_r13s_formats(r13s_filename=R13S_CONFIG_JSON):
    with open(r13s_filename, "r") as f:
        return json.load(f)

def validate(r13s, config_file = R13S_CONFIG_JSON):
    "Validate a JSON (recommendations, r13s) accordingly to a configuration"
    formats = __load_sample_r13s_formats(config_file)
    # validate all top-level fields
    __validate(r13s, formats['r13s_format'])

    # validate all items in data field
    for data_item in r13s[DATA_ITEM_DATA]:
        assert(DATA_ITEM_TYPE in data_item)
        data_item_type = data_item[DATA_ITEM_TYPE]
        __validate(data_item, formats[data_item_type])

def __make_json_from_id(id, json_sample, withRecommendations=False):
    json = __clone__(json_sample)
    if not withRecommendations:
        json.pop(RECOMMENDATIONS, None)
    return json


# ----------------------------------------------------------------------------
# Public methods
# ----------------------------------------------------------------------------
def make_json_series(id, r13s_configs, withRecommendations=False):
    jseries = __make_json_from_id(id, r13s_configs[SERIES], withRecommendations)
    jseries["series_id"] = id
    return jseries

def make_json_movie(id, r13s_configs, withRecommendations=False):
    jmovie = __make_json_from_id(id, r13s_configs[MOVIE], withRecommendations)
    jmovie["video_id"] = id
    return jmovie

def make_r13s(r13s_configs):
    return __clone__(r13s_configs['r13s_format'])

def make_r13s_data(r13s_configs):
    return __clone__(r13s_configs['r13s_format']['data'])

def add_r13s_data_item(data, item, associated_items):
    if isinstance(item, dict):
        item[RECOMMENDATIONS] = [a_item for a_item in associated_items]
    
    if isinstance(data, list):
        data.append(item)
    elif isinstance(data, dict):
        data[item] = [a_item for a_item in associated_items]
        
def main():
    r13s_configs = __load_sample_r13s_formats(R13S_CONFIG_JSON)
    r13s = make_r13s(r13s_configs)
    data = make_r13s_data(r13s_configs)
    r13s[DATA_ITEM_DATA] = data

    for video_id in range(1, 5):
        item = make_json_movie(str(video_id), r13s_configs, True)
        associated_items = [  make_json_movie(str(other_video_id), r13s_configs)
                             for other_video_id in range (0, video_id) ]
        add_r13s_data_item(data, item, associated_items)
    #validate(r13s)
    pprint.pprint(r13s)    

if __name__ == '__main__':
  main()