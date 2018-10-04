import json
import copy
import pprint

DATA_ITEM_TYPE = 'type'
DATA_ITEM_DATA = 'data'
MOVIE = 'movie'
SERIES = 'series'
R13S_CONFIG_JSON = 'r13s_config.json'
R13S_CONFIG1_JSON = 'r13s_config1.json'
RECOMMENDATIONS = 'recommendations'
R13S_FORMAT = 'r13s_format'
SERIES_ID = 'series_id'
MOVIE_ID = 'video_id'

def __clone__(o):
    return copy.deepcopy(o)

def __is_dict(o):
    return isinstance(o, dict)

def __is_str(o):
    return isinstance(o, str) or isinstance(o, unicode)

def __validate(json, json_sample):
    for key, value in json_sample.items():
        acutal_value = json[key]
        assert((type(acutal_value) is type(value)) 
                or (type(acutal_value).__name__ == 'unicode' 
                    and  type(value).__name__ == 'str')
                or (type(acutal_value).__name__ == 'str' 
                    and  type(value).__name__ == 'unicode')) 

def load_sample_r13s_formats(r13s_filename=R13S_CONFIG_JSON):
    with open(r13s_filename, "r") as f:
        return json.load(f)

def validate(r13s, config_file = R13S_CONFIG_JSON):
    "Validate a JSON (recommendations, r13s) accordingly to a configuration"
    formats = load_sample_r13s_formats(config_file)
    # validate all top-level fields
    __validate(r13s, formats[R13S_FORMAT])

    # validate all items in data field
    for data_item in r13s[DATA_ITEM_DATA]:
        assert(DATA_ITEM_TYPE in data_item)
        data_item_type = data_item[DATA_ITEM_TYPE]
        __validate(data_item, formats[data_item_type])

def __make_obj_from_id(id, json_sample, withRecommendations=False):
    obj = __clone__(json_sample)
    if not withRecommendations and __is_dict(obj):
       obj.pop(RECOMMENDATIONS, None)
    if __is_str(obj):
        obj = id
    return obj


# ----------------------------------------------------------------------------
# Public methods
# ----------------------------------------------------------------------------
def make_series(id, r13s_configs, withRecommendations=False):
    series = __make_obj_from_id(id, r13s_configs[SERIES], withRecommendations)
    if __is_dict(series):
        series[SERIES_ID] = id
    return series

def make_movie(id, r13s_configs, withRecommendations=False):
    movie = __make_obj_from_id(id, r13s_configs[MOVIE], withRecommendations)
    if __is_dict(movie):
        movie[MOVIE_ID] = id
    return movie

def make_r13s(r13s_configs):
    return __clone__(r13s_configs[R13S_FORMAT])

def make_r13s_data(r13s_configs):
    return __clone__(r13s_configs[R13S_FORMAT][DATA_ITEM_DATA])

def add_r13s_data_item(data, item, associated_items):
    if __is_dict(item):
        item[RECOMMENDATIONS] = [a_item for a_item in associated_items]
    
    if isinstance(data, list):
        data.append(item)
    elif __is_dict(data):
        data[item] = [a_item for a_item in associated_items]

def test(config_file):
    r13s_configs = load_sample_r13s_formats(config_file)
    r13s = make_r13s(r13s_configs)
    data = make_r13s_data(r13s_configs)
    r13s[DATA_ITEM_DATA] = data

    for video_id in range(1, 5):
        item = make_movie(str(video_id), r13s_configs, True)
        associated_items = [  make_movie(str(other_video_id), r13s_configs)
                             for other_video_id in range (0, video_id) ]
        add_r13s_data_item(data, item, associated_items)
    #validate(r13s)
    pprint.pprint(r13s)   

def main():
    test(R13S_CONFIG_JSON)
    test(R13S_CONFIG1_JSON)     

if __name__ == '__main__':
  main()