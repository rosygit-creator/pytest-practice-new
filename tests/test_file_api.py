# get values from test_file.txt
import json

with open('test_file.txt', 'r') as f:
    input = json.load(f)


    print(input['included'][0]) # or print(input['included']) is same
    print(len(input['included']))

    print(input['included'][0]['id'])
    print(input['included'][0]['attributes'])

    print(input['data'][0]['relationships']['author']['data'])


    # for k,v in input.items():
    #     if k==input['included']:
    #         print(v)
