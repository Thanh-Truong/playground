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

def __format_item(item, json_sample_dict):
    assert(DATA_ITEM_TYPE in item and item[DATA_ITEM_TYPE])
    item_type = item[DATA_ITEM_TYPE]
    formatted_item = copy.deepcopy(json_sample_dict[item_type])
    formatted_item.pop(RECOMMENDATIONS, None)
    if (MOVIE == item_type):
        formatted_item["video_id"] = item[DATA_ITEM_ID]
    elif (SERIES == item_type):
        formatted_item["series_id"] = item[DATA_ITEM_ID]
    else:
        assert(False)

    return formatted_item


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
    json = copy.deepcopy(json_sample)
    if not withRecommendations:
        json.pop(RECOMMENDATIONS, None)
    return json

# ----------------------------------------------------------------------------
# Public methods
# ----------------------------------------------------------------------------
def make_json_series(id, json_sample, withRecommendations=False):
    jseries = __make_json_from_id(id, json_sample, withRecommendations)
    jseries["series_id"] = id
    return jseries

def make_json_movie(id, json_sample, withRecommendations=False):
    jmovie = __make_json_from_id(id, json_sample, withRecommendations)
    jmovie["video_id"] = id
    return jmovie

def make_a_recommendation0(jitem, associated_jitems=[], json_sample_dict={}, 
                        config_file = R13S_CONFIG_JSON):
    "Format a recommendation consisting of an (json) item and its associated (json) items"
    # load conifgurations if not provided 
    if len(json_sample_dict) == 0:
        json_sample_dict = __load_sample_r13s_formats(config_file)

    recommendation = __format_item(jitem, json_sample_dict)
    # associated_items
    if (len(associated_jitems) != 0):
        recommendation[RECOMMENDATIONS] = [__format_item(i, json_sample_dict) 
                                        for i in associated_jitems]
    return recommendation

def format_r13s(config_file = R13S_CONFIG_JSON):
    "Format recommendations"
    json_sample_dict = __load_sample_r13s_formats(config_file)
    return json_sample_dict['r13s_format']

def main():
    r13s = format_r13s()
    data = []
    r13s[DATA_ITEM_DATA] = data
    for video_id in range(1, 5):
        item = {"type": "movie", "id" : str(video_id)}
        associated_items = [  {"type": "movie", "id" : str(other_video_id)} 
                             for other_video_id in range (0, video_id) ]
        data.append(make_a_recommendation0(item, associated_items))
    validate(r13s)
    pprint.pprint(r13s)    

if __name__ == '__main__':
  main()